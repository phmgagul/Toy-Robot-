import unittest
import robot
from test_base import captured_io
from io import StringIO
from world import obstacles
from world.text import world

class MyTests(unittest.TestCase):

    def test_forward_command(self):
        self.assertEqual(world.do_forward("Bmax", 10),(True, " > Bmax moved forward by 10 steps."))
        
    def test_backward_command(self):
        self.assertEqual(world.do_back("Bmax", 10),(True, " > Bmax moved back by 10 steps."))

    def test_is_position_allowed_false(self):
        self.assertEqual(world.is_position_allowed(150, 150), False)

    def test_is_position_allowed_true(self):
        self.assertEqual(world.is_position_allowed(100, 150), True)

    def test_turn_left(self):    
        self.assertEqual(world.do_left_turn("Bmax"),(True, " > Bmax turned left."))

    def test_turn_right(self):
        self.assertEqual(world.do_right_turn("Bmax"),(True, " > Bmax turned right."))

if __name__ == "__main__":
    unittest.main()