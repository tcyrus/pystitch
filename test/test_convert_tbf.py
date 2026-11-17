import os
import unittest

import pystitch
from pystitch import EmbPattern
from pystitch.EmbConstant import *
from pystitch.EmbFunctions import decode_embroidery_command
from test.pattern_for_tests import (
    get_big_pattern,
    get_fractal_pattern,
    get_shift_pattern_needles,
)


class TestConverts(unittest.TestCase):
    def position_equals(self, stitches, j, k):
        self.assertEqual(stitches[j][:1], stitches[k][:1])

    def test_convert_tbf_to_u01(self):
        file1 = "convert_u01.tbf"
        file2 = "converted_tbf.u01"
        pystitch.write_tbf(get_big_pattern(), file1)
        f_pattern = pystitch.read_tbf(file1)
        pystitch.write_u01(f_pattern, file2)
        t_pattern = pystitch.read_u01(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(NEEDLE_SET), 16)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("tbf->u01: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_tbf_to_csv(self):
        file1 = "convert_csv.tbf"
        file2 = "converted_tbf.csv"
        pystitch.write_tbf(get_big_pattern(), file1)
        f_pattern = pystitch.read_tbf(file1)
        pystitch.write_csv(f_pattern, file2)
        t_pattern = pystitch.read_csv(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(NEEDLE_SET), 16)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("tbf->csv: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_tbf_to_exp(self):
        file1 = "convert_exp.tbf"
        file2 = "converted_tbf.exp"
        pystitch.write_tbf(get_big_pattern(), file1)
        f_pattern = pystitch.read_tbf(file1)
        pystitch.write_exp(f_pattern, file2)
        t_pattern = pystitch.read_exp(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("tbf->exp: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_tbf_to_vp3(self):
        file1 = "convert_vp3.tbf"
        file2 = "converted_tbf.vp3"
        pystitch.write_tbf(get_big_pattern(), file1)
        f_pattern = pystitch.read_tbf(file1)
        pystitch.write_vp3(f_pattern, file2)
        t_pattern = pystitch.read_vp3(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("tbf->vp3: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_tbf_to_jef(self):
        file1 = "convert_jef.tbf"
        file2 = "converted_tbf.jef"
        pystitch.write_tbf(get_big_pattern(), file1)
        f_pattern = pystitch.read_tbf(file1)
        pystitch.write_jef(f_pattern, file2)
        t_pattern = pystitch.read_jef(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("tbf->jef: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_tbf_to_pec(self):
        file1 = "convert_pec.tbf"
        file2 = "converted_tbf.pec"
        pystitch.write_tbf(get_big_pattern(), file1)
        f_pattern = pystitch.read_tbf(file1)
        pystitch.write_pec(f_pattern, file2)
        t_pattern = pystitch.read_pec(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("tbf->pec: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_tbf_to_tbf(self):
        file1 = "convert_tbf.tbf"
        file2 = "converted_tbf.tbf"
        pystitch.write_tbf(get_big_pattern(), file1)
        f_pattern = pystitch.read_tbf(file1)
        pystitch.write_tbf(f_pattern, file2)
        t_pattern = pystitch.read_tbf(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(NEEDLE_SET), 16)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("tbf->tbf: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_tbf_to_dst(self):
        file1 = "convert_dst.tbf"
        file2 = "converted_tbf.dst"
        pystitch.write_tbf(get_big_pattern(), file1)
        f_pattern = pystitch.read_tbf(file1)
        pystitch.write_dst(f_pattern, file2)
        t_pattern = pystitch.read_dst(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("tbf->dst: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_tbf_to_gcode(self):
        file1 = "convert_gcode.tbf"
        file2 = "converted_tbf.gcode"
        pystitch.write_tbf(get_big_pattern(), file1)
        f_pattern = pystitch.read_tbf(file1)
        pystitch.write_gcode(f_pattern, file2)
        t_pattern = pystitch.read_gcode(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("tbf->gcode: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_tbf_to_pes(self):
        file1 = "convert_pes.tbf"
        file2 = "converted_tbf.pes"
        pystitch.write_tbf(get_big_pattern(), file1)
        f_pattern = pystitch.read_tbf(file1)
        pystitch.write_pes(f_pattern, file2)
        t_pattern = pystitch.read_pes(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("tbf->pes: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_convert_tbf_to_xxx(self):
        file1 = "convert_xxx.tbf"
        file2 = "converted_tbf.xxx"
        pystitch.write_tbf(get_big_pattern(), file1)
        f_pattern = pystitch.read_tbf(file1)
        pystitch.write_xxx(f_pattern, file2)
        t_pattern = pystitch.read_xxx(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(t_pattern.count_stitch_commands(COLOR_CHANGE), 15)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        self.position_equals(t_pattern.stitches, 0, -1)
        print("tbf->xxx: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_needles_convert_tbf_to_u01(self):
        file1 = "convert_u01.tbf"
        file2 = "converted_tbf.u01"
        pystitch.write_tbf(get_shift_pattern_needles(), file1)
        f_pattern = pystitch.read_tbf(file1)

        t = 8
        for x, y, cmd in f_pattern.stitches:
            if cmd & COMMAND_MASK == NEEDLE_SET:
                flag, thread, needle, order = decode_embroidery_command(cmd)
                self.assertEqual(needle, t)
                t -= 1
                if t <= 0:
                    t = 8

        pystitch.write_u01(f_pattern, file2)
        t_pattern = pystitch.read_u01(file2)

        self.assertIsNotNone(t_pattern)
        self.assertEqual(f_pattern.count_stitch_commands(NEEDLE_SET), 16)
        self.assertEqual(t_pattern.count_stitch_commands(NEEDLE_SET), 16)
        self.assertEqual(t_pattern.count_stitch_commands(STITCH), 16 * 5)
        print("tbf->u01: ", t_pattern.stitches)
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_tbf_flipped(self):
        """
        Test whether tbf is flipped on subsequent loads. This creates a pattern. Saves/loads, then save/loads.
        These patterns should be the same but a bug in 1.5.0 was flipping TBF patterns on write.
        """
        pattern = get_fractal_pattern()
        file1 = "fractal1.tbf"
        file2 = "fractal2.tbf"
        pystitch.write(pattern, file1)
        f1 = pystitch.read_tbf(file1)
        pystitch.write(f1, file2)
        f2 = pystitch.read_tbf(file2)
        for i in range(len(f1.stitches)):
            self.assertEqual(f1.stitches[i], f2.stitches[i])
        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)

    def test_needle_tbf_range(self):
        file1 = "test_range8.tbf"
        file2 = "test_range8.ct0"
        pattern = EmbPattern()
        pattern.metadata("name", "colorswitch8")
        pattern += "red"
        pattern += "blue"
        pattern += "green"
        pattern += "grey"
        pattern += "gold"
        pattern += "ivory"
        pattern += "khaki"
        pattern += "oldlace"

        pattern.needle_change(needle=4)
        pattern += (0, 0), (0, 100), (100, 100), (100, 0), (0, 0)
        pattern.add_command(MATRIX_TRANSLATE, 25, 25)
        pattern.add_command(MATRIX_ROTATE, 360.0 / 3)

        pattern.needle_change(needle=5)
        pattern += (0, 0), (0, 100), (100, 100), (100, 0), (0, 0)
        pattern.add_command(MATRIX_TRANSLATE, 25, 25)
        pattern.add_command(MATRIX_ROTATE, 360.0 / 3)

        pattern.needle_change(needle=6)
        pattern += (0, 0), (0, 100), (100, 100), (100, 0), (0, 0)

        pystitch.write_tbf(pattern, file1, settings={"ct0": file2})
        f_pattern = pystitch.read_tbf(file1)

        self.assertNotEqual(len(f_pattern.threadlist), 1)
        self.assertEqual(f_pattern.count_stitch_commands(STITCH), 3 * 5)

        self.addCleanup(os.remove, file1)
        self.addCleanup(os.remove, file2)
