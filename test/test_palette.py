import unittest

from pystitch import EmbPattern, EmbThread
from pystitch.EmbThread import (
    build_nonrepeat_palette,
    build_palette,
    build_unique_palette,
)


class TestPalettes(unittest.TestCase):

    def setUp(self) -> None:
        # Minimal threadset based on EmbThreadPec
        self.threadset = [
            EmbThread(0x0a55a3, "Blue"),
            EmbThread(0xed171f, "Red"),
            EmbThread(0x000000, "Black"),
            EmbThread(0x0B3D91, "Ultramarine"),
            EmbThread(0xE8A900, "Deep Gold"),
            EmbThread(0xFFC864, "Applique Material", reserved=True),
            EmbThread(0xFFC8C8, "Applique Position", reserved=True),
            EmbThread(0xFFC8C8, "Applique", reserved=True),
        ]

    def test_unique_palette(self):
        """Similar elements should not plot to the same palette index"""
        pattern = EmbPattern()
        pattern += "#FF0001"
        pattern += "Blue"
        pattern += "Blue"
        pattern += "Red"

        palette = build_unique_palette(self.threadset, pattern.threadlist)
        self.assertNotEqual(palette[0], palette[3], "Red and altered Red")
        self.assertEqual(palette[1], palette[2], "Blue and Blue")

    def test_unique_palette_large(self):
        """Excessive palette entries that all map, should be mapped"""
        pattern = EmbPattern()
        for _ in range(100):
            pattern += "black"

        palette = build_unique_palette(self.threadset, pattern.threadlist)
        self.assertEqual(palette[0], palette[1])

    def test_unique_palette_unmap(self):
        """Excessive palette entries can't all map, should map what it can and repeat"""
        pattern = EmbPattern()
        for i in range(100):
            thread = EmbThread()
            thread.set_color(i, i, i)
            pattern += thread

        palette = build_unique_palette(self.threadset, pattern.threadlist)
        palette.sort()

    def test_unique_palette_max(self):
        """If the entries equal the list they should all map."""
        matchable_count = sum(
            1 for t in self.threadset if t is not None and not getattr(t, "reserved", False)
        )

        pattern = EmbPattern()
        for i in range(matchable_count):
            thread = EmbThread()
            thread.set_color(i, i, i)
            pattern += thread

        palette = build_unique_palette(self.threadset, pattern.threadlist)
        palette.sort()

        self.assertEqual(len(palette), len(set(palette)))

    def test_nonrepeat_palette_moving(self):
        """The almost same color should not get plotted to the same palette index"""
        pattern = EmbPattern()
        pattern += "Red"
        pattern += "Blue"
        pattern += "#0100FF"
        pattern += "Red"

        palette = build_nonrepeat_palette(self.threadset, pattern.threadlist)
        self.assertEqual(palette[0], palette[3], "Red and Red")
        self.assertNotEqual(palette[1], palette[2], "Blue and altered Blue")

    def test_nonrepeat_palette_stay_moved(self):
        """An almost same moved, only temporary"""
        pattern = EmbPattern()
        pattern += "Red"
        pattern += "Blue"
        pattern += "#0100FF"
        pattern += "Red"
        pattern += "#0100FF"

        palette = build_nonrepeat_palette(self.threadset, pattern.threadlist)
        self.assertEqual(palette[0], palette[3], "Red and Red")
        self.assertNotEqual(palette[1], palette[2], "Blue and altered Blue")
        self.assertNotEqual(palette[2], palette[4], "same color, but color was moved")

    def test_nonrepeat_palette_same(self):
        """The same exact same color if repeated should remain"""
        pattern = EmbPattern()
        pattern += "Red"
        pattern += "Blue"
        pattern += "#0000FF"  # actual blue
        pattern += "Red"

        palette = build_nonrepeat_palette(self.threadset, pattern.threadlist)
        self.assertEqual(palette[0], palette[3], "Red and Red")
        self.assertEqual(palette[1], palette[2], "Blue and Blue")

    def test_reserved_indices_excluded_from_matching(self):
        reservedIdx = [
            i for i, t in enumerate(self.threadset) if t.reserved
        ]

        # Two colliding "Deep Gold" threads used to fall through to the
        # reserved index 62 slot (inkstitch#1105).
        pattern = EmbPattern()
        gold1 = EmbThread()
        gold1.set_color(0xE8, 0xA9, 0x00)
        gold2 = EmbThread()
        gold2.set_color(0xE8, 0xA9, 0x00)
        pattern.threadlist = [gold1, gold2]

        palette = build_unique_palette(self.threadset, pattern.threadlist)
        for i in reservedIdx:
            self.assertNotIn(i, palette)

        # An RGB value that lands on reserved must resolve to a real color
        # instead.
        exact = EmbThread()
        exact.set_color(255, 200, 200)
        index = exact.find_nearest_color_index(self.threadset)
        self.assertNotIn(index, reservedIdx)

    def test_palette(self):
        """Similar colors map to the same index"""
        pattern = EmbPattern()
        pattern += "#FF0001"
        pattern += "Blue"
        pattern += "Blue"
        pattern += "Red"

        palette = build_palette(self.threadset, pattern.threadlist)
        self.assertEqual(palette[0], palette[3], "Red and altered Red")
        self.assertEqual(palette[1], palette[2], "Blue and Blue")
