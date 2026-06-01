from .system import AFETTensions

TENSIONS_TARGETS: dict[str, tuple[float, float]] = {
    "h0_local_km_s_mpc": (73.0, 0.5),
    "h0_cmb_km_s_mpc": (67.4, 0.3),
    "h0_ratio": (1.083, 0.01),
    "s8_z0": (0.76, 0.02),
    "s8_z_cmb": (0.83, 0.01),
    "ligo_omega_rig_Hz": (0.018, 0.002),
}


def run_benchmark() -> dict[str, bool]:
    system = AFETTensions()
    cycle = system.run_cycle()

    mapping = {
        "h0_local_km_s_mpc": cycle["h0_local"],
        "h0_cmb_km_s_mpc": cycle["h0_cmb"],
        "h0_ratio": cycle["h0_ratio"],
        "s8_z0": cycle["s8_z0"],
        "s8_z_cmb": cycle["s8_z_cmb"],
        "ligo_omega_rig_Hz": cycle["omega_rig_hz"],
    }

    results = {}
    for key, (target, tol) in TENSIONS_TARGETS.items():
        value = mapping[key]
        results[key] = abs(value - target) <= tol

    return results
