from pathlib import Path

import typer
from rich import print

from embedl_hub.core.infer import infer

infer_cli = typer.Typer(help="Run inference on your data")


@infer_cli.command("infer")
def infer_cmd(
    model: Path = typer.Option(
        ...,
        "-m",
        "--model",
        help="Path to compiled model file (.tflite, .onnx, or .bin)",
    ),
    data: Path = typer.Option(
        ...,
        "-d",
        "--data",
        help="Path to .npy or .pt file containing input data",
    ),
    batch: int = typer.Option(
        1, "-b", "--batch", help="Batch size", show_default=True
    ),
    dtype: str = typer.Option(
        "int8", "--dtype", help="Data type (int8 or fp32)", show_default=True
    ),
    save_csv: Path = typer.Option(
        "preds.csv",
        "--save-csv",
        help="Path to save predictions CSV",
        show_default=True,
    ),
    device: str = typer.Option(
        "default", "--device", "-D", help="Device name", show_default=True
    ),
    input_name: str = typer.Option(
        "input",
        "--input-name",
        help="Name of the model input (default: 'input')",
        show_default=True,
    ),
):
    """Run inference on your data and save predictions to CSV."""
    infer(model, data, batch, dtype, save_csv, device, input_name)
    print(f"[green]✓ Predictions saved to:[/] {save_csv}")
