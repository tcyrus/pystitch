import tempfile
import unittest

import pystitch
from pystitch import decode_embroidery_command, encode_thread_change
from pystitch.EmbConstant import *
from test.pattern_for_tests import get_big_pattern


class TestDataPreservation(unittest.TestCase):

    def test_preserve_u01_needles(self):
        pattern = get_big_pattern()
        pattern.add_command(encode_thread_change(SET_CHANGE_SEQUENCE, None, 6, 0))

        with tempfile.NamedTemporaryFile(suffix=".u01") as fp:
            pystitch.write_u01(pattern, fp)
            fp.seek(0)
            read_pattern = pystitch.read_u01(fp)

        for cmd in read_pattern.get_match_commands(NEEDLE_SET):
            print(decode_embroidery_command(cmd[2]))
