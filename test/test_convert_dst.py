import tempfile
import unittest
from pathlib import Path

import pystitch
from pystitch.EmbConstant import *
from test.pattern_for_tests import get_big_pattern


class TestConverts(unittest.TestCase):
    def position_equals(self, stitches, j, k):
        self.assertEqual(stitches[j][:1], stitches[k][:1])

    def test_convert_dst_to_u01(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_u01.dst"
            file2 = Path(tmpdirname) / "converted_dst.u01"

            pystitch.write_dst(pattern, file1)
            f_pattern = pystitch.read_dst(file1)
            pystitch.write_u01(f_pattern, file2)
            t_pattern = pystitch.read_u01(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(NEEDLE_SET), 16)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("dst->u01:", t_pattern.stitches)

    def test_convert_dst_to_csv(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_csv.dst"
            file2 = Path(tmpdirname) / "converted_dst.csv"

            pystitch.write_dst(pattern, file1)
            f_pattern = pystitch.read_dst(file1)
            pystitch.write_csv(f_pattern, file2)
            t_pattern = pystitch.read_csv(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("dst->csv:", t_pattern.stitches)

    def test_convert_dst_to_exp(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_exp.dst"
            file2 = Path(tmpdirname) / "converted_dst.exp"

            pystitch.write_dst(pattern, file1)
            f_pattern = pystitch.read_dst(file1)
            pystitch.write_exp(f_pattern, file2)
            t_pattern = pystitch.read_exp(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("dst->exp:", t_pattern.stitches)

    def test_convert_dst_to_pes(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_pes.dst"
            file2 = Path(tmpdirname) / "converted_dst.pes"

            pystitch.write_dst(pattern, file1)
            f_pattern = pystitch.read_dst(file1)
            pystitch.write_pes(f_pattern, file2)
            t_pattern = pystitch.read_pes(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("dst->pes:", t_pattern.stitches)

    def test_convert_dst_to_jef(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_jef.dst"
            file2 = Path(tmpdirname) / "converted_dst.jef"

            pystitch.write_dst(pattern, file1)
            f_pattern = pystitch.read_dst(file1)
            pystitch.write_jef(f_pattern, file2)
            t_pattern = pystitch.read_jef(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("dst->jef:", t_pattern.stitches)

    def test_convert_dst_to_pec(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_pec.dst"
            file2 = Path(tmpdirname) / "converted_dst.pec"

            pystitch.write_dst(pattern, file1)
            f_pattern = pystitch.read_dst(file1)
            pystitch.write_pec(f_pattern, file2)
            t_pattern = pystitch.read_pec(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("dst->pec:", t_pattern.stitches)

    def test_convert_dst_to_vp3(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_vp3.dst"
            file2 = Path(tmpdirname) / "converted_dst.vp3"

            pystitch.write_dst(pattern, file1)
            f_pattern = pystitch.read_dst(file1)
            pystitch.write_vp3(f_pattern, file2)
            t_pattern = pystitch.read_vp3(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("dst->vp3:", t_pattern.stitches)

    def test_convert_dst_to_dst(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_dst.dst"
            file2 = Path(tmpdirname) / "converted_dst.dst"

            pystitch.write_dst(pattern, file1)
            f_pattern = pystitch.read_dst(file1)
            pystitch.write_dst(f_pattern, file2)
            t_pattern = pystitch.read_dst(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("dst->dst:", t_pattern.stitches)

    def test_convert_dst_to_gcode(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_gcode.dst"
            file2 = Path(tmpdirname) / "converted_dst.gcode"

            pystitch.write_dst(pattern, file1)
            f_pattern = pystitch.read_dst(file1)
            pystitch.write_gcode(f_pattern, file2)
            t_pattern = pystitch.read_gcode(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("dst->gcode:", t_pattern.stitches)

    def test_convert_dst_to_xxx(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_xxx.dst"
            file2 = Path(tmpdirname) / "converted_dst.xxx"

            pystitch.write_dst(pattern, file1)
            f_pattern = pystitch.read_dst(file1)
            pystitch.write_xxx(f_pattern, file2)
            t_pattern = pystitch.read_xxx(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("dst->xxx:", t_pattern.stitches)

    def test_convert_dst_to_tbf(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_tbf.dst"
            file2 = Path(tmpdirname) / "converted_dst.tbf"

            pystitch.write_dst(pattern, file1)
            f_pattern = pystitch.read_dst(file1)
            pystitch.write_tbf(f_pattern, file2)
            t_pattern = pystitch.read_tbf(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(NEEDLE_SET), 16)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("dst->tbf:", t_pattern.stitches)
