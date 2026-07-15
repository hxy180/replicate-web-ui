#!/usr/bin/env python3
"""Compare two same-size screenshots and optionally write an amplified diff."""

from __future__ import annotations

import argparse
import math
from pathlib import Path

from PIL import Image, ImageChops, ImageEnhance, ImageStat


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reference", type=Path)
    parser.add_argument("implementation", type=Path)
    parser.add_argument("--diff", type=Path, help="Write an amplified RGB diff image")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    reference = Image.open(args.reference).convert("RGB")
    implementation = Image.open(args.implementation).convert("RGB")

    if reference.size != implementation.size:
        raise SystemExit(
            "Screenshot sizes differ: "
            f"reference={reference.size}, implementation={implementation.size}"
        )

    diff = ImageChops.difference(reference, implementation)
    stats = ImageStat.Stat(diff)
    channel_mse = [value * value for value in stats.rms]
    rmse = math.sqrt(sum(channel_mse) / len(channel_mse))
    similarity = max(0.0, 100.0 * (1.0 - rmse / 255.0))

    grayscale = diff.convert("L")
    changed = sum(
        count for value, count in enumerate(grayscale.histogram()) if value > 8
    )
    changed_ratio = 100.0 * changed / (reference.width * reference.height)

    print(f"size: {reference.width}x{reference.height}")
    print(f"rmse: {rmse:.3f}")
    print(f"similarity: {similarity:.2f}%")
    print(f"changed_pixels_over_threshold: {changed_ratio:.2f}%")

    if args.diff:
        args.diff.parent.mkdir(parents=True, exist_ok=True)
        ImageEnhance.Contrast(diff).enhance(3.0).save(args.diff)
        print(f"diff: {args.diff}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
