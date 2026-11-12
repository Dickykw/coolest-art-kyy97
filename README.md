# coolest-art-01 Entry: Luminous Luna Moth

## The Artwork
A single luminous luna moth with pale green wings glowing from within, perched on a dark mossy branch against a near-black background. The moth's translucent wings spread to fill the frame, emitting an ethereal light that catches the texture of the bark and the delicate wing patterns. This composition follows the winning aesthetic: dark moody night scene, one strong glowing focal point, mythic subject.

## How It Works
`main.py` is a deterministic Python 3.13 standard-library-only program that:
1. Verifies `art.png` is a valid PNG by checking its IHDR header
2. Ensures the source file is ≤ 1 MiB (1,048,576 bytes)
3. Creates `/output` directory if needed
4. Copies `art.png` to `/output/entry.png`
5. Verifies the output file is also ≤ 1 MiB
6. Prints the output size and dimensions

No network, no randomness, no external dependencies beyond Python stdlib.

## Running
```bash
python3 main.py
```
Expected output: `OK: 931448 bytes, 880x880`

## Source Image
The source `art.png` is an 880×880 optimized PNG (931,448 bytes) derived from the generated 1600×1600 luna moth candidate, resized with Lanczos and compressed to fit the 1 MiB limit.