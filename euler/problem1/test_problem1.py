import problem1
import unittest

class Problem1Test(unittest.TestCase):

    def test_sum_of_multiples_of_3_and_5(self):
        problem = problem1()
        problem.limit = 10
        problem.solve_problem()
        self.assertEqual(problem.solution, 23)
