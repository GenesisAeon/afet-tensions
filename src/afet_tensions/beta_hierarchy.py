import math

from .constants import BETA_CMB, BETA_LOCAL, GAMMA_DOMAIN, H0_CMB, SIGMA_PHI


class BetaHierarchyModel:
    """
    H₀_eff(β) = H₀_ref · exp(β · σ_Φ · Γ_domain)

    β_local ≈ 1.8 → H₀ ≈ 73.0 km/s/Mpc (late-universe, SNe Ia)
    β_CMB ≈ 0.05 → H₀ ≈ 67.4 km/s/Mpc (early-universe, CMB)
    Ratio: exp((β_local - β_CMB) · σ_Φ · Γ) ≈ 1.083
    """

    def __init__(
        self,
        h0_ref: float = H0_CMB,
        sigma_phi: float = SIGMA_PHI,
        gamma_domain: float = GAMMA_DOMAIN,
    ) -> None:
        self.h0_ref = h0_ref
        self.sigma_phi = sigma_phi
        self.gamma_domain = gamma_domain

    def h0_effective(self, beta: float) -> float:
        return self.h0_ref * math.exp(beta * self.sigma_phi * self.gamma_domain)

    def h0_local(self) -> float:
        return self.h0_effective(BETA_LOCAL)

    def h0_cmb(self) -> float:
        return self.h0_effective(BETA_CMB)

    def h0_ratio(self) -> float:
        return self.h0_local() / self.h0_cmb()

    def beta_from_h0(self, h0_target: float) -> float:
        return math.log(h0_target / self.h0_ref) / (self.sigma_phi * self.gamma_domain)
