import unittest
import unittest_configuration
from p_00001_two_sum import Solution


class Test_NormalCases(unittest.TestCase):

    examples = [
        {"nums": [2, 7, 11, 15], "target": 9, "ans": [0, 1]},
        {"nums": [3, 2, 4], "target": 6, "ans": [1, 2]},
        {"nums": [3, 3], "target": 6, "ans": [0, 1]}
    ]

    def setUp(self):
        self.obj = Solution()

    def tearDown(self) -> None:
        super().tearDown()

    def test_solutions(self):
        for case in self.examples:
            for solve in [self.obj.solve_001, self.obj.solve_002, self.obj.solve_003]:
                ret = solve(case["nums"], case["target"])
                self.assertEqual(case["ans"], sorted(ret))


class Test_ExceptionCases(unittest.TestCase):

    examples = [
        {"nums": ["2", "7", "11", "15"], "target": "9"},
        {"nums": [2, 7, 11, 15], "target": "9"},
        {"nums": [2], "target": 9},
        {"nums": [-1-10**9, 7, 11, 15], "target": 9},
        {"nums": [1+10**9, 7, 11, 15], "target": 9},
        {"nums": [2, 7, 11, 15], "target": -1-10**9},
        {"nums": [2, 7, 11, 15], "target": 1+10**9}
    ]

    def setUp(self):
        self.obj = Solution()

    def tearDown(self) -> None:
        super().tearDown()

    def test_solutions(self):
        for case in self.examples:
            for solve in [self.obj.solve_001, self.obj.solve_002, self.obj.solve_003]:
                self.assertRaises(TypeError, solve, case["nums"], case["target"])


if __name__ == "__main__":

    normal_suite = unittest.TestLoader().loadTestsFromTestCase(Test_NormalCases)
    exception_suite = unittest.TestLoader().loadTestsFromTestCase(Test_ExceptionCases)

    all_tests = unittest.TestSuite([normal_suite, exception_suite])
    unittest.TextTestRunner().run(all_tests)
