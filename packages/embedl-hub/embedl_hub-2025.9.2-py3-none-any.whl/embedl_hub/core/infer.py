import csv
from pathlib import Path
from typing import Optional

import numpy as np
import qai_hub as hub
import torch
from tqdm import tqdm


def infer(
    model: Path,
    data: Path,
    batch: int = 1,
    dtype: str = "int8",
    out_csv: Path = Path("preds.csv"),
    device_name: str = "default",
    input_name: str = "input",
) -> None:
    """
    Run inference on user data and save predictions to CSV.
    Supports .npy/.pt arrays, image folders, or CSVs (future).
    """
    # For now, only .npy/.pt arrays are supported
    if str(data).endswith(".npy"):
        arr = np.load(data)
    elif str(data).endswith(".pt"):
        arr = torch.load(data)
        if isinstance(arr, torch.Tensor):
            arr = arr.cpu().numpy()
        else:
            raise RuntimeError("Torch file must contain a tensor.")
    else:
        raise RuntimeError("Only .npy or .pt input supported for now.")
    num_samples = arr.shape[0]
    device = hub.Device(device_name)
    results = []
    for i in tqdm(range(0, num_samples, batch), desc="Inferencing"):
        batch_arr = arr[i : i + batch]
        dataset = hub.upload_dataset({input_name: batch_arr})
        job = hub.submit_inference_job(
            model=model, device=device, inputs=dataset
        )
        out = job.download_output_data()
        for j in range(batch_arr.shape[0]):
            row = {k: v[j].tolist() for k, v in out.items()}
            results.append(row)
    # Save to CSV
    with open(out_csv, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        for row in results:
            writer.writerow(row)
