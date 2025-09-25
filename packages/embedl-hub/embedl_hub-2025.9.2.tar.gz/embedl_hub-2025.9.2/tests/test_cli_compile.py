# filepath: /home/andreas/src/embedl-web/apps/sdk/embedl-hub/tests/test_cli_compile.py
# Copyright (C) 2025 Embedl AB

"""Tests for the embedl-hub CLI compile command."""

import pytest  # noqa: F401
from pathlib import Path
from typer.testing import CliRunner

from embedl_hub.cli.compile import compile_cli


runner = CliRunner()


def test_compile_cli_uses_default_output_and_flags(monkeypatch):
    """When --output-file is not provided, CLI computes one from model+runtime.

    Also verifies that flags are forwarded to core.compile.compile_model.
    """

    captured = {}

    def fake_compile_model(model_file, device, runtime, quantize_io, output_file, image_size=None):  # pylint: disable=unused-argument
        captured["args"] = {
            "model_file": model_file,
            "device": device,
            "runtime": runtime,
            "quantize_io": quantize_io,
            "output_file": output_file,
            "image_size": image_size,
        }
        # Late import to avoid importing heavy deps during test collection
        from embedl_hub.core.compile import CompileResult

        return CompileResult(model_path=Path("/tmp/out.tflite"), job_id="job123", device=device)

    monkeypatch.setattr("embedl_hub.core.compile.compile_model", fake_compile_model)

    model_path = Path("/models/int8_model.onnx")
    args = [
        "compile",
        "-m",
        str(model_path),
        "-d",
        "Samsung Galaxy S24",
        "-r",
        "tflite",
    ]

    result = runner.invoke(compile_cli, args)
    assert result.exit_code == 0
    # Should print a message about default output file
    assert "No output file specified" in result.output
    # Should print success line
    assert "Compiled model for Samsung Galaxy S24" in result.output

    forwarded = captured["args"]
    assert Path(forwarded["model_file"]) == model_path
    assert forwarded["device"] == "Samsung Galaxy S24"
    assert forwarded["runtime"] == "tflite"
    assert forwarded["quantize_io"] is False
    # Derived output filename: model.with_suffix('.tflite')
    assert forwarded["output_file"] == model_path.with_suffix(".tflite").as_posix()
    assert forwarded["image_size"] is None


def test_compile_cli_accepts_custom_output_and_options(monkeypatch):
    """CLI forwards custom --output-file, --runtime and --quantize-io correctly."""

    captured = {}

    def fake_compile_model(model_file, device, runtime, quantize_io, output_file, image_size=None):  # pylint: disable=unused-argument
        captured["args"] = {
            "model_file": model_file,
            "device": device,
            "runtime": runtime,
            "quantize_io": quantize_io,
            "output_file": output_file,
            "image_size": image_size,
        }
        from embedl_hub.core.compile import CompileResult

        return CompileResult(model_path=Path("/tmp/out.qnn.bin"), job_id="job456", device=device)

    monkeypatch.setattr("embedl_hub.core.compile.compile_model", fake_compile_model)

    model_path = Path("/models/fp32_model.onnx")
    out_path = "/my/outputs/model.bin"
    args = [
        "compile",
        "-m",
        str(model_path),
        "-d",
        "Samsung Galaxy S24",
        "-r",
        "qnn",
        "--quantize-io",
        "-o",
        out_path,
    ]

    result = runner.invoke(compile_cli, args)
    assert result.exit_code == 0
    assert "Compiled model for Samsung Galaxy S24" in result.output

    forwarded = captured["args"]
    assert Path(forwarded["model_file"]) == model_path
    assert forwarded["device"] == "Samsung Galaxy S24"
    assert forwarded["runtime"] == "qnn"
    assert forwarded["quantize_io"] is True
    assert forwarded["output_file"] == out_path


def test_compile_cli_handles_core_error(monkeypatch):
    """CLI exits with code 1 when core.compile raises CompileError."""

    from embedl_hub.core.compile import CompileError

    def boom(*_args, **_kwargs):  # pylint: disable=unused-argument
        raise CompileError("Failed to submit compile job.")

    monkeypatch.setattr("embedl_hub.core.compile.compile_model", boom)

    result = runner.invoke(
        compile_cli,
        [
            "compile",
            "-m",
            "/models/model.onnx",
            "-d",
            "Samsung Galaxy S24",
        ],
    )

    assert result.exit_code == 1
    assert "Failed to submit compile job." in result.output
