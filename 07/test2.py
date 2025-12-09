from unittest import TestCase
from solution2 import solve


class Test2(TestCase):
    def test_cycle(self):
        manifold = [
            '...S...',
            '.......',
            '...^...',
            '.......',
            '..^.^..',
            '.......',
            '.^.^.^.',
            '.......',
            '..^.^..',
            '.......',
            '.^.....',
            '.......',
            '....^..',
            '.......',
            '...^...',
        ]
        result = solve(manifold)
        self.assertEqual(result,0)
