import os
import unittest

import pystitch
from pystitch.EmbConstant import *
from test.pattern_for_tests import (
    get_big_pattern,
    get_shift_stop_pattern,
    get_simple_stop,
)


class TestConverts(unittest.TestCase):

    def position_equals(self, stitches, j, k):
        self.assertEqual(stitches[j][:1], stitches[k][:1])

    def test_convert_jef_to_u01(self):
        file1 = "convert_u01.jef"
        file2 = "converted_jef.u01"
        pystitch.write_jef(get_big_pattern(), file1)
        f_pattern = pystitch.read_jef(file1)
        pystitch.write_u01(f_pattern, file2)
        t_pattern = pystitch.read_u01(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(NEEDLE_SET), 16)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("jef->u01: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_jef_to_csv(self):
        file1 = "convert_csv.jef"
        file2 = "converted_jef.csv"
        pystitch.write_jef(get_big_pattern(), file1)
        f_pattern = pystitch.read_jef(file1)
        pystitch.write_csv(f_pattern, file2)
        t_pattern = pystitch.read_csv(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("jef->csv: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_jef_to_exp(self):
        file1 = "convert_exp.jef"
        file2 = "converted_jef.exp"
        pystitch.write_jef(get_big_pattern(), file1)
        f_pattern = pystitch.read_jef(file1)
        pystitch.write_exp(f_pattern, file2)
        t_pattern = pystitch.read_exp(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("jef->exp: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_jef_to_pes(self):
        file1 = "convert_pes.jef"
        file2 = "converted_jef.pes"
        pystitch.write_jef(get_big_pattern(), file1)
        f_pattern = pystitch.read_jef(file1)
        pystitch.write_pes(f_pattern, file2)
        t_pattern = pystitch.read_pes(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("jef->pes: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_jef_to_jef(self):
        file1 = "convert_jef.jef"
        file2 = "converted_jef.jef"
        pystitch.write_jef(get_big_pattern(), file1)
        f_pattern = pystitch.read_jef(file1)
        pystitch.write_jef(f_pattern, file2)
        t_pattern = pystitch.read_jef(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("jef->jef: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_jef_to_pec(self):
        file1 = "convert_pec.jef"
        file2 = "converted_jef.pec"
        pystitch.write_jef(get_big_pattern(), file1)
        f_pattern = pystitch.read_jef(file1)
        pystitch.write_pec(f_pattern, file2)
        t_pattern = pystitch.read_pec(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("jef->pec: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_jef_to_vp3(self):
        file1 = "convert_vp3.jef"
        file2 = "converted_jef.vp3"
        pystitch.write_jef(get_big_pattern(), file1)
        f_pattern = pystitch.read_jef(file1)
        pystitch.write_vp3(f_pattern, file2)
        t_pattern = pystitch.read_vp3(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("jef->vp3: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_jef_to_dst(self):
        file1 = "convert_dst.jef"
        file2 = "converted_jef.dst"
        pystitch.write_jef(get_big_pattern(), file1)
        f_pattern = pystitch.read_jef(file1)
        pystitch.write_dst(f_pattern, file2)
        t_pattern = pystitch.read_dst(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("jef->dst: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_jef_to_gcode(self):
        file1 = "convert_gcode.jef"
        file2 = "converted_jef.gcode"
        pystitch.write_jef(get_big_pattern(), file1)
        f_pattern = pystitch.read_jef(file1)
        pystitch.write_gcode(f_pattern, file2)
        t_pattern = pystitch.read_gcode(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("jef->gcode: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_jef_to_xxx(self):
        file1 = "convert_xxx.jef"
        file2 = "converted_jef.xxx"
        pystitch.write_jef(get_big_pattern(), file1)
        f_pattern = pystitch.read_jef(file1)
        pystitch.write_xxx(f_pattern, file2)
        t_pattern = pystitch.read_xxx(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("jef->xxx: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_jef_to_tbf(self):
        file1 = "convert_tbf.jef"
        file2 = "converted_jef.tbf"
        pystitch.write_jef(get_big_pattern(), file1)
        f_pattern = pystitch.read_jef(file1)
        pystitch.write_tbf(f_pattern, file2)
        t_pattern = pystitch.read_tbf(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(NEEDLE_SET), 16)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("jef->tbf: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_jef_stop_write_simple(self):
        file = "stop.jef"
        pystitch.write_jef(get_simple_stop(), file)
        s_pattern = pystitch.read_jef(file)
        self.assertEqual(s_pattern.count_stitch_commands(STOP), 1)
        self.assertEqual(s_pattern.count_color_changes(), 0)
        self.addCleanup(os.remove, file)

    def test_jef_stop_write_large(self):
        file = "stop2.jef"
        pattern = get_shift_stop_pattern()
        n_pattern = pattern.get_normalized_pattern()
        self.assertEqual(n_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(n_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.assertEqual(n_pattern.count_stitch_commands(STOP), 5)

        pystitch.write_jef(pattern, file)
        f_pattern = pystitch.read_jef(file)
        self.assertIsNotNone(f_pattern)

        with open(file, "rb") as f:
            f.seek(0x18)
            colors = f.read(1)
            self.assertEqual(ord(colors), f_pattern.count_color_changes() + f_pattern.count_stitch_commands(STOP) + 1)

        self.assertEqual(f_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(f_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.assertEqual(f_pattern.count_stitch_commands(STOP), 5)
        self.addCleanup(os.remove, file)
