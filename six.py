def move(): pass
def turn_left(): pass
def front_is_clear(): return True
def right_is_clear(): return True
def at_goal(): return False

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()