def my_function():
    print("Hello")

my_function()

def box():
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def one_step():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_left()
    while front_is_clear():
        move()


while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        one_step()

# for step in range(0,6):
#     one_step()

# while not at_goal():
#     one_step()

while not at_goal():
    if wall_in_front() and wall_in_right():
        turn_left()
        while not wall_in_front():
            move()
    elif wall_in_front():
        turn_right()
        # if wall_in_right():
        #     turn_right()
        while not wall_in_front():
            move()


