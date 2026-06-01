from .constants import OMEGA_RIG_HZ


class LIGOPrediction:
    """Predicted gravitational-wave background from rigid-frame oscillation."""

    def __init__(self) -> None:
        self.omega_rig_hz = OMEGA_RIG_HZ

    def peak_frequency(self) -> float:
        return self.omega_rig_hz

    def snr_estimate(self, observation_years: float = 1.0) -> float:
        return float(2.3 * (observation_years / 1.0) ** 0.5)

    def falsification_criterion(self) -> dict[str, object]:
        return {
            "target_frequency_hz": self.omega_rig_hz,
            "tolerance_hz": 0.002,
            "mission": "LIGO O5",
            "expected_year": 2028,
            "description": "Peak GW background frequency from AFET rigid-frame oscillation",
        }
