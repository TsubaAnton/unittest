import unittest
from unittest_proj.utils import arrs


class TestArrs(unittest.TestCase):

    def test_get_existing_index(self):
        result = arrs.get([1, 2, 3], 1, "default")
        self.assertEqual(result, 2)

    def test_get_non_existing_index(self):
        result = arrs.get([1, 2, 3], 10, "default")
        self.assertEqual(result, "default")

    def test_get_empty_list(self):
        result = arrs.get([], 0, "default")
        self.assertEqual(result, "default")

    def test_my_slice_with_positive_indices(self):
        result = arrs.my_slice([1, 2, 3, 4, 5], 1, 4)
        self.assertEqual(result, [2, 3, 4])

    def test_my_slice_with_negative_indices(self):
        result = arrs.my_slice([1, 2, 3, 4, 5], -3, -1)
        self.assertEqual(result, [3, 4])

    def test_my_slice_with_start_and_end_None(self):
        result = arrs.my_slice([1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_my_slice_with_end_None(self):
        result = arrs.my_slice([1, 2, 3, 4, 5], start=2)
        self.assertEqual(result, [3, 4, 5])

    def test_my_slice_with_end_greater_than_length(self):
        result = arrs.my_slice([1, 2, 3, 4, 5], end=10)
        self.assertEqual(result, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()