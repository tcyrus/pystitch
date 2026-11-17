import tempfile
import unittest
from pathlib import Path

import pystitch
from pystitch.EmbConstant import *
from test.pattern_for_tests import get_big_pattern


class TestConverts(unittest.TestCase):

    def position_equals(self, stitches, j, k):
        self.assertEqual(stitches[j][:1], stitches[k][:1])

    def test_convert_exp_to_u01(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_u01.exp"
            file2 = Path(tmpdirname) / "converted_exp.u01"

            pystitch.write_exp(pattern, file1)
            f_pattern = pystitch.read_exp(file1)
            pystitch.write_u01(f_pattern, file2)
            t_pattern = pystitch.read_u01(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(NEEDLE_SET), 16)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("exp->u01:", t_pattern.stitches)

    def test_convert_exp_to_csv(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_csv.exp"
            file2 = Path(tmpdirname) / "converted_exp.csv"

            pystitch.write_exp(pattern, file1)
            f_pattern = pystitch.read_exp(file1)
            pystitch.write_csv(f_pattern, file2)
            t_pattern = pystitch.read_csv(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("exp->csv:", t_pattern.stitches)

    def test_convert_exp_to_exp(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_exp.exp"
            file2 = Path(tmpdirname) / "converted_exp.exp"

            pystitch.write_exp(pattern, file1)
            f_pattern = pystitch.read_exp(file1)
            pystitch.write_exp(f_pattern, file2)
            t_pattern = pystitch.read_exp(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("exp->exp:", t_pattern.stitches)

    def test_convert_exp_to_pes(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_pes.exp"
            file2 = Path(tmpdirname) / "converted_exp.pes"

            pystitch.write_exp(pattern, file1)
            f_pattern = pystitch.read_exp(file1)
            pystitch.write_pes(f_pattern, file2)
            t_pattern = pystitch.read_pes(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("exp->pes:", t_pattern.stitches)

    def test_convert_exp_to_jef(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_jef.exp"
            file2 = Path(tmpdirname) / "converted_exp.jef"

            pystitch.write_exp(pattern, file1)
            f_pattern = pystitch.read_exp(file1)
            pystitch.write_jef(f_pattern, file2)
            t_pattern = pystitch.read_jef(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("exp->jef:", t_pattern.stitches)

    def test_convert_exp_to_pec(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_pec.exp"
            file2 = Path(tmpdirname) / "converted_exp.pec"

            pystitch.write_exp(pattern, file1)
            f_pattern = pystitch.read_exp(file1)
            pystitch.write_pec(f_pattern, file2)
            t_pattern = pystitch.read_pec(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("exp->pec:", t_pattern.stitches)

    def test_convert_exp_to_vp3(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_vp3.exp"
            file2 = Path(tmpdirname) / "converted_exp.vp3"

            pystitch.write_exp(pattern, file1)
            f_pattern = pystitch.read_exp(file1)
            pystitch.write_vp3(f_pattern, file2)
            t_pattern = pystitch.read_vp3(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("exp->vp3:", t_pattern.stitches)

    def test_convert_exp_to_dst(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_dst.exp"
            file2 = Path(tmpdirname) / "converted_exp.dst"

            pystitch.write_exp(pattern, file1)
            f_pattern = pystitch.read_exp(file1)
            pystitch.write_dst(f_pattern, file2)
            t_pattern = pystitch.read_dst(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("exp->dst:", t_pattern.stitches)

    def test_convert_exp_to_gcode(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_gcode.exp"
            file2 = Path(tmpdirname) / "converted_exp.gcode"

            pystitch.write_exp(pattern, file1)
            f_pattern = pystitch.read_exp(file1)
            pystitch.write_gcode(f_pattern, file2)
            t_pattern = pystitch.read_gcode(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("exp->gcode:", t_pattern.stitches)

    def test_convert_exp_to_xxx(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_xxx.exp"
            file2 = Path(tmpdirname) / "converted_exp.xxx"

            pystitch.write_exp(pattern, file1)
            f_pattern = pystitch.read_exp(file1)
            pystitch.write_xxx(f_pattern, file2)
            t_pattern = pystitch.read_xxx(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("exp->xxx:", t_pattern.stitches)

    def test_convert_exp_to_tbf(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_tbf.exp"
            file2 = Path(tmpdirname) / "converted_exp.tbf"

            pystitch.write_exp(pattern, file1)
            f_pattern = pystitch.read_exp(file1)
            pystitch.write_tbf(f_pattern, file2)
            t_pattern = pystitch.read_tbf(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(NEEDLE_SET), 16)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("exp->tbf:", t_pattern.stitches)
