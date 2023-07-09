import settings
import unittest
from src.two_sum import TwoSum


class Test_two_sum(unittest.TestCase):

    def setUp(self):
        self.obj = TwoSum()

    def test_001(self):
        nums = [2, 7, 11, 15]
        target = 9
        ans = [0, 1]
        result = self.obj.solve_001(nums, target)
        self.assertEqual(sorted(ans), sorted(result))
    
    def test_002(self):
        nums = [3, 2, 4]
        target = 6
        ans = [1, 2]
        result = self.obj.solve_001(nums, target)
        self.assertEqual(sorted(ans), sorted(result))

    def test_003(self):
        nums = [2, 7, 11, 15]
        target = 9
        ans = [0, 1]
        result = self.obj.solve_002(nums, target)
        self.assertEqual(sorted(ans), sorted(result))
    
    def test_004(self):
        nums = [3, 2, 4]
        target = 6
        ans = [1, 2]
        result = self.obj.solve_002(nums, target)
        self.assertEqual(sorted(ans), sorted(result))



if __name__ == "__main__":
    unittest.main()

