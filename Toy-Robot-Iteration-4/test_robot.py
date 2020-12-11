import unittest
import robot
from test_base import captured_io
from io import StringIO
from world import obstacles

class TestRobot(unittest.TestCase):
    robot.history.clear()
    maxDiff = None

    def test_history_list_empty(self):
        self.assertEqual(len(robot.history), 0)
            
    def test_do_replay_normal(self):
        with captured_io(StringIO('Bmax\nforward 3\nforward 2\nforward 1\nreplay\noff\n')) as (out, err):
            robot.history.clear()
            obstacles.random.randint = lambda a, b : 0
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? Bmax: Hello kiddo!
Bmax: What must I do next?  > Bmax moved forward by 3 steps.
 > Bmax now at position (0,3).
Bmax: What must I do next?  > Bmax moved forward by 2 steps.
 > Bmax now at position (0,5).
Bmax: What must I do next?  > Bmax moved forward by 1 steps.
 > Bmax now at position (0,6).
Bmax: What must I do next?  > Bmax moved forward by 3 steps.
 > Bmax now at position (0,9).
 > Bmax moved forward by 2 steps.
 > Bmax now at position (0,11).
 > Bmax moved forward by 1 steps.
 > Bmax now at position (0,12).
 > Bmax replayed 3 commands.
 > Bmax now at position (0,12).
Bmax: What must I do next? Bmax: Shutting down..""", out.getvalue().strip())

    def test_do_replay_normal_upper_case(self):
        with captured_io(StringIO('Bmax\nforward 3\nforward 2\nforward 1\nREPLAY\noff\n')) as (out, err):
            robot.history.clear()
            obstacles.random.randint = lambda a, b : 0
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? Bmax: Hello kiddo!
Bmax: What must I do next?  > Bmax moved forward by 3 steps.
 > Bmax now at position (0,3).
Bmax: What must I do next?  > Bmax moved forward by 2 steps.
 > Bmax now at position (0,5).
Bmax: What must I do next?  > Bmax moved forward by 1 steps.
 > Bmax now at position (0,6).
Bmax: What must I do next?  > Bmax moved forward by 3 steps.
 > Bmax now at position (0,9).
 > Bmax moved forward by 2 steps.
 > Bmax now at position (0,11).
 > Bmax moved forward by 1 steps.
 > Bmax now at position (0,12).
 > Bmax replayed 3 commands.
 > Bmax now at position (0,12).
Bmax: What must I do next? Bmax: Shutting down..""", out.getvalue().strip())

    def test_do_replay_silent_okay(self):
        with captured_io(StringIO('Bmax\nforward 3\nforward 2\nforward 1\nreplay silent\noff\n')) as (out, err):
            robot.history.clear()
            obstacles.random.randint = lambda a, b : 0
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? Bmax: Hello kiddo!
Bmax: What must I do next?  > Bmax moved forward by 3 steps.
 > Bmax now at position (0,3).
Bmax: What must I do next?  > Bmax moved forward by 2 steps.
 > Bmax now at position (0,5).
Bmax: What must I do next?  > Bmax moved forward by 1 steps.
 > Bmax now at position (0,6).
Bmax: What must I do next?  > Bmax replayed 3 commands silently.
 > Bmax now at position (0,12).
Bmax: What must I do next? Bmax: Shutting down..""", out.getvalue().strip())

    def test_do_replay_reversed(self):
        with captured_io(StringIO('Bmax\nforward 3\nforward 2\nforward 1\nreplay reversed\noff\n')) as (out, err):
            robot.history.clear()
            obstacles.random.randint = lambda a, b : 0
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? Bmax: Hello kiddo!
Bmax: What must I do next?  > Bmax moved forward by 3 steps.
 > Bmax now at position (0,3).
Bmax: What must I do next?  > Bmax moved forward by 2 steps.
 > Bmax now at position (0,5).
Bmax: What must I do next?  > Bmax moved forward by 1 steps.
 > Bmax now at position (0,6).
Bmax: What must I do next?  > Bmax moved forward by 1 steps.
 > Bmax now at position (0,7).
 > Bmax moved forward by 2 steps.
 > Bmax now at position (0,9).
 > Bmax moved forward by 3 steps.
 > Bmax now at position (0,12).
 > Bmax replayed 3 commands in reverse.
 > Bmax now at position (0,12).
Bmax: What must I do next? Bmax: Shutting down..""", out.getvalue().strip())


    def test_do_replay_reversed_silent(self):
        with captured_io(StringIO('Bmax\nforward 3\nforward 2\nforward 1\nreplay reversed silent\noff\n')) as (out, err):
            robot.history.clear()
            obstacles.random.randint = lambda a, b : 0
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? Bmax: Hello kiddo!
Bmax: What must I do next?  > Bmax moved forward by 3 steps.
 > Bmax now at position (0,3).
