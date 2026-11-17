import tempfile
import unittest

import pystitch
from pystitch import EmbPattern, EmbThread
from test.pattern_for_tests import get_shift_pattern


class TestJson(unittest.TestCase):

    def test_metadata_write_read_json(self):
        pattern = EmbPattern()
        for _ in range(4, 20):
            pattern.add_thread(EmbThread("random"))

        pattern.extras['name'] = "My Embroidery."
        pattern.extras['bytes'] = b'\00these are bytes'
        pattern.extras['bytes2'] = bytearray(b'this is bytearray')
        pattern.extras['value'] = 208

        with tempfile.NamedTemporaryFile(
            prefix="metadata",
            suffix=".json"
        ) as fp:
            pystitch.write(pattern, fp)
            fp.seek(0)
            w_pattern = pystitch.read(fp)

        self.assertEqual(w_pattern.extras['name'], "My Embroidery.")
        self.assertEqual(w_pattern.extras['value'], 208)
        self.assertEqual(len(pattern.threadlist), len(w_pattern.threadlist))
        for q in range(len(pattern.threadlist)):
            self.assertEqual(pattern.threadlist[q], w_pattern.threadlist[q])

    def test_colors_write_read_json(self):
        for _ in range(50):
            pattern = EmbPattern()
            for _ in range(4, 20):
                pattern.add_thread(EmbThread("random"))
            with tempfile.NamedTemporaryFile(
                prefix="color",
                suffix=".json"
            ) as fp:
                pystitch.write(pattern, fp)
                fp.seek(0)
                w_pattern = pystitch.read(fp)
            self.assertEqual(len(pattern.threadlist), len(w_pattern.threadlist))
            for q in range(len(pattern.threadlist)):
                self.assertEqual(pattern.threadlist[q], w_pattern.threadlist[q])

    def test_write_read_json(self):
        pattern = get_shift_pattern()

        with tempfile.NamedTemporaryFile(suffix=".json") as fp:
            pystitch.write(pattern, fp)
            fp.seek(0)
            w_pattern = pystitch.read(fp)

        self.assertEqual(len(pattern.threadlist), len(w_pattern.threadlist))
        for q in range(len(pattern.threadlist)):
            self.assertEqual(pattern.threadlist[q], w_pattern.threadlist[q])
        for q in range(len(pattern.stitches)):
            self.assertEqual(pattern.stitches[q], w_pattern.stitches[q])
