import tempfile
import unittest
from pathlib import Path

import pystitch
from pystitch.EmbConstant import *
from test.pattern_for_tests import get_big_pattern


class TestConverts(unittest.TestCase):
    def position_equals(self, stitches, j, k):
        self.assertEqual(stitches[j][:1], stitches[k][:1])

    def test_convert_csv_to_u01(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_u01.csv"
            file2 = Path(tmpdirname) / "converted_csv.u01"

            pystitch.write_csv(pattern, file1)
            f_pattern = pystitch.read_csv(file1)
            pystitch.write_u01(f_pattern, file2)
            t_pattern = pystitch.read_u01(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(NEEDLE_SET), 16)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("csv->u01:", t_pattern.stitches)

    def test_convert_csv_to_csv(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_csv.csv"
            file2 = Path(tmpdirname) / "converted_csv.csv"

            pystitch.write_csv(pattern, file1, {"encode": True})
            f_pattern = pystitch.read_csv(file1)
            pystitch.write_csv(f_pattern, file2)
            t_pattern = pystitch.read_csv(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("csv->csv:", t_pattern.stitches)

    def test_convert_csv_to_exp(self):
        pattern = get_big_pattern()

        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_exp.csv"
            file2 = Path(tmpdirname) / "converted_csv.exp"

            pystitch.write_csv(pattern, file1)
            f_pattern = pystitch.read_csv(file1)
            pystitch.write_exp(f_pattern, file2)
            t_pattern = pystitch.read_exp(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("csv->exp:", t_pattern.stitches)

    def test_convert_csv_to_pes(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_pes.csv"
            file2 = Path(tmpdirname) / "converted_csv.pes"

            pystitch.write_csv(get_big_pattern(), file1)
            f_pattern = pystitch.read_csv(file1)
            pystitch.write_pes(f_pattern, file2)
            t_pattern = pystitch.read_pes(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("csv->pes:", t_pattern.stitches)

    def test_convert_csv_to_jef(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_jef.csv"
            file2 = Path(tmpdirname) / "converted_csv.jef"

            pystitch.write_csv(get_big_pattern(), file1)
            f_pattern = pystitch.read_csv(file1)
            pystitch.write_jef(f_pattern, file2)
            t_pattern = pystitch.read_jef(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("csv->jef:", t_pattern.stitches)

    def test_convert_csv_to_pec(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_pec.csv"
            file2 = Path(tmpdirname) / "converted_csv.pec"

            pystitch.write_csv(get_big_pattern(), file1)
            f_pattern = pystitch.read_csv(file1)
            pystitch.write_pec(f_pattern, file2)
            t_pattern = pystitch.read_pec(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("csv->pec:", t_pattern.stitches)

    def test_convert_csv_to_vp3(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_vp3.csv"
            file2 = Path(tmpdirname) / "converted_csv.vp3"

            pystitch.write_csv(get_big_pattern(), file1)
            f_pattern = pystitch.read_csv(file1)
            pystitch.write_vp3(f_pattern, file2)
            t_pattern = pystitch.read_vp3(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("csv->vp3:", t_pattern.stitches)


    def test_convert_csv_to_dst(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_dst.csv"
            file2 = Path(tmpdirname) / "converted_csv.dst"

            pystitch.write_csv(get_big_pattern(), file1)
            f_pattern = pystitch.read_csv(file1)
            pystitch.write_dst(f_pattern, file2)
            t_pattern = pystitch.read_dst(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("csv->dst:", t_pattern.stitches)

    def test_convert_csv_to_gcode(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_gcode.csv"
            file2 = Path(tmpdirname) / "converted_csv.gcode"

            pystitch.write_csv(get_big_pattern(), file1)
            f_pattern = pystitch.read_csv(file1)
            pystitch.write_gcode(f_pattern, file2)
            t_pattern = pystitch.read_gcode(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("csv->gcode:", t_pattern.stitches)

    def test_convert_csv_to_xxx(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            file1 = Path(tmpdirname) / "convert_xxx.csv"
            file2 = Path(tmpdirname) / "converted_csv.xxx"

            pystitch.write_csv(get_big_pattern(), file1)
            f_pattern = pystitch.read_csv(file1)
            pystitch.write_xxx(f_pattern, file2)
            t_pattern = pystitch.read_xxx(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)

        print("csv->xxx:", t_pattern.stitches)
