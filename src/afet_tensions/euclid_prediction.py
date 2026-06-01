from .crep_redshift import CREPRedshiftEvolution
from .constants import S8_WL


class EuclidPrediction:
    """Euclid DR1 predictions for S₈ and growth rate."""

    def __init__(self) -> None:
        self.crep = CREPRedshiftEvolution()

    def s8_predicted(self, z: float = 0.5) -> float:
        return self.crep.s8_at_z(z)

    def growth_rate_predicted(self, z: float = 0.5) -> float:
        gamma_z = self.crep.gamma_at_z(z)
        return 0.55 * gamma_z

    def falsification_criterion(self) -> dict:
        return {
            "target_s8": S8_WL,
            "tolerance": 0.02,
            "mission": "Euclid DR1",
            "expected_year": 2027,
            "description": "S₈ weak-lensing measurement consistent with AFET CREP evolution",
        }
