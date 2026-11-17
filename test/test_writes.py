import tempfile
import unittest
from pathlib import Path

import pystitch
from pystitch import EmbPattern
from pystitch.EmbConstant import *
from test.pattern_for_tests import get_big_pattern, get_shift_pattern


class TestWrites(unittest.TestCase):

    def position_equals(self, stitches, j, k):
        self.assertEqual(stitches[j][:1], stitches[k][:1])

    def test_write_png(self):
        pattern = get_shift_pattern()
        with tempfile.NamedTemporaryFile(suffix=".png") as fp:
            pystitch.write_png(pattern, fp, {"background": "#F00", "linewidth": 5})

    def test_write_fancy_png(self):
        pattern = get_shift_pattern()
        with tempfile.NamedTemporaryFile(suffix=".png") as fp:
            pystitch.write_png(pattern, fp, {"background": "#F00", "linewidth": 5, "fancy": True})

    def test_write_guides_png(self):
        pattern = get_shift_pattern()
        with tempfile.NamedTemporaryFile(suffix=".png") as fp:
            pystitch.write_png(pattern, fp, {"background": "#F00", "linewidth": 5, "guides": True})

    def test_write_fancy_guides_png(self):
        pattern = get_shift_pattern()
        with tempfile.NamedTemporaryFile(suffix=".png") as fp:
            pystitch.write_png(pattern, fp, {"background": "#F00", "linewidth": 5, "fancy": True,  "guides": True})

    def test_write_dst_read_dst(self):
        pattern = get_big_pattern()

        with tempfile.NamedTemporaryFile(suffix=".dst") as fp:
            pystitch.write_dst(pattern, fp)
            fp.seek(0)
            dst_pattern = pystitch.read_dst(fp)

        self.assertIsNotNone(dst_pattern)
        self.assertEqual(len(dst_pattern.threadlist), 0)
        self.assertEqual(dst_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(dst_pattern.count_stitch_commands(STITCH), 5 * 16)
        self.position_equals(dst_pattern.stitches, 0, -1)
        print("dst: ", dst_pattern.stitches)

    def test_write_exp_read_exp(self):
        pattern = get_big_pattern()

        with tempfile.NamedTemporaryFile(suffix=".exp") as fp:
            pystitch.write_exp(pattern, fp)
            fp.seek(0)
            exp_pattern = pystitch.read_exp(fp)

        self.assertIsNotNone(exp_pattern)
        self.assertEqual(len(exp_pattern.threadlist), 0)
        self.assertEqual(exp_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(exp_pattern.count_stitch_commands(STITCH), 5 * 16)
        self.position_equals(exp_pattern.stitches, 0, -1)
        print("exp: ", exp_pattern.stitches)

    def test_write_vp3_read_vp3(self):
        pattern = get_big_pattern()

        with tempfile.NamedTemporaryFile(suffix=".vp3") as fp:
            pystitch.write_vp3(pattern, fp)
            fp.seek(0)
            vp3_pattern = pystitch.read_vp3(fp)

        self.assertIsNotNone(vp3_pattern)
        self.assertEqual(len(vp3_pattern.threadlist), vp3_pattern.count_stitch_commands(COLOR_CHANGE) + 1)
        self.assertEqual(vp3_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(vp3_pattern.count_stitch_commands(STITCH), 5 * 16)
        self.position_equals(vp3_pattern.stitches, 0, -1)
        print("vp3: ", vp3_pattern.stitches)

    def test_write_jef_read_jef(self):
        pattern = get_big_pattern()

        with tempfile.NamedTemporaryFile(suffix=".jef") as fp:
            pystitch.write_jef(pattern, fp)
            fp.seek(0)
            jef_pattern = pystitch.read_jef(fp)

        self.assertIsNotNone(jef_pattern)
        self.assertEqual(len(jef_pattern.threadlist), jef_pattern.count_stitch_commands(COLOR_CHANGE) + 1)
        self.assertEqual(jef_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(jef_pattern.count_stitch_commands(STITCH), 5 * 16)
        self.position_equals(jef_pattern.stitches, 0, -1)
        print("jef: ", jef_pattern.stitches)

    def test_write_pec_read_pec(self):
        pattern = get_big_pattern()

        with tempfile.NamedTemporaryFile(suffix=".pec") as fp:
            pystitch.write_pec(pattern, fp)
            fp.seek(0)
            pec_pattern = pystitch.read_pec(fp)

        self.assertIsNotNone(pec_pattern)
        self.assertEqual(len(pec_pattern.threadlist), pec_pattern.count_stitch_commands(COLOR_CHANGE) + 1)
        self.assertEqual(pec_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(pec_pattern.count_stitch_commands(STITCH), 5 * 16)
        self.position_equals(pec_pattern.stitches, 0, -1)
        print("pec: ", pec_pattern.stitches)

    def test_write_pes_read_pes(self):
        pattern = get_big_pattern()

        with tempfile.NamedTemporaryFile(suffix=".pes") as fp:
            pystitch.write_pes(pattern, fp)
            fp.seek(0)
            pes_pattern = pystitch.read_pes(fp)

        self.assertIsNotNone(pes_pattern)
        self.assertEqual(len(pes_pattern.threadlist), pes_pattern.count_stitch_commands(COLOR_CHANGE) + 1)
        self.assertEqual(pes_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(pes_pattern.count_stitch_commands(STITCH), 5 * 16)
        self.position_equals(pes_pattern.stitches, 0, -1)
        print("pes: ", pes_pattern.stitches)

    def test_write_xxx_read_xxx(self):
        pattern = get_big_pattern()

        with tempfile.NamedTemporaryFile(suffix=".xxx") as fp:
            pystitch.write_xxx(pattern, fp)
            fp.seek(0)
            pattern = pystitch.read_xxx(fp)

        self.assertIsNotNone(pattern)
        self.assertEqual(len(pattern.threadlist), pattern.count_stitch_commands(COLOR_CHANGE) + 1)
        self.assertEqual(pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(pattern.count_stitch_commands(STITCH), 5 * 16)
        self.position_equals(pattern.stitches, 0, -1)
        print("xxx: ", pattern.stitches)

    def test_write_u01_read_u01(self):
        pattern = get_big_pattern()

        with tempfile.NamedTemporaryFile(suffix=".u01") as fp:
            pystitch.write_u01(pattern, fp)
            fp.seek(0)
            u01_pattern = pystitch.read_u01(fp)

        self.assertIsNotNone(u01_pattern)
        self.assertEqual(len(u01_pattern.threadlist), 0)
        self.assertEqual(u01_pattern.count_stitch_commands(NEEDLE_SET), 16)
        self.assertEqual(u01_pattern.count_stitch_commands(STITCH), 5 * 16)
        self.position_equals(u01_pattern.stitches, 0, -1)
        print("u01: ", u01_pattern.stitches)

    def test_write_csv_read_csv(self):
        pattern = get_big_pattern()

        with tempfile.NamedTemporaryFile(suffix=".csv") as fp:
            pystitch.write_csv(pattern, fp, {"encode": True})
            fp.seek(0)
            csv_pattern = pystitch.read_csv(fp)

        self.assertIsNotNone(csv_pattern)
        self.assertEqual(len(csv_pattern.threadlist), csv_pattern.count_stitch_commands(COLOR_CHANGE) + 1)
        self.assertEqual(csv_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(csv_pattern.count_stitch_commands(STITCH), 5 * 16)
        self.position_equals(csv_pattern.stitches, 0, -1)
        print("csv: ", csv_pattern.stitches)

    def test_write_gcode_read_gcode(self):
        pattern = get_big_pattern()

        with tempfile.NamedTemporaryFile(suffix=".gcode") as fp:
            pystitch.write_gcode(pattern, fp)
            fp.seek(0)
            gcode_pattern = pystitch.read_gcode(fp)

        self.assertIsNotNone(gcode_pattern)
        thread_count = len(gcode_pattern.threadlist)
        change_count = gcode_pattern.count_stitch_commands(COLOR_CHANGE) + 1
        print(thread_count)
        print(change_count)

        self.assertEqual(thread_count, change_count)
        self.assertEqual(gcode_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(gcode_pattern.count_stitch_commands(STITCH), 5 * 16)
        self.position_equals(gcode_pattern.stitches, 0, -1)

    def test_write_txt(self):
        pattern1 = get_big_pattern()
        pattern2 = get_big_pattern()
        with tempfile.NamedTemporaryFile(suffix=".txt") as fp:
            pystitch.write_txt(pattern1, fp)
            fp.seek(0)
            pystitch.write_txt(pattern2, fp, {"mimic": True})

    def test_write_pes_mismatched(self):
        pattern = EmbPattern()
        pattern += "red"
        pattern += "red"
        pattern += "red"
        pattern += (0, 0), (100, 100)
        pattern += COLOR_CHANGE
        pattern += (100, 0), (0, 100)
        pattern += COLOR_CHANGE
        pattern += (0, 0), (100, 100)
        pattern += COLOR_CHANGE
        pattern += (100, 0), (0, 100)
        with tempfile.NamedTemporaryFile(suffix=".pes") as fp:
            pystitch.write_pes(pattern, fp, {"version": "6t"})
            fp.seek(0)
            pystitch.write_pes(pattern, fp)

    def test_pes_writes_stop(self):
        """Test if pes can read/write a stop command."""
        pattern = EmbPattern()
        pattern += "red"
        pattern += (0, 0), (100, 100)
        pattern += STOP
        pattern += (100, 0), (0, 100)
        pattern += "blue"
        pattern += (0, 0), (100, 100)
        pattern += STOP
        pattern += (100, 0), (0, 100)
        with tempfile.NamedTemporaryFile(suffix=".pes") as fp:
            pystitch.write_pes(pattern, fp, {"version": "6t"})
            fp.seek(0)
            loaded = pystitch.read_pes(fp)
        self.assertEqual(pattern.count_stitch_commands(STOP), 2)
        self.assertEqual(pattern.count_stitch_commands(COLOR_CHANGE), 1)
        self.assertEqual(pattern.count_threads(), 2)
        self.assertEqual(loaded.count_stitch_commands(STOP), 2)
        self.assertEqual(loaded.count_stitch_commands(COLOR_CHANGE), 1)
        self.assertEqual(loaded.count_threads(), 2)
