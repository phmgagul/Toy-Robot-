import unittest
import robot
from test_base import captured_io
from io import StringIO

class TestRobot(unittest.TestCase):

    

    def test_valid_commands(self):
        self.assertEqual(robot.information_command("off"),"Shut down robot")
        self.assertEqual(robot.information_command("help"),"provide information about commands")
        self.assertEqual(robot.information_command("HELP"),"provide information about commands")
        self.assertEqual(robot.information_command("OFF"),"Shut down robot")

    def test_correctness(self):
        self.assertEqual(robot.information_command("help"), "provide information about commands")

    def test_forward_command(self):
        with captured_io(StringIO("")) as (out, err):
            robot.move_forward("Bmax", "10",{"X":0, "Y":10})
            output = out.getvalue().strip()
        self.assertEqual("""> Bmax moved forward by 10 steps.""", output) 
        
    def test_move_backward_command(self):
        with captured_io(StringIO("")) as (out, err):
            robot.move_backward("Bmax", "10", {"X":0, "Y":10})
            output = out.getvalue().strip()
        self.assertEqual("""> Bmax moved back by 10 steps.""", output)

    def test_limit_area(self):
        self.assertEqual(robot.check_limits)
