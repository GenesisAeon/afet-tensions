import sys

import typer
from rich.console import Console
from rich.table import Table

from .benchmark import TENSIONS_TARGETS, run_benchmark
from .system import AFETTensions

app = typer.Typer(help="AFET Tensions — Package 34 CLI")
console = Console()


@app.command()
def run() -> None:
    """Run AFETTensions cycle and display results."""
    system = AFETTensions()
    results = system.run_cycle()

    table = Table(title="AFET Tensions — Cycle Results", show_lines=True)
    table.add_column("Parameter", style="cyan")
    table.add_column("Value", style="green")

    labels = {
        "h0_local": "H₀ local [km/s/Mpc]",
        "h0_cmb": "H₀ CMB [km/s/Mpc]",
        "h0_ratio": "H₀ ratio",
        "s8_z0": "S₈ (z=0)",
        "s8_z_cmb": "S₈ (z=1100)",
        "omega_rig_hz": "Ω_rig [Hz]",
        "gamma_domain": "Γ_domain",
        "ligo_peak_frequency_hz": "LIGO peak freq [Hz]",
        "euclid_s8_z05": "Euclid S₈ (z=0.5)",
        "desi_dv_rd_z051": "DESI DV/rd (z=0.51)",
    }

    for key, value in results.items():
        label = labels.get(key, key)
        table.add_row(label, f"{value:.6f}")

    console.print(table)


@app.command()
def h0_predict(z: float = typer.Option(..., "--z", help="Redshift")) -> None:
    """Predict H₀_eff at redshift z."""
    system = AFETTensions()
    h0 = system.h0_prediction(z)
    console.print(f"H₀_eff(z={z}) = [green]{h0:.4f}[/green] km/s/Mpc")


@app.command()
def s8_predict(z: float = typer.Option(..., "--z", help="Redshift")) -> None:
    """Predict S₈ at redshift z."""
    system = AFETTensions()
    s8 = system.s8_prediction(z)
    console.print(f"S₈(z={z}) = [green]{s8:.4f}[/green]")


@app.command()
def benchmark() -> None:
    """Run all benchmark checks."""
    results = run_benchmark()

    table = Table(title="AFET Tensions — Benchmark", show_lines=True)
    table.add_column("Target", style="cyan")
    table.add_column("Expected", style="yellow")
    table.add_column("Pass", style="green")

    all_pass = True
    for key, passed in results.items():
        target, tol = TENSIONS_TARGETS[key]
        status = "[green]PASS[/green]" if passed else "[red]FAIL[/red]"
        table.add_row(key, f"{target} ± {tol}", status)
        if not passed:
            all_pass = False

    console.print(table)

    if not all_pass:
        console.print("[red]Benchmark FAILED[/red]")
        sys.exit(1)
    else:
        console.print("[green]All benchmarks PASSED[/green]")


@app.command()
def falsification_schedule() -> None:
    """Print falsification timeline."""
    table = Table(title="AFET Tensions — Falsification Schedule", show_lines=True)
    table.add_column("Mission", style="cyan")
    table.add_column("Year", style="yellow")
    table.add_column("Observable", style="white")

    table.add_row("DESI DR2", "2026", "BAO scale DV/rd → H₀ gradient")
    table.add_row("Euclid DR1", "2027", "S₈ weak lensing → CREP evolution")
    table.add_row("LIGO O5", "2028", "GW background peak → Ω_rig ≈ 0.018 Hz")

    console.print(table)
