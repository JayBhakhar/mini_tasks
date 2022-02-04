import unittest

from Classic_Algorithms.Sorting import merge_sort, bubble_sort


class MyTestCase(unittest.TestCase):
    def test_merge_sort(self):
        self.assertEqual(merge_sort([8, 2, 4, 6, 1, 7, 3, 5]), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(bubble_sort([8, 2, 4, 6, 1, 7, 3, 5]), [1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == '__main__':
    unittest.main()
