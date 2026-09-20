import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("decode_media", Path(__file__).with_name("decode-media.py"))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
ROOT = Path(__file__).resolve().parents[1]


class DecodeMediaTests(unittest.TestCase):
    def test_truncated_image_is_rejected_despite_valid_header(self):
        original = (ROOT / "media/variant-noir.png").read_bytes()
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "truncated.png"
            file.write_bytes(original[:100])
            with self.assertRaises((OSError, ValueError, SyntaxError)):
                module.validate_image(file)

    def test_corrupt_chunk_is_rejected(self):
        original = bytearray((ROOT / "media/variant-noir.png").read_bytes())
        original[29] ^= 1  # IHDR checksum: dimensions remain unchanged.
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "corrupt.png"
            file.write_bytes(original)
            with self.assertRaises((OSError, ValueError, SyntaxError)):
                module.validate_image(file)

    def test_archival_animation_decodes_all_frames(self):
        self.assertTrue(module.validate_image(ROOT / "media/auralis-feature-tour.gif"))


if __name__ == "__main__":
    unittest.main()
