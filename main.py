#!/usr/bin/env python3
"""
Entry for make.fun bounty coolest-art-01.

Winning image: A small cute child in cozy pajamas standing on a fluffy cloud, gently stitching a large glowing crescent moon with golden thread and a big needle. The moon is the dominant subject, warm luminous glow, deep blue night sky with a few twinkling stars, minimal clutter, handcrafted storybook feel, luminous storybook sticker art a developer would love on their laptop.
"""
import sys
import os
import struct
import shutil

SRC = "art.png"
DST = "/output/entry.png"
MAX_BYTES = 1024 * 1024  # 1 MiB

def verify_png(path: str) -> tuple[int, int]:
    """Verify PNG via IHDR header, return (width, height)."""
    with open(path, "rb") as f:
        # PNG signature
        sig = f.read(8)
        if sig != b"\x89PNG\r\n\x1a\n":
            raise ValueError("Not a PNG: bad signature")
        # IHDR chunk
        length = struct.unpack(">I", f.read(4))[0]
        if length != 13:
            raise ValueError("Bad IHDR length")
        chunk_type = f.read(4)
        if chunk_type != b"IHDR":
            raise ValueError("Missing IHDR chunk")
        ihdr = f.read(13)
        width, height = struct.unpack(">II", ihdr[:8])
        # CRC (skip)
        f.read(4)
    return width, height

def main() -> int:
    # Verify source
    try:
        w, h = verify_png(SRC)
    except Exception as e:
        print(f"FAIL: {e}", file=sys.stderr)
        return 1

    src_size = os.path.getsize(SRC)
    if src_size > MAX_BYTES:
        print(f"FAIL: source {src_size} bytes exceeds 1 MiB limit", file=sys.stderr)
        return 1

    # Ensure output directory exists
    os.makedirs(os.path.dirname(DST), exist_ok=True)

    # Copy to output
    shutil.copy2(SRC, DST)

    # Verify destination
    dst_size = os.path.getsize(DST)
    if dst_size > MAX_BYTES:
        print(f"FAIL: output {dst_size} bytes exceeds 1 MiB limit", file=sys.stderr)
        return 1

    print(f"OK: {dst_size} bytes, {w}x{h}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
