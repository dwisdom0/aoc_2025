from unittest import TestCase

from solution2 import rotate


class TestPart2(TestCase):

    def test_100(self):
        dial = 30
        direction = 'R'
        amount = 70
        new_dial, zeros = rotate(dial, direction, amount)
        self.assertEqual(new_dial, 0)
        self.assertEqual(zeros, 1)

    def test_200(self):
        dial = 30
        direction = 'R'
        amount = 170
        new_dial, zeros = rotate(dial, direction, amount)
        self.assertEqual(new_dial, 0)
        self.assertEqual(zeros, 2)

    def test_negative_100(self):
        dial = 30
        direction = 'L'
        amount = 130
        new_dial, zeros = rotate(dial, direction, amount)
        self.assertEqual(new_dial, 0)
        self.assertEqual(zeros, 2)

    def test_negative_200(self):
        dial = 30
        direction = 'L'
        amount = 230
        new_dial, zeros = rotate(dial, direction, amount)
        self.assertEqual(new_dial, 0)
        self.assertEqual(zeros, 3)
    
    def test_start_at_0_go_right(self):
        dial = 0 
        direction = 'R'
        amount = 5
        new_dial, zeros = rotate(dial, direction, amount)
        self.assertEqual(new_dial, 5)
        self.assertEqual(zeros, 0)

    def test_start_at_0_go_left(self):
        dial = 0 
        direction = 'L'
        amount = 5
        new_dial, zeros = rotate(dial, direction, amount)
        self.assertEqual(new_dial, 95)
        self.assertEqual(zeros, 0)
