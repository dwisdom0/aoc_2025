from unittest import TestCase

from solution2 import is_repeat



class Test2(TestCase):

    def test_example_repeats(self):
        for n in [11, 22, 99, 111, 999, 1010, 1188511885, 222222, 446446, 38593859, 565656, 824824824, 2121212121]:
            with self.subTest(n):
                self.assertTrue(is_repeat(n))
    
    def test_non_repeats(self):
        for n in [5, 12, 1001, 121, 990, 10100, 11885111885, 232222, 644446]:
            with self.subTest(n):
                self.assertFalse(is_repeat(n))

