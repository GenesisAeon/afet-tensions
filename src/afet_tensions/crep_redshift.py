import math
import numpy as np
from scipy.integrate import solve_ivp
from .constants import GAMMA_DOMAIN, S8_CMB


class CREPRedshiftEvolution:
    def __init__(self, kappa: float = 0.5, gamma_cmb: float = GAMMA_DOMAIN) -> None:
        self.kappa = kappa
        self.gamma_cmb = gamma_cmb
        self._solve()

    def _solve(self) -> None:
        z_span = (1100.0, 0.0)
        z_eval = np.linspace(1100.0, 0.0, 5000)

        def rhs(z: float, y: list) -> list:
            gamma = y[0]
            # dΓ/dz = κ · (1 - Γ) · Γ  (logistic; negative dz direction handled by sign)
            return [-self.kappa * (1.0 - gamma) * gamma]

        sol = solve_ivp(
            rhs,
            z_span,
            [self.gamma_cmb],
            t_eval=z_eval,
            method="RK45",
            rtol=1e-9,
            atol=1e-11,
        )
        self._z_grid = sol.t
        self._gamma_grid = sol.y[0]

    def gamma_at_z(self, z: float) -> float:
        return float(np.interp(z, self._z_grid[::-1], self._gamma_grid[::-1]))

    def gamma_array(self, z_values: np.ndarray) -> np.ndarray:
        return np.interp(z_values, self._z_grid[::-1], self._gamma_grid[::-1])

    def s8_at_z(self, z: float, s8_ref: float = S8_CMB, sigma: float = 2.2) -> float:
        g = self.gamma_at_z(z)
        g_cmb = self.gamma_cmb
        return s8_ref * math.tanh(sigma * g) / math.tanh(sigma * g_cmb)
