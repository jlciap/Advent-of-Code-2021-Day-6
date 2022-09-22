import unittest
from Solution import Solution


# These unit tests come straight from the Advent of Code Website and are used both the help and verify
# the solving of the problem

class TestSolution(unittest.TestCase):

    def test_80_days_test_data(self):
        sol = Solution('test.txt')
        self.assertEqual(sol.give_number_of_fish(80), 5934)

    def test_256_days_test_data(self):
        sol = Solution('test.txt')
        self.assertEqual(sol.give_number_of_fish(256), 26984457539)

    def test_80_days_real_data(self):
        sol = Solution('data.txt')
        self.assertEqual(sol.give_number_of_fish(80), 362639)

    def test_strings_a(self):
        sol = Solution('data.txt')
        self.assertEqual(sol.give_number_of_fish(256), 1639854996917)



if __name__ == '__main__':
    unittest.main()