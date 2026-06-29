import turtle
from turtle import *


def square():
   
    def reset():
        clear()
        setx(0)
        sety(0)

    reset()
    pendown()

    times = 4
    for i in range(times):
        forward(100)
        left(90)

    print("Process has been completed, Review the output and close the windows to end the process.")
    print("Done!")
    done()

def triangle():
    def reset():
        clear()
        setx(0)
        sety(0)

    reset()
    pendown()

    times = 3
    for i in range(times):
        forward(100)
        left(120)

    print("Process has been completed, Review the output and close the windows to end the process.")
    print("Done!")
    done()
