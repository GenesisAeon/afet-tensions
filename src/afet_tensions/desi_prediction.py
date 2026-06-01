from .beta_hierarchy import BetaHierarchyModel
from .crep_redshift import CREPRedshiftEvolution


class DESIPrediction:
    """DESI BAO predictions from AFET β-hierarchy."""

    def __init__(self) -> None:
        self.beta_model = BetaHierarchyModel()
        self.crep = CREPRedshiftEvolution()

    def h0_bao(self, z: float = 0.51) -> float:
        return self.beta_model.h0_effective(
            self.beta_model.beta_from_h0(self.beta_model.h0_local())
            * self.crep.gamma_at_z(z)
            / self.crep.gamma_at_z(0.0)
        )

    def dv_rd_predicted(self, z: float = 0.51) -> float:
        h0 = self.h0_bao(z)
        return 13.36 * (h0 / 73.0) ** (-2 / 3)

    def falsification_criterion(self) -> dict:
        return {
            "mission": "DESI DR2",
            "expected_year": 2026,
            "description": "BAO scale DV/rd consistent with AFET H₀ gradient",
        }
