import unittest
from io import StringIO
import sys
from test_base import run_unittests
from test_base import captured_io
import world.obstacles as obstacles
import robot


class MyTest(unittest.TestCase):

    def test_is_position_blocked(self):
        obstacles.obstacle_list = [(1,1), (2,2), (3,3), (4,4)]
        self.assertEqual(obstacles.is_position_blocked(3,3), True)

    def test_is_position_blocked_false(self):
        obstacles.obstacle_list = [(1,2),(2,1),(2,3),(2,4)]
        self.assertEqual(obstacles.is_position_blocked(2,2), False)
        self.assertEqual(obstacles.is_position_blocked(4,4), False)
    
    def test_is_path_blocked(self):
        # obstacles.obstacle_list = [(1,2),(1,4),(1, 3),(2,4)]
        obstacles.random.randint = lambda a, b : 1
        #print(obstacles.get_obstacles())
        self.assertEqual(obstacles.is_path_blocked(1, 0 ,1,  1 + 4), True)

    def test_get_obstacles_is_empty(self):
        obstacles.random.randint = lambda a, b : 0
        self.assertEqual(obstacles.get_obstacles() == [], True)

    def test_get_obstacles_is_not_empty(self):
        obstacles.random.randint = lambda a, b : 1
        self.assertEqual(obstacles.get_obstacles() == [], False)




if __name__ == "__main__":
    unittest.main()