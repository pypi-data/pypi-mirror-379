from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from .utils.conversion_delay import Conversion_Delay
from .utils.elasticity import Elasticity
from .utils.distributions import (
    Lognormal,
    Beta,
    Lognormal_Ratio,
    safe_poisson,
    safe_binomial,
)
from .utils.seasonality import Seasonality
from .utils.plot_utils import style


class Campaign:
    def __init__(
        self,
        name: str = "Campaign",
        cpm: float = 10,
        cvr: float = 1e-4,
        aov: float = 100,
        cv: float = 0.1,
        start_date: str = "2025-01-01",
        duration: int = 90,
        seasonality_cv: float = 0.2,
        conversion_delay: float = 0.3,
        elasticity: float = 0.9,
        base_budget: float = 1000,
        is_organic: bool = False,
        color: str = None,
    ):
        self.name = name
        self.cpm = cpm
        self.cvr = cvr
        self.aov = aov
        self.cv = cv
        self.start_date = start_date
        self.duration = duration
        self.base_budget = base_budget
        self.is_organic = is_organic
        self.Seasonality = Seasonality(cv=seasonality_cv)
        self.Delay = Conversion_Delay(p=conversion_delay)
        self.Elasticity = Elasticity(elasticity_coef=elasticity)
        self.color = color
        self.df = None

    def __repr__(self):
        return f"Campaign({self.name}, cpm={self.cpm:.1f}, cvr={self.cvr:.3%}, aov={self.aov:.1f}, roas={self.exp_roas():.0%}, start_date={self.start_date}, duration={self.duration})"

    def exp_roas(self, budget: float = None):
        if budget is None:
            budget = self.base_budget
        if self.is_organic:
            return 1000 * self.cvr * self.aov / self.cpm
        elasticity = self.Elasticity.roas(budget / self.base_budget)
        return 1000 * self.cvr * self.aov / self.cpm * elasticity

    def exp_daily_sales(self, budget: float = None):
        if budget is None:
            budget = self.base_budget
        if self.is_organic:
            return 1000 * self.cvr * self.aov / self.cpm * budget
        elasticity = self.Elasticity.roas(budget / self.base_budget)
        return 1000 * self.cvr * self.aov / self.cpm * elasticity * budget

    def exp_tot_sales(self, budget: float = None):
        return self.exp_daily_sales(budget) * self.duration

    def sim_outcomes(
        self,
        start_date: str = "2025-01-01",
        periods: int = 90,
        budget: float = None,
        cv: float = None,
        plot: bool = False,
    ):
        if budget is None:
            budget = self.base_budget
        if cv is None:
            cv = self.cv

        date_range = pd.date_range(start=start_date, periods=periods, name="date")
        df = pd.DataFrame(index=date_range)
        df["name"] = self.name
        df["seasonality"] = self.Seasonality.values(date_range)

        if budget == 0:
            df["base_budget"] = 0
        else:
            Budget = Lognormal(mean=budget, cv=cv, name=f"{self.name}_Budget")
            df["base_budget"] = Budget.generate(periods)
        df["budget"] = df["base_budget"] * df["seasonality"]
        df["budget_relative_to_baseline"] = df["budget"] / self.base_budget
        df["elasticity"] = self.Elasticity.roas(df["budget_relative_to_baseline"])
        elasticity = df["elasticity"] ** (1 / 2)

        CPM = Lognormal(mean=self.cpm * (1 + cv**2), cv=cv, name=f"{self.name}_CPM")
        CVR = Beta(mean=self.cvr, cv=cv, name=f"{self.name}_CVR")
        AOV = Lognormal(mean=self.aov, cv=cv, name=f"{self.name}_AOV")

        df["imps"] = safe_poisson(
            1000 * df["budget"] / CPM.generate(periods) / elasticity
        )
        df["convs"] = safe_binomial(df["imps"], CVR.generate(periods) * elasticity)

        attr_convs = self.Delay.delay(df["convs"])
        df = df.join(attr_convs, how="outer")
        df["aov"] = AOV.generate(periods + self.Delay.duration - 1)
        df["sales"] = df["attr_convs"] * df["aov"]
        mask = df["budget"] > 0
        df.loc[mask, "roas"] = df.loc[mask, "sales"] / df.loc[mask, "budget"]
        df = df[df["attr_convs"] > 0].copy()
        if plot:
            self.plot(df)
        self.df = df
        return df

    def plot(self, df: pd.DataFrame = None):
        if df is None:
            df = self.df

        def plot_seasonality(ax):
            mu = df["seasonality"].mean()
            cv = df["seasonality"].std(ddof=1) / mu
            ax.plot(
                df.index,
                df["seasonality"],
                color="dodgerblue",
                lw=2,
                label=f"mu={mu:.0%}, cv={cv:.0%}",
            )

            ax.axhline(mu, color="gray", lw=1, ls="--")
            style(
                ax,
                "date",
                "%",
                "Date",
                "Seasonality",
                "Seasonality",
            )

        def plot_elasticity_curve(ax):
            self.Elasticity.plot(ax=ax)

        def plot_conversion_delay(ax):
            self.Delay.plot(ax=ax)

        def plot_outcomes(ax):
            for k, v in {"budget": "orangered", "sales": "dodgerblue"}.items():
                mu = df[k].mean()
                cv = df[k].std(ddof=1) / mu
                ax.scatter(df.index, df[k], alpha=0.3, color=v)
                ax.plot(
                    df[k].rolling(window=7).mean(),
                    color=v,
                    lw=2,
                    label=f"{k}: mu={mu:,.0f}, cv={cv:.0%}",
                )
            style(
                ax,
                x_fmt="date",
                x_label="Date",
                title="Outcomes",
                legend=True,
            )

        def plot_elasticity(ax):
            ax.plot(
                df.index,
                df["budget_relative_to_baseline"],
                color="orangered",
                lw=2,
                label="Spend Relative to Baseline",
            )
            ax.plot(
                df.index, df["elasticity"], color="limegreen", lw=2, label="Elasticity"
            )
            style(
                ax,
                "date",
                "%",
                "Date",
                "Elasticity",
                "Elasticity",
            )

        def plot_roas(ax):
            ax.scatter(df.index, df["roas"], alpha=0.3, color="limegreen")
            mu = df["sales"].sum() / df["budget"].sum()
            cv = df["roas"].std(ddof=1) / mu
            ax.plot(
                df["roas"].rolling(window=7).mean(),
                color="limegreen",
                lw=2,
                label=f"mu={mu:.0%}, cv={cv:.0%}",
            )
            ax.axhline(mu, color="gray", lw=1, ls="--")
            style(
                ax,
                "date",
                "%",
                "Date",
                "ROAS",
                "ROAS",
            )

        fig, axs = plt.subplots(2, 3, figsize=(16, 9))
        fig.suptitle(self.name, fontsize=16)
        ax = axs.ravel()

        plot_elasticity_curve(ax[0])
        plot_seasonality(ax[1])
        plot_outcomes(ax[2])
        plot_conversion_delay(ax[3])
        plot_elasticity(ax[4])
        plot_roas(ax[5])
        plt.show()
