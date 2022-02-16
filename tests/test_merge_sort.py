import unittest
from Classic_Algorithms.Sorting import merge_sort, bubble_sort


class MyTestCase(unittest.TestCase):
    def test_merge_sort(self):
        self.assertEqual(merge_sort([8, 2, 4, 6, 1, 7, 3, 5]), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(bubble_sort([8, 2, 4, 6, 1, 7, 3, 5]), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(merge_sort([1, 9, 11, 3, 5, 13, 15, 7]), [1, 3, 5, 7, 9, 11, 13, 15])
        self.assertEqual(bubble_sort([21, 19, 11, 63, 85, 13, 105, 377]), [11, 13, 19, 21, 63, 85, 105, 377])
        self.assertEqual(merge_sort([61, 19, 121, 93, 35, 153, 135, 71]), [19, 35, 61, 71, 93, 121, 135, 153])
        self.assertEqual(bubble_sort([114, 489, 4111, 633, 455, 813, 215, 27]), [27, 114, 215, 455, 489, 633, 813, 4111])

