import turtle

def line(length):
    if length <= 5:
        turtle.forward(length)
        return
    for angle in (60, -120, 60, 0):
        line(length / 3)
        turtle.left(angle)

line(810)
turtle.done()
