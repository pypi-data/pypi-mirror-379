# Copyright (C) 2025 Embedl AB
from pathlib import Path

import typer
from rich import print

from embedl_hub.core.old_benchmark import BenchmarkError, benchmark_model
from embedl_hub.core.hardware.qualcomm_ai_hub import print_device_table

benchmark_cli = typer.Typer(
    name="benchmark",
    help="On-device verification of latency and/or accuracy.",
    invoke_without_command=True,
    no_args_is_help=True,
)


@benchmark_cli.callback()
def benchmark_default(
    ctx: typer.Context,
    model: Path = typer.Option(
        ...,
        "-m",
        "--model",
        help="Path to compiled model file for target engine: .tflite (tflite), .onnx (onnxruntime), or .bin (qnn)",
        show_default=False,
    ),
    device: str = typer.Option(
        ...,
        "-d",
        "--device",
        help="Device name, see options with command `list-device`",
        show_default=False,
    ),
    data_array: Path = typer.Option(
        None,
        "--data-array",
        "-a",
        help="Path to .npy or .pt file containing preprocessed input data (N, ...)",
    ),
    output_json: Path = typer.Option(
        None, "--output-json", help="Path to save inference outputs as JSON"
    ),
    max_samples: int = typer.Option(
        None,
        "--max-samples",
        help="Max number of samples to process from the array",
    ),
    input_name: str = typer.Option(
        "input",
        "--input-name",
        help="Name of the model input (default: 'input'). Use e.g. 'input.1' if required by your model.",
    ),
):
    if ctx.invoked_subcommand:
        return

    if data_array is None:
        print(
            "[red]Error: --save-inference requires --data-array <file> (.npy or .pt)"
        )
        raise typer.Exit(1)

    try:
        res = benchmark_model(
            device_name=device,
            model_path=model,
            data_array=data_array,
            measure_latency=True,
            output_json=output_json,
            max_samples=max_samples,
            input_name=input_name,
        )
        if res.latency_ms is not None:
            print(f"[green]✓ Latency:[/] {res.latency_ms:.2f} ms")
        if data_array:
            print(
                f"[green]✓ Inference outputs saved to:[/] {output_json or 'inference_outputs.json'}"
            )
        print(f"Device: {res.device}  •  Precision: {res.precision}")
    except BenchmarkError as e:
        print(f"[red]✗ Benchmark error:[/] {e}")
        raise typer.Exit(1)


@benchmark_cli.command("list-devices")
def list_devices():
    """Show available device targets and exit."""
    print_device_table()
