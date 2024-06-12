# Dictionary to store robots and their positions
robots = {}
next_robot_id = 1

def create_robot():
    global next_robot_id
    robot_id = next_robot_id
    robots[robot_id] = (0, 0)  # Initialize robot at position (0, 0)
    next_robot_id += 1
    return robot_id

def get_robot_position(robot_id):
    return robots.get(robot_id)

def move_robot(robot_id, command):
    if robot_id not in robots:
        return "id not in the list"
    x, y = robots[robot_id]
    direction = command[0]
    steps = int(command[1])
    
    if direction == 'N':
        new_x, new_y = x, y + steps
    elif direction == 'S':
        new_x, new_y = x, y - steps
    elif direction == 'E':
        new_x, new_y = x + steps, y
    elif direction == 'W':
        new_x, new_y = x - steps, y
    else:
        return  "Invalid direction"

    # Check for id with other robots
    for other_robot_id, position in robots.items():
        if other_robot_id != robot_id and position == (new_x, new_y):
            # Stop at the previous cell
            robots[robot_id] = (x, y)
            return robots[robot_id]
    
    # Move to the new position 
    robots[robot_id] = (new_x, new_y)
    return  robots[robot_id]