Bmax: What must I do next?  > Bmax moved forward by 2 steps.
 > Bmax now at position (0,5).
Bmax: What must I do next?  > Bmax moved forward by 1 steps.
 > Bmax now at position (0,6).
Bmax: What must I do next?  > Bmax replayed 3 commands in reverse silently.
 > Bmax now at position (0,12).
Bmax: What must I do next? Bmax: Shutting down..""", out.getvalue().strip())

    def test_do_replay_range_ERROR(self):
        with captured_io(StringIO('Bmax\nforward 3\nforward 2\nforward 1\nreplay ---\noff\n')) as (out, err):
            robot.history.clear()
            obstacles.random.randint = lambda a, b : 0
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? Bmax: Hello kiddo!
Bmax: What must I do next?  > Bmax moved forward by 3 steps.
 > Bmax now at position (0,3).
Bmax: What must I do next?  > Bmax moved forward by 2 steps.
 > Bmax now at position (0,5).
Bmax: What must I do next?  > Bmax moved forward by 1 steps.
 > Bmax now at position (0,6).
Bmax: What must I do next? Bmax: Sorry, I did not understand 'replay ---'.
Bmax: What must I do next? Bmax: Shutting down..""", out.getvalue().strip())

    def test_do_replay_2(self):
        with captured_io(StringIO('Bmax\nforward 3\nforward 2\nforward 1\nreplay 2\noff\n')) as (out, err):
            robot.history.clear()
            obstacles.random.randint = lambda a, b : 0
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? Bmax: Hello kiddo!
Bmax: What must I do next?  > Bmax moved forward by 3 steps.
 > Bmax now at position (0,3).
Bmax: What must I do next?  > Bmax moved forward by 2 steps.
 > Bmax now at position (0,5).
Bmax: What must I do next?  > Bmax moved forward by 1 steps.
 > Bmax now at position (0,6).
Bmax: What must I do next?  > Bmax moved forward by 2 steps.
 > Bmax now at position (0,8).
 > Bmax moved forward by 1 steps.
 > Bmax now at position (0,9).
 > Bmax replayed 2 commands.
 > Bmax now at position (0,9).
Bmax: What must I do next? Bmax: Shutting down..""", out.getvalue().strip())

    def test_do_replay_range_negative(self):
        with captured_io(StringIO('Bmax\nforward 3\nforward 2\nforward 1\nreplay 1-2\noff\n')) as (out, err):
            robot.history.clear()
            obstacles.random.randint = lambda a, b : 0
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? Bmax: Hello kiddo!
Bmax: What must I do next?  > Bmax moved forward by 3 steps.
 > Bmax now at position (0,3).
Bmax: What must I do next?  > Bmax moved forward by 2 steps.
 > Bmax now at position (0,5).
Bmax: What must I do next?  > Bmax moved forward by 1 steps.
 > Bmax now at position (0,6).
Bmax: What must I do next?  > Bmax moved forward by 1 steps.
 > Bmax now at position (0,7).
 > Bmax replayed 1 commands.
 > Bmax now at position (0,7).
Bmax: What must I do next? Bmax: Shutting down..""", out.getvalue().strip())

    def test_do_replay_range_positive(self):
        with captured_io(StringIO('Bmax\nforward 3\nforward 2\nforward 1\nforward 0\nreplay 4-2\noff\n')) as (out, err):
            robot.history.clear()
            obstacles.random.randint = lambda a, b : 0
            robot.robot_start()
        self.assertEqual("""What do you want to name your robot? Bmax: Hello kiddo!
Bmax: What must I do next?  > Bmax moved forward by 3 steps.
 > Bmax now at position (0,3).
Bmax: What must I do next?  > Bmax moved forward by 2 steps.
 > Bmax now at position (0,5).
Bmax: What must I do next?  > Bmax moved forward by 1 steps.
 > Bmax now at position (0,6).
Bmax: What must I do next?  > Bmax moved forward by 0 steps.
 > Bmax now at position (0,6).
Bmax: What must I do next?  > Bmax moved forward by 3 steps.
 > Bmax now at position (0,9).
 > Bmax moved forward by 2 steps.
 > Bmax now at position (0,11).
 > Bmax replayed 2 commands.
 > Bmax now at position (0,11).
Bmax: What must I do next? Bmax: Shutting down..""", out.getvalue().strip())
 
 
if __name__ == "__main__":
    unittest.main()
