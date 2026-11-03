"""Regressions for reading times with seconds in Chinese text normalization, without loading any model."""

import sys
import unittest
from pathlib import Path

sys.path[:0] = [str(Path(__file__).resolve().parent / "GPT_SoVITS")]
from text.zh_normalization.text_normlization import TextNormalizer  # noqa: E402


class TimeWithSecondsTests(unittest.TestCase):
    def setUp(self):
        self.normalizer = TextNormalizer()

    def test_half_hour_with_seconds(self):
        self.assertEqual(self.normalizer.normalize_sentence("12:30:45"), "十二点三十分四十五秒")
        self.assertEqual(self.normalizer.normalize_sentence("现在是8:30:05"), "现在是八点三十分零五秒")

    def test_half_hour_with_seconds_in_range(self):
        self.assertEqual(self.normalizer.normalize_sentence("8:30:15-9:00"), "八点三十分十五秒至九点")
        self.assertEqual(self.normalizer.normalize_sentence("9:00-9:30:15"), "九点至九点三十分十五秒")

    def test_half_hour_without_seconds(self):
        self.assertEqual(self.normalizer.normalize_sentence("12:30"), "十二点半")
        self.assertEqual(self.normalizer.normalize_sentence("12:30:00"), "十二点半")
        self.assertEqual(self.normalizer.normalize_sentence("12:15:45"), "十二点十五分四十五秒")


if __name__ == "__main__":
    unittest.main()
