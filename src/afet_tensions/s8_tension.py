from .constants import S8_CMB, S8_WL
from .crep_redshift import CREPRedshiftEvolution


class S8TensionModel:
    def __init__(self) -> None:
        self.crep = CREPRedshiftEvolution()

    def s8_late(self) -> float:
        return self.crep.s8_at_z(0.0)

    def s8_early(self) -> float:
        return self.crep.s8_at_z(1100.0)

    def tension_sigma(self) -> float:
        sigma_wl = 0.013
        sigma_cmb = 0.013
        import math
        combined = math.sqrt(sigma_wl**2 + sigma_cmb**2)
        return abs(S8_CMB - S8_WL) / combined

    def afet_explanation(self) -> str:
        return (
            f"AFET CREP evolution: S₈(z=0)={self.s8_late():.3f} (WL), "
            f"S₈(z=1100)={self.s8_early():.3f} (CMB)"
        )
