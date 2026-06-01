from .beta_hierarchy import BetaHierarchyModel
from .constants import H0_LOCAL, H0_CMB, H0_RATIO


class HubbleTensionModel:
    def __init__(self) -> None:
        self.beta_model = BetaHierarchyModel()

    def h0_local(self) -> float:
        return self.beta_model.h0_local()

    def h0_cmb(self) -> float:
        return self.beta_model.h0_cmb()

    def tension_sigma(self) -> float:
        sigma_local = 1.04
        sigma_cmb = 0.5
        import math
        combined_sigma = math.sqrt(sigma_local**2 + sigma_cmb**2)
        return abs(H0_LOCAL - H0_CMB) / combined_sigma

    def afet_explanation(self) -> str:
        return (
            f"AFET β-hierarchy: β_local={1.8} → H₀={self.h0_local():.2f}, "
            f"β_CMB={0.05} → H₀={self.h0_cmb():.2f}, "
            f"ratio={H0_RATIO:.4f}"
        )
