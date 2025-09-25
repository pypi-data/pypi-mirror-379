from __future__ import annotations

import pandas as pd
from typing import TYPE_CHECKING
import numpy as np
from scipy.optimize import minimize
from matplotlib.colors import to_hex
from itertools import cycle
import matplotlib.pyplot as plt
from .plot_utils import style

if TYPE_CHECKING:
    from ..campaigns import Campaign


class Portfolio:
    def __init__(self, campaigns: list[Campaign]):
        colors = cycle([to_hex(c) for c in plt.get_cmap("tab20").colors])
        self.campaigns = {c.name: c for c in campaigns}
        for c in campaigns:
            if c.color is None:
                c.color = next(colors)
        self.names = [c.name for c in campaigns]
        self.organic_campaigns = [c for c in campaigns if c.is_organic]
        self.organic_names = [c.name for c in self.organic_campaigns]
        self.paid_campaigns = [c for c in campaigns if not c.is_organic]
        self.paid_names = [c.name for c in self.paid_campaigns]
        self.df = None

    def print_stats(self, budgets: dict[str, float] = None):
        columns = [
            "base_budget",
            "base_sales",
            "base_roas",
            "budget",
            "elasticity",
            "exp_roas",
            "exp_sales",
        ]
        df = pd.DataFrame(columns=columns)
        for c in self.paid_campaigns:
            df.loc[c.name, "base_budget"] = c.base_budget
            df.loc[c.name, "base_sales"] = c.exp_daily_sales()
            df.loc[c.name, "base_roas"] = c.exp_roas()
            df.loc[c.name, "budget"] = (
                budgets[c.name] if budgets is not None else c.base_budget
            )
            df.loc[c.name, "elasticity"] = c.Elasticity.roas(
                df.loc[c.name, "budget"] / c.base_budget
            )

            df.loc[c.name, "exp_roas"] = c.exp_roas(df.loc[c.name, "budget"])
            df.loc[c.name, "exp_sales"] = c.exp_daily_sales(df.loc[c.name, "budget"])
        for c in self.organic_campaigns:
            df.loc[c.name, "base_sales"] = c.exp_daily_sales()
            df.loc[c.name, "exp_sales"] = c.exp_daily_sales()
        for col in ["base_budget", "base_sales", "budget", "exp_sales"]:
            df.loc["total", col] = df[col].sum()
        df.loc["total", "base_roas"] = (
            df.loc["total", "base_sales"] / df.loc["total", "base_budget"]
        )
        df.loc["total", "exp_roas"] = (
            df.loc["total", "exp_sales"] / df.loc["total", "base_budget"]
        )
        df_fmt = df.map(lambda x: f"{x:.2f}")
        print(df_fmt.to_string())

    def exp_paid_sales(self, budgets: np.ndarray):
        sales = [c.exp_daily_sales(b) for c, b in zip(self.paid_campaigns, budgets)]
        return np.sum(sales)

    def find_optimal_budgets(self, total_budget: float):
        def obj_fun(share_of_wallet: np.ndarray):
            share_of_wallet = np.asarray(share_of_wallet)
            budgets = share_of_wallet * total_budget
            sales = self.exp_paid_sales(budgets)
            roas = sales / total_budget - 1
            return -roas

        x0 = [1 / len(self.paid_campaigns) for _ in range(len(self.paid_campaigns))]
        bounds = [(0, 1) for _ in range(len(self.paid_campaigns))]
        constraints = {"type": "eq", "fun": lambda x: np.sum(x) - 1}
        res = minimize(obj_fun, x0, bounds=bounds, constraints=constraints)
        optimial_budget_allocation = {
            name: float(res.x[i] * total_budget)
            for i, name in enumerate(self.paid_names)
        }

        return optimial_budget_allocation

    def sim_outcomes(self, budgets: dict[str, float] = None):
        if budgets is None:
            budgets = {name: c.base_budget for name, c in self.campaigns.items()}
        for name, budget in budgets.items():
            self.campaigns[name].sim_outcomes(budget=budget)
        df = pd.concat([c.df for c in self.campaigns.values()])
        self.df = df
        return df

    def plot(self, df: pd.DataFrame = None):
        if df is None:
            df = self.df
        df = df.reset_index(names="date")

        fig, ax = plt.subplots(1, 2, figsize=(15, 5))

        def stacked_bar_plot(ax, col):
            pt = df.pivot_table(col, "date", "name", "sum", 0)
            cum_sales = pd.Series(0, index=pt.index)
            for c in self.campaigns.values():
                if c.name in pt.columns:
                    ax.bar(
                        pt.index,
                        pt[c.name],
                        width=1,
                        bottom=cum_sales,
                        color=c.color,
                        label=f"{c.name}:\n{pt[c.name].mean():,.0f}",
                        alpha=0.5,
                    )
                    cum_sales += pt[c.name]
            tot = pt.sum(axis=1)
            tot_rolling = tot.rolling(window=7).mean()
            ax.plot(
                pt.index,
                tot_rolling,
                lw=2,
                label=f"Total:\n{tot.mean():,.0f}",
                color="black",
            )

        stacked_bar_plot(ax[0], "budget")
        style(
            ax[0],
            "date",
            "$",
            "Date",
            "Sales",
            "Sales",
            legend_loc="r",
        )
        stacked_bar_plot(ax[1], "sales")
        style(
            ax[1],
            "date",
            "$",
            "Date",
            "Sales",
            "Sales",
            legend_loc="r",
        )
        plt.show()
