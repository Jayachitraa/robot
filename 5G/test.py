import unittest
from robot import create_robot, get_robot_position, move_robot

class TestRobotFunctions(unittest.TestCase):

    def test_create_robot(self):
        robot_id = create_robot()
        self.assertIsInstance(robot_id, int, "create_robot should return an integer robot ID")
        print("Test create_robot passed.")

    def test_get_robot_position(self):
        robot_id = create_robot()
        position = get_robot_position(robot_id)
        self.assertEqual(position, (0, 0), f"Expected initial position (0, 0), got {position}")
        print("Test get_robot_position passed.")

    def test_move_robot(self):
        robot_id = create_robot()
        move_robot(robot_id, 'N4')
        position = get_robot_position(robot_id)
        self.assertEqual(position, (0, 4), f"Expected position after moving N4: (0, 4), got {position}")
        print("Test move_robot passed.")

        move_robot(robot_id, 'E3')
        position = get_robot_position(robot_id)
        self.assertEqual(position, (3, 4), f"Expected position after moving E3: (3, 4), got {position}")
        print("Test move_robot passed.")

        move_robot(robot_id, 'S1')
        position = get_robot_position(robot_id)
        self.assertEqual(position, (3, 3), f"Expected position after moving S1: (3, 3), got {position}")
        print("Test move_robot passed.")

        move_robot(robot_id, 'W2')
        position = get_robot_position(robot_id)
        self.assertEqual(position, (1, 3), f"Expected position after moving W2: (1, 3), got {position}")
        print("Test move_robot passed.")

        # Test moving with invalid direction
        result = move_robot(robot_id, 'X2')
        self.assertEqual(result, "Invalid direction", f"Expected 'Invalid direction', got {result}")
        print("Test move_robot with invalid direction passed.")

        # Test moving with non-existent robot ID
        result = move_robot(999, 'N1')
        self.assertEqual(result, "id not in the list", f"Expected 'id not in the list', got {result}")
        print("Test move_robot with non-existent robot ID passed.")

if __name__ == '__main__':
    unittest.main()
