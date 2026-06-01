import pytest
from afet_tensions import AFETTensions, BetaHierarchyModel, CREPRedshiftEvolution
from afet_tensions import constants
from afet_tensions.benchmark import run_benchmark, TENSIONS_TARGETS


def test_constants_physically_reasonable():
    assert 60.0 < constants.H0_LOCAL < 80.0
    assert 60.0 < constants.H0_CMB < 75.0
    assert 1.0 < constants.H0_RATIO < 1.2
    assert 0.0 < constants.SIGMA_PHI < 1.0
    assert 0.0 < constants.GAMMA_DOMAIN < 2.0
    assert 0.0 < constants.OMEGA_RIG_HZ < 1.0


def test_beta_hierarchy_h0_ratio():
    model = BetaHierarchyModel()
    assert abs(model.h0_ratio() - 1.083) <= 0.01


def test_beta_hierarchy_h0_local():
    model = BetaHierarchyModel()
    assert abs(model.h0_local() - 73.0) <= 0.5


def test_beta_hierarchy_h0_cmb():
    model = BetaHierarchyModel()
    assert abs(model.h0_cmb() - 67.4) <= 0.3


def test_beta_hierarchy_inverse():
    model = BetaHierarchyModel()
    h0_target = 70.0
    beta = model.beta_from_h0(h0_target)
    assert abs(model.h0_effective(beta) - h0_target) < 0.01


def test_crep_gamma_decreases_toward_z0():
    crep = CREPRedshiftEvolution()
    assert crep.gamma_at_z(0) < crep.gamma_at_z(1100)


def test_crep_s8_at_z0():
    crep = CREPRedshiftEvolution()
    assert abs(crep.s8_at_z(0) - 0.76) <= 0.02


def test_crep_s8_at_z_cmb():
    crep = CREPRedshiftEvolution()
    assert abs(crep.s8_at_z(1100) - 0.83) <= 0.01


def test_run_cycle_keys():
    system = AFETTensions()
    result = system.run_cycle()
    expected_keys = [
        "h0_local", "h0_cmb", "h0_ratio", "s8_z0", "s8_z_cmb",
        "omega_rig_hz", "gamma_domain",
    ]
    for key in expected_keys:
        assert key in result, f"Missing key: {key}"


def test_get_crep_state_gamma_range():
    system = AFETTensions()
    state = system.get_crep_state()
    assert 0.0 <= state["Gamma"] <= 1.0


def test_benchmark_all_pass():
    results = run_benchmark()
    for key, passed in results.items():
        assert passed, f"Benchmark failed for {key}"


def test_h0_prediction():
    system = AFETTensions()
    h0_z0 = system.h0_prediction(0.0)
    h0_z5 = system.h0_prediction(5.0)
    assert h0_z0 > 0
    assert h0_z5 > 0


def test_s8_prediction():
    system = AFETTensions()
    s8_z0 = system.s8_prediction(0.0)
    s8_z1100 = system.s8_prediction(1100.0)
    assert abs(s8_z0 - 0.76) <= 0.02
    assert abs(s8_z1100 - 0.83) <= 0.01
