import random
# from turtle import position

#random.randint = lambda x, y: 1
obstacle_list = []
cubes = []

min_y, max_y = -200, 200
min_x, max_x = -100, 100
#random.randint = lambda a, b: 1
def is_position_blocked(x, y):
    if (x, y) in obstacle_list:
        return True
    else:
        return False


def is_path_blocked(x1, y1, x2, y2):
    """this function checks the path between the current position and the position the robot must go to."""
    step = 1
    if y2 > y1 or x2 > x1:
        step = 1
    elif y2 < y1 or x2 < x1:
        step = -1

    path = []
    
    if x1 == x2:
        path = [(x2, y) for y in range(y1, y2 + step, step)]
    elif y1 == y2:
        path = [(x, y1) for x in range (x1, x2 + step, step)]
    #print(path)
    for item in path:
        if item in cubes:
            return True
    return False


def get_obstacles():
    """this function returns a list of obstacles."""
    global obstacle_list
    global cubes

    num_obstacles = random.randint(0, 10)
    for i in range(num_obstacles):
        x_cord = random.randint(min_x, max_x - 4)
        y_cord = random.randint(min_y, max_y - 4)
        obstacle_list.append((x_cord, y_cord))

    for (x, y) in obstacle_list:
        for x_cord in range(x, x + 5):
            for y_cord in range(y, y + 5):
                cubes.append((x_cord, y_cord))

    return obstacle_list

# if __name__== "__main__":
#     print(get_obstacles())
