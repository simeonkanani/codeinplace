from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def fill_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

def move_back():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def main():
    while front_is_clear():
        fill_row()
        move_back()
        turn_left()
        if front_is_clear():
            move()
            turn_right()
        else:
            turn_right()
            while front_is_clear():
                move()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
