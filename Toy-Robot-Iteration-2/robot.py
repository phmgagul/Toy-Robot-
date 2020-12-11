
i = 0
#step 1
def get_robot_name():
    """this function is to get the robot name."""
    robot_name = input("What do you want to name your robot? ")

    return robot_name

#step 2
def get_command(robot_name):
    """this is to get the command as input from the user."""
    input_command = input(f"{robot_name}: What must I do next? ")

    return input_command
#step 2
def list_of_commands():
    """this function stores the list of commands."""
    command_list = ["OFF", "HELP", "FORWARD", "BACK", "RIGHT", "LEFT","SPRINT"]

    return command_list

def command_information():
    """this function stores the information about the available commands."""
    valid_commands = ["OFF  - Shut down robot", "HELP - provide information about commands", "FORWARD - moved the robot forward", "BACK - moved the robot back", "RIGHT - turn the robot 90 degrees to the right", "LEFT - turn the robot left", "SPRINT - gives the robot a boost of speed"]
    print("\n".join(valid_commands))
    print()

def information_command(command_information):
    command_map = {"OFF":"Shut down robot", "HELP":"provide information about commands", "FORWARD":"moved the robot forward", "BACK":"moved the robot back", "RIGHT":"turn the robot 90 degrees to the right", "LEFT":"turn the robot left", "SPRINT":"gives robot a boost of speed"} 
    for x,y in command_map.items():
        if command_information.upper() == x:
            return y
    return "command not found" 

#step 6
def robot_position(robot_name,coordinates):
    """this function is to track the robot position."""   
    print(f" > {robot_name} now at position ({coordinates['X']},{coordinates['Y']}).")

#step 5
def move_forward(robot_name,number_of_steps,coordinates):
    """this function moves the robot forward."""
    if check_limits(coordinates,number_of_steps) == True:
        if coordinates["turns"] == 0:#no turn
            coordinates['Y']+= int(number_of_steps)
        elif coordinates['turns'] == 1:#turned once
            coordinates['X']+= int(number_of_steps)
        elif coordinates['turns'] == 2:#turned twice
            coordinates['Y']-= int(number_of_steps)
        elif coordinates['turns'] == 3:#turned thrice
            coordinates['X']-= int(number_of_steps)
        print(f" > {robot_name} moved forward by {number_of_steps} steps.")
    else:
        print(f"{robot_name}: Sorry, I cannot go outside my safe zone.")

                
    
 #step 7
def move_backward(robot_name, number_of_steps, coordinates):
    """this function moves the robot backward."""
    if check_limits(coordinates,number_of_steps) == True:
        if coordinates["turns"] == 0:
            coordinates['Y']-= int(number_of_steps)
        elif coordinates["turns"] == 1:
            coordinates['X']-= int(number_of_steps)
        elif coordinates["turns"] == 2:
            coordinates['Y']+= int(number_of_steps)
        elif coordinates["turns"] == 3:
            coordinates['X']+= int(number_of_steps)     
        print(f" > {robot_name} moved back by {number_of_steps} steps.")    
    else:
        print(f"{robot_name}: Sorry, I cannot go outside my safe zone.")

#step 8
def turn_right(robot_name, coordinates):
    """"this method turns the robot 90 degrees to the right"""
    coordinates["turns"] += 1
    coordinates["direction"] = "right"
    if coordinates["turns"] > 3:
        coordinates["turns"] = 0
    
    print(f" > {robot_name} turned right.")

def turn_left(robot_name, coordinates): 
    """"this method turns the robot 90 degrees to the left"""
    coordinates["turns"] -= 1 
    coordinates["direction"] = "left" 
    if coordinates["turns"] < 0:
        coordinates["turns"] = 3
    
    
    print(f" > {robot_name} turned left.")

def check_limits(coordinates,number_of_steps):
    """this function is to check the limits of the robot."""
    if coordinates["direction"] == "right"  and int(number_of_steps) in range(-100,101):
        return True
    elif coordinates["direction"] == "left"  and int(number_of_steps) in range(-100,101):
        return True
    elif coordinates["direction"] == "up" and int(number_of_steps) in range (-200,200):
        return True
    return False

def sprint_command(robot_name,number_of_steps,coordinates):
    """this function is to give the robot a boost."""
    global i 
    if int(number_of_steps) == 0:
        coordinates["Y"] += i
    else:
        i+= int(number_of_steps)
        print(f" > {robot_name} moved forward by {int (number_of_steps)} steps.")
        sprint_command(robot_name,int(number_of_steps) - 1, coordinates)


def robot_start():
    """This is the entry function, do not change"""

    global i
    robot_name = get_robot_name()
    print(f"{robot_name}: Hello kiddo!")
    coordinates = {# i want to keep track of the coordinates of the robot
        "X": 0,
        "Y": 0,
        "turns":0,
        "direction": "up" 
    }
  
    while True:
        get_user_command = get_command(robot_name).split()
        if get_user_command[0].upper() in list_of_commands():
            if get_user_command[0].upper() == "FORWARD":
                move_forward(robot_name, get_user_command[1], coordinates)
            if get_user_command[0].upper() == "SPRINT":
                sprint_command(robot_name,get_user_command[1],coordinates)    
            if get_user_command[0].upper() == "BACK":
                move_backward(robot_name, get_user_command[1], coordinates)
            if get_user_command[0].upper() == "HELP":
                print("I can understand these commands:")
                command_information()
            if get_user_command[0].upper() == "RIGHT":
                turn_right(robot_name, coordinates)
            if get_user_command[0].upper() == "LEFT":
                turn_left(robot_name,coordinates)    
            if get_user_command[0].upper() == "OFF":
                print(f"{robot_name}: Shutting down..")
                break

            robot_position(robot_name, coordinates)
        else:
            print(f"{robot_name}: Sorry, I did not understand '{' '.join(get_user_command)}'.")
    i = 0

if __name__ == "__main__":
    robot_start()
