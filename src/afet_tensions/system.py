from .beta_hierarchy import BetaHierarchyModel
from .crep_redshift import CREPRedshiftEvolution
from .ligo_prediction import LIGOPrediction
from .euclid_prediction import EuclidPrediction
from .desi_prediction import DESIPrediction
from .constants import (
    GAMMA_DOMAIN,
    OMEGA_RIG_HZ,
    S8_WL,
    S8_CMB,
    SIGMA_PHI,
    BETA_LOCAL,
)


class AFETTensions:
    """Diamond interface — GenesisAeon Package 34"""

    PACKAGE_ID = 34
    DOMAIN = "cosmology"
    SCALE = "cosmological"
    ZENODO = "10.5281/zenodo.17472834"

    def __init__(self, z_range: tuple = (0, 10)) -> None:
        self.z_range = z_range
        self.beta_model = BetaHierarchyModel()
        self.crep = CREPRedshiftEvolution()
        self.ligo = LIGOPrediction()
        self.euclid = EuclidPrediction()
        self.desi = DESIPrediction()

    def run_cycle(self, z_range: tuple = (0, 10)) -> dict:
        return {
            "h0_local": self.beta_model.h0_local(),
            "h0_cmb": self.beta_model.h0_cmb(),
            "h0_ratio": self.beta_model.h0_ratio(),
            "s8_z0": self.crep.s8_at_z(0.0),
            "s8_z_cmb": self.crep.s8_at_z(1100.0),
            "omega_rig_hz": OMEGA_RIG_HZ,
            "gamma_domain": GAMMA_DOMAIN,
            "ligo_peak_frequency_hz": self.ligo.peak_frequency(),
            "euclid_s8_z05": self.euclid.s8_predicted(0.5),
            "desi_dv_rd_z051": self.desi.dv_rd_predicted(0.51),
        }

    def get_crep_state(self) -> dict:
        gamma_z0 = self.crep.gamma_at_z(0.0)
        return {
            "C": gamma_z0,
            "R": self.beta_model.h0_ratio() / 1.1,
            "E": S8_WL / S8_CMB,
            "P": 0.8,
            "Gamma": gamma_z0,
        }

    def get_utac_state(self) -> dict:
        return {
            "r": BETA_LOCAL,
            "K": self.beta_model.h0_local(),
            "sigma": SIGMA_PHI * 16,
            "H": self.beta_model.h0_effective(0.0),
        }

    def get_phase_events(self) -> list:
        return [
            {
                "z": 1100.0,
                "event": "beta_domain_switch",
                "description": "CMB β regime → late-universe β regime transition",
                "gamma": GAMMA_DOMAIN,
            },
            {
                "z": 0.5,
                "event": "euclid_survey_depth",
                "description": "Euclid median survey redshift",
                "gamma": self.crep.gamma_at_z(0.5),
            },
            {
                "z": 0.0,
                "event": "present_epoch",
                "description": "Today: weak lensing S₈ measurement epoch",
                "gamma": self.crep.gamma_at_z(0.0),
            },
        ]

    def to_zenodo_record(self) -> dict:
        results = self.run_cycle()
        return {
            "doi": self.ZENODO,
            "package_id": self.PACKAGE_ID,
            "domain": self.DOMAIN,
            "scale": self.SCALE,
            "title": "AFET β-Hierarchie → Kosmologische Spannungen (Hubble, S₈)",
            "results": results,
            "falsification": [
                self.desi.falsification_criterion(),
                self.euclid.falsification_criterion(),
                self.ligo.falsification_criterion(),
            ],
        }

    def h0_prediction(self, z: float) -> float:
        gamma_z = self.crep.gamma_at_z(z)
        gamma_0 = self.crep.gamma_at_z(0.0)
        beta_eff = BETA_LOCAL * (gamma_z / gamma_0) if gamma_0 > 0 else 0.0
        return self.beta_model.h0_effective(beta_eff)

    def s8_prediction(self, z: float) -> float:
        return self.crep.s8_at_z(z)
