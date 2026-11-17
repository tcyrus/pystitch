import os
import unittest

import pystitch
from pystitch.EmbConstant import *
from test.pattern_for_tests import get_big_pattern


class TestConverts(unittest.TestCase):

    def position_equals(self, stitches, j, k):
        self.assertEqual(stitches[j][:1], stitches[k][:1])

    def test_convert_gcode_to_u01(self):
        file1 = "convert_u01.gcode"
        file2 = "converted_gcode.u01"
        pystitch.write_gcode(get_big_pattern(), file1)
        f_pattern = pystitch.read_gcode(file1)
        pystitch.write_u01(f_pattern, file2)
        t_pattern = pystitch.read_u01(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(NEEDLE_SET), 16)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("gcode->u01: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_gcode_to_csv(self):
        file1 = "convert_csv.gcode"
        file2 = "converted_gcode.csv"
        pystitch.write_gcode(get_big_pattern(), file1, {"encode": True})
        f_pattern = pystitch.read_gcode(file1)
        pystitch.write_csv(f_pattern, file2)
        t_pattern = pystitch.read_csv(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("gcode->csv: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_gcode_to_exp(self):
        file1 = "convert_exp.gcode"
        file2 = "converted_gcode.exp"
        pystitch.write_gcode(get_big_pattern(), file1)
        f_pattern = pystitch.read_gcode(file1)
        pystitch.write_exp(f_pattern, file2)
        t_pattern = pystitch.read_exp(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("gcode->exp: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_gcode_to_pes(self):
        file1 = "convert_pes.gcode"
        file2 = "converted_gcode.pes"
        pystitch.write_gcode(get_big_pattern(), file1)
        f_pattern = pystitch.read_gcode(file1)
        pystitch.write_pes(f_pattern, file2)
        t_pattern = pystitch.read_pes(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("gcode->pes: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_gcode_to_jef(self):
        file1 = "convert_jef.gcode"
        file2 = "converted_gcode.jef"
        pystitch.write_gcode(get_big_pattern(), file1)
        f_pattern = pystitch.read_gcode(file1)
        pystitch.write_jef(f_pattern, file2)
        t_pattern = pystitch.read_jef(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("gcode->jef: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_gcode_to_pec(self):
        file1 = "convert_pec.gcode"
        file2 = "converted_gcode.pec"
        pystitch.write_gcode(get_big_pattern(), file1)
        f_pattern = pystitch.read_gcode(file1)
        pystitch.write_pec(f_pattern, file2)
        t_pattern = pystitch.read_pec(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("gcode->pec: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_gcode_to_vp3(self):
        file1 = "convert_vp3.gcode"
        file2 = "converted_gcode.vp3"
        pystitch.write_gcode(get_big_pattern(), file1)
        f_pattern = pystitch.read_gcode(file1)
        pystitch.write_vp3(f_pattern, file2)
        t_pattern = pystitch.read_vp3(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("gcode->vp3: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_gcode_to_dst(self):
        file1 = "convert_dst.gcode"
        file2 = "converted_gcode.dst"
        pystitch.write_gcode(get_big_pattern(), file1)
        f_pattern = pystitch.read_gcode(file1)
        pystitch.write_dst(f_pattern, file2)
        t_pattern = pystitch.read_dst(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("gcode->dst: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_gcode_to_gcode(self):
        file1 = "convert_gcode.gcode"
        file2 = "converted_gcode.gcode"
        pystitch.write_gcode(get_big_pattern(), file1)
        f_pattern = pystitch.read_gcode(file1)
        pystitch.write_gcode(f_pattern, file2)
        t_pattern = pystitch.read_gcode(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("gcode->gcode: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_gcode_to_xxx(self):
        file1 = "convert_xxx.gcode"
        file2 = "converted_gcode.xxx"
        pystitch.write_gcode(get_big_pattern(), file1)
        f_pattern = pystitch.read_gcode(file1)
        pystitch.write_xxx(f_pattern, file2)
        t_pattern = pystitch.read_xxx(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("gcode->xxx: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_gcode_to_tbf(self):
        file1 = "convert_tbf.gcode"
        file2 = "converted_gcode.tbf"
        pystitch.write_gcode(get_big_pattern(), file1)
        f_pattern = pystitch.read_gcode(file1)
        pystitch.write_tbf(f_pattern, file2)
        t_pattern = pystitch.read_tbf(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(NEEDLE_SET), 16)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("gcode->tbf: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)
