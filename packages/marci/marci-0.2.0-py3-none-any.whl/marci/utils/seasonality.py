from __future__ import annotations

import numpy as np
import pandas as pd


class Seasonality:
    def __init__(
        self,
        cv=0.2,
        anchor_date="2000-01-01",
        weekly_harmonics=4,
        monthly_harmonics=1,
        annual_harmonics=5,
        weekly_prominance=1.5,
        monthly_prominance=1.5,
        annual_prominance=4,
        seed=None,
        month_days=30.4375,
        year_days=365.2425,
    ):
        self.cv = cv
        self.anchor_date = pd.Timestamp(anchor_date)
        self.Kw, self.Km, self.Ky = map(
            int, (weekly_harmonics, monthly_harmonics, annual_harmonics)
        )
        self.ww, self.wm, self.wy = (
            float(weekly_prominance),
            float(monthly_prominance),
            float(annual_prominance),
        )
        self.W, self.M, self.Y = 7.0, float(month_days), float(year_days)
        self.rng = np.random.default_rng(seed)

        def ab(K):
            if K <= 0:
                return None, None
            k = np.arange(1, K + 1, dtype=float)
            s = 1 / np.sqrt(k)  # softer higher harmonics
            return self.rng.normal(0, s), self.rng.normal(0, s)

        self.aw, self.bw = ab(self.Kw)
        self.am, self.bm = ab(self.Km)
        self.ay, self.by = ab(self.Ky)

        # Pre-calculate seasonalities for a 4-year cycle (1461 days incl. leap year) to normalize
        self._precalculate_seasonalities()

    def _precalculate_seasonalities(self):
        """Pre-calculate seasonalities for a 4-year cycle and normalize to mean=1 with target CV.

        Using 1461 days (365*4 + 1 leap day) starting at a leap cycle boundary ensures
        that leap-year effects are represented in the base normalization.
        """
        cycle_start = pd.Timestamp("2000-01-01")  # leap-year cycle anchor
        cycle_days = 365 * 4 + 1
        cycle_index = pd.date_range(cycle_start, periods=cycle_days, freq="D")

        # Calculate raw seasonalities
        y = self._raw(cycle_index)

        if self.cv == 0:
            self._normalized_seasonalities = np.ones(cycle_days)
            return

        # Normalize to have mean=1 and target CV on the 4-year cycle
        mu = float(y.mean())
        sd = float(y.std(ddof=0)) or 1.0
        z = (y - mu) / sd
        normalized = 1 + z * self.cv

        self._normalized_seasonalities = normalized

    def _fourier(self, t, period, K, a, b, weight):
        if (K is None) or (K <= 0) or (weight == 0):
            return np.zeros_like(t, dtype=float)
        k = np.arange(1, K + 1, dtype=float)  # (K,)
        omega = 2 * np.pi * k / period  # (K,)
        C = np.cos(t[:, None] * omega[None, :])  # (N,K)
        S = np.sin(t[:, None] * omega[None, :])  # (N,K)
        return weight * (C @ a + S @ b)  # (N,)

    def _raw(self, index: pd.DatetimeIndex) -> np.ndarray:
        # GLOBAL phase anchored to fixed epoch
        t = ((index - self.anchor_date) / pd.Timedelta(days=1)).to_numpy(dtype=float)
        y = (
            self._fourier(t, self.W, self.Kw, self.aw, self.bw, self.ww)
            + self._fourier(t, self.M, self.Km, self.am, self.bm, self.wm)
            + self._fourier(t, self.Y, self.Ky, self.ay, self.by, self.wy)
        )
        return y

    def values(self, index: pd.DatetimeIndex) -> pd.Series:
        """Return seasonalities for timeframe; re-normalize so window mean = 1.

        Uses precomputed 4-year normalized seasonalities and wraps by 1461 days,
        then rescales multiplicatively so the returned series has mean exactly 1.
        """
        if not isinstance(index, pd.DatetimeIndex):
            raise TypeError("index must be a pandas.DatetimeIndex")

        cycle_start = pd.Timestamp("2000-01-01")
        days_from_start = ((index - cycle_start) / pd.Timedelta(days=1)).astype(int)
        cycle_days = 1461
        cycle_idx = days_from_start % cycle_days

        vals = self._normalized_seasonalities[cycle_idx]

        # Ensure mean = 1 over the requested window
        mean_val = float(np.mean(vals)) or 1.0
        vals = vals / mean_val

        return pd.Series(vals, index=index)

    def raw_standardized(self, index: pd.DatetimeIndex) -> pd.Series:
        """Optional helper: window-local z-scored raw trend (mean 0, std 1)."""
        y = self._raw(index)
        sd = float(y.std(ddof=0)) or 1.0
        return pd.Series((y - float(y.mean())) / sd, index=index)
