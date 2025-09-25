# Copyright (C) 2025 Embedl AB
"""
On-device verification of models via Qualcomm AI Hub. Functionality for
measuring latency and verify outputs on target device.

"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import qai_hub as hub
import torch
from tqdm import tqdm


class BenchmarkError(RuntimeError):
    """Raised on any benchmark related failure."""


@dataclass
class BenchmarkResult:
    latency_ms: Optional[float]
    accuracy_top1: Optional[float]
    device: str
    precision: str


def benchmark_model(
    device_name: str,
    *,
    model_path: Path,
    data_array: Path,
    measure_latency: bool = False,
    output_json: Optional[Path] = None,
    max_samples: Optional[int] = None,
    input_name: str = "input",
) -> BenchmarkResult:
    """
    Benchmark a compiled model file on a target device via Qualcomm AI Hub.
    The user must provide a file path to a numpy or torch array containing the input data.
    Data transforms must be applied by the user before saving the array.

    Args:
        device_name: Name of the device to benchmark on.
        model_path: Path to the compiled model file (.tflite, .bin, .onnx).
        data_array: Path to a .npy or .pt file containing input data (N, ...).
        measure_latency: Whether to measure inference latency.
        output_json: Path to save inference outputs as JSON.
        max_samples: Max number of samples to process from the array.
        input_name: Name of the model input (default: "input").

    Returns:
        BenchmarkResult with latency (ms), device, and precision.
    """
    import json

    device = hub.Device(device_name)
    cmp_model = model_path
    latency_ms = None
    if measure_latency:
        profile_job = hub.submit_profile_job(model=cmp_model, device=device)
        prof = profile_job.download_profile()
        latency_ms = (
            prof["execution_summary"]["estimated_inference_time"] / 1000.0
        )
    if data_array is not None:
        if not data_array.exists():
            raise BenchmarkError(
                f"data_array file does not exist: {data_array}"
            )
        if not data_array.is_file():
            raise BenchmarkError(f"data_array must be a file: {data_array}")
        if not data_array.suffix in [".npy", ".pt", ".pth"]:
            raise BenchmarkError(
                f"data_array must be a .npy or .pt file, got: {data_array.suffix}"
            )
        # Ensure the model is compiled for the target device
        if not cmp_model.exists():
            raise BenchmarkError(
                f"Model file does not exist: {cmp_model}. "
                "Ensure the model is compiled for the target device."
            )
        if not cmp_model.is_file():
            raise BenchmarkError(
                f"Model file must be a file: {cmp_model}. "
                "Ensure the model is compiled for the target device."
            )
        # Load user data (numpy or torch array)
        if str(data_array).endswith(".npy"):
            arr = np.load(data_array)
        elif str(data_array).endswith(".pt") or str(data_array).endswith(
            ".pth"
        ):
            arr = torch.load(data_array)
            if isinstance(arr, torch.Tensor):
                arr = arr.cpu().numpy()
            else:
                raise BenchmarkError("Torch file must contain a tensor.")
        else:
            raise BenchmarkError("data_array must be a .npy or .pt file.")
        # arr shape: (N, ...)
        num_samples = arr.shape[0]
        if max_samples is not None:
            arr = arr[:max_samples]
        # Upload the batch as a dataset for batched inference
        dataset = hub.upload_dataset({input_name: arr})
        job = hub.submit_inference_job(
            model=cmp_model,
            device=device,
            inputs=dataset,
        )
        out: Dict[str, List[np.ndarray]] = job.download_output_data()
        # Save all outputs as a single entry per input
        results = [
            {
                "input_index": i,
                "output": {k: v[i].tolist() for k, v in out.items()},
            }
            for i in range(arr.shape[0])
        ]
        if output_json is None:
            output_json = Path.cwd() / "inference_outputs.json"
        with open(output_json, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)
    precision = model_path.suffix.lstrip(".").lower()
    return BenchmarkResult(latency_ms, None, device.name, precision)
