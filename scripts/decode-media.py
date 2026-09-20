"""Decode every approved image; this gate never writes image files."""

import io
from pathlib import Path
import re
import warnings

from PIL import Image, ImageSequence

Image.MAX_IMAGE_PIXELS = 8_000_000
warnings.simplefilter("error", Image.DecompressionBombWarning)
IDENTIFYING_METADATA = re.compile(r"/Users/|[A-Z]:\\Users\\|\.codex|private[_ -]?key|api[_ -]?key", re.I)


def validate_image(file):
    data = Path(file).read_bytes()
    if len(data) > 32 * 1024 * 1024:
        raise ValueError(f"{file}: image exceeds the review limit")
    with Image.open(io.BytesIO(data), formats=["PNG", "GIF"]) as image:
        image.verify()
    with Image.open(io.BytesIO(data), formats=["PNG", "GIF"]) as image:
        if image.n_frames > 64:
            raise ValueError(f"{file}: too many animation frames")
        for value in image.info.values():
            if isinstance(value, str) and IDENTIFYING_METADATA.search(value):
                raise ValueError(f"{file}: potentially identifying metadata requires review")
        for frame in ImageSequence.Iterator(image):
            frame.load()
    return True


if __name__ == "__main__":
    files = sorted((Path(__file__).resolve().parents[1] / "media").iterdir())
    images = [file for file in files if file.suffix in {".png", ".gif"}]
    for file in images:
        validate_image(file)
    print(f"Full decoding and identifying-metadata checks passed for {len(images)} images.")
