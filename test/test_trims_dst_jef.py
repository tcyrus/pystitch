import tempfile
import unittest

import pystitch
from pystitch.EmbConstant import *
from test.pattern_for_tests import get_fractal_pattern


class TestTrims(unittest.TestCase):

    def test_dst_trims(self):
        pattern = get_fractal_pattern()

        with tempfile.NamedTemporaryFile(suffix=".dst") as fp:
            pystitch.write_dst(pattern, fp)
            fp.seek(0)
            loaded_pattern = pystitch.read_dst(fp)

        self.assertIsNotNone(loaded_pattern)
        self.assertNotEqual(loaded_pattern.count_stitch_commands(TRIM), 0)

    def test_dst_trims_fail(self):
        pattern = get_fractal_pattern()

        with tempfile.NamedTemporaryFile(suffix=".dst") as fp:
            pystitch.write_dst(pattern, fp)
            fp.seek(0)
            # Lines beyond 50 jumps get a trim.
            loaded_pattern = pystitch.read_dst(fp, {"trim_at": 50})

        self.assertIsNotNone(loaded_pattern)
        self.assertEqual(loaded_pattern.count_stitch_commands(TRIM), 0)

    def test_dst_trims_success(self):
        pattern = get_fractal_pattern()

        with tempfile.NamedTemporaryFile(suffix=".dst") as fp:
            # We make trim jumps big enough.
            pystitch.write_dst(pattern, fp, {"trim_at": 50})
            fp.seek(0)
            # Lines beyond 50 jumps get a trim.
            loaded_pattern = pystitch.read_dst(fp, {"trim_at": 50, "clipping": False})

        self.assertIsNotNone(loaded_pattern)
        self.assertNotEqual(loaded_pattern.count_stitch_commands(TRIM), 0)

    def test_jef_trims(self):
        pattern = get_fractal_pattern()

        with tempfile.NamedTemporaryFile(suffix=".jef") as fp:
            pystitch.write_jef(pattern, fp)
            fp.seek(0)
            loaded_pattern = pystitch.read_jef(fp)

        self.assertIsNotNone(loaded_pattern)
        self.assertNotEqual(loaded_pattern.count_stitch_commands(TRIM), 0)

    def test_jef_trims_off(self):
        pattern = get_fractal_pattern()

        with tempfile.NamedTemporaryFile(suffix=".jef") as fp:
            pystitch.write_jef(pattern, fp)
            fp.seek(0)
            loaded_pattern = pystitch.read_jef(fp, {"trim_distance": None})

        self.assertIsNotNone(loaded_pattern)
        self.assertEqual(loaded_pattern.count_stitch_commands(JUMP), 15)
        self.assertEqual(loaded_pattern.count_stitch_commands(TRIM), 0)

    def test_jef_trims_commands(self):
        # inkstitch also counts single zero-length jumps as trims
        pattern = get_fractal_pattern()

        with tempfile.NamedTemporaryFile(suffix=".jef") as fp:
            pystitch.write_jef(pattern, fp, {"trims": True})
            fp.seek(0)

            loaded_pattern = pystitch.read_jef(fp, {"trim_distance": None})
            fp.seek(0)

            self.assertEqual(loaded_pattern.count_stitch_commands(JUMP), 15)
            # self.assertEqual(loaded_pattern.count_stitch_commands(TRIM), 0)
            self.assertEqual(loaded_pattern.count_stitch_commands(TRIM), 6)

            loaded_pattern = pystitch.read_jef(fp, {"trim_distance": None, "clipping": False})
            fp.seek(0)

            # self.assertEqual(loaded_pattern.count_stitch_commands(JUMP), 21)
            # self.assertEqual(loaded_pattern.count_stitch_commands(TRIM), 0)
            self.assertEqual(loaded_pattern.count_stitch_commands(JUMP), 15)
            self.assertEqual(loaded_pattern.count_stitch_commands(TRIM), 6)

            loaded_pattern = pystitch.read_jef(fp, {"trim_distance": None, "clipping": False, "trims": True, })
            fp.seek(0)

            # self.assertEqual(loaded_pattern.count_stitch_commands(JUMP), 21)
            # self.assertEqual(loaded_pattern.count_stitch_commands(TRIM), 2)
            self.assertEqual(loaded_pattern.count_stitch_commands(JUMP), 15)
            self.assertEqual(loaded_pattern.count_stitch_commands(TRIM), 6)

            loaded_pattern = pystitch.read_jef(fp, {"trim_distance": None, "trims": True})
            fp.seek(0)

            self.assertEqual(loaded_pattern.count_stitch_commands(JUMP), 15)
            # self.assertEqual(loaded_pattern.count_stitch_commands(TRIM), 2)
            self.assertEqual(loaded_pattern.count_stitch_commands(TRIM), 6)
