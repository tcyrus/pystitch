import os
import unittest

import pystitch
from pystitch.EmbConstant import *
from test.pattern_for_tests import get_big_pattern


class TestConverts(unittest.TestCase):

    def position_equals(self, stitches, j, k):
        self.assertEqual(stitches[j][:1], stitches[k][:1])

    def test_convert_xxx_to_u01(self):
        file1 = "convert_u01.xxx"
        file2 = "converted_xxx.u01"
        pystitch.write_xxx(get_big_pattern(), file1)
        f_pattern = pystitch.read_xxx(file1)
        pystitch.write_u01(f_pattern, file2)
        t_pattern = pystitch.read_u01(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(NEEDLE_SET), 16)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("xxx->u01: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_xxx_to_csv(self):
        file1 = "convert_csv.xxx"
        file2 = "converted_xxx.csv"
        pystitch.write_xxx(get_big_pattern(), file1)
        f_pattern = pystitch.read_xxx(file1)
        pystitch.write_csv(f_pattern, file2)
        t_pattern = pystitch.read_csv(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("xxx->csv: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_xxx_to_exp(self):
        file1 = "convert_exp.xxx"
        file2 = "converted_xxx.exp"
        pystitch.write_xxx(get_big_pattern(), file1)
        f_pattern = pystitch.read_xxx(file1)
        pystitch.write_exp(f_pattern, file2)
        t_pattern = pystitch.read_exp(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("xxx->exp: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_xxx_to_vp3(self):
        file1 = "convert_vp3.xxx"
        file2 = "converted_xxx.vp3"
        pystitch.write_xxx(get_big_pattern(), file1)
        f_pattern = pystitch.read_xxx(file1)
        pystitch.write_vp3(f_pattern, file2)
        t_pattern = pystitch.read_vp3(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("xxx->vp3: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_xxx_to_jef(self):
        file1 = "convert_jef.xxx"
        file2 = "converted_xxx.jef"
        pystitch.write_xxx(get_big_pattern(), file1)
        f_pattern = pystitch.read_xxx(file1)
        pystitch.write_jef(f_pattern, file2)
        t_pattern = pystitch.read_jef(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("xxx->jef: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_xxx_to_pec(self):
        file1 = "convert_pec.xxx"
        file2 = "converted_xxx.pec"
        pystitch.write_xxx(get_big_pattern(), file1)
        f_pattern = pystitch.read_xxx(file1)
        pystitch.write_pec(f_pattern, file2)
        t_pattern = pystitch.read_pec(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("xxx->pec: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_xxx_to_xxx(self):
        file1 = "convert_xxx.xxx"
        file2 = "converted_xxx.xxx"
        pystitch.write_xxx(get_big_pattern(), file1)
        f_pattern = pystitch.read_xxx(file1)
        pystitch.write_xxx(f_pattern, file2)
        t_pattern = pystitch.read_xxx(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("xxx->xxx: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_xxx_to_dst(self):
        file1 = "convert_dst.xxx"
        file2 = "converted_xxx.dst"
        pystitch.write_xxx(get_big_pattern(), file1)
        f_pattern = pystitch.read_xxx(file1)
        pystitch.write_dst(f_pattern, file2)
        t_pattern = pystitch.read_dst(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("xxx->dst: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_xxx_to_gcode(self):
        file1 = "convert_gcode.xxx"
        file2 = "converted_xxx.gcode"
        pystitch.write_xxx(get_big_pattern(), file1)
        f_pattern = pystitch.read_xxx(file1)
        pystitch.write_gcode(f_pattern, file2)
        t_pattern = pystitch.read_gcode(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("xxx->gcode: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_xxx_to_pes(self):
        file1 = "convert_pes.xxx"
        file2 = "converted_xxx.pes"
        pystitch.write_xxx(get_big_pattern(), file1)
        f_pattern = pystitch.read_xxx(file1)
        pystitch.write_pes(f_pattern, file2)
        t_pattern = pystitch.read_pes(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("xxx->pes: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_xxx_to_tbf(self):
        file1 = "convert_tbf.xxx"
        file2 = "converted_xxx.tbf"
        pystitch.write_xxx(get_big_pattern(), file1)
        f_pattern = pystitch.read_xxx(file1)
        pystitch.write_tbf(f_pattern, file2)
        t_pattern = pystitch.read_tbf(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(NEEDLE_SET), 16)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("xxx->tbf: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)
