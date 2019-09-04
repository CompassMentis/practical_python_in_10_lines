import turtle
def line(length):
    if length <= 15:
        turtle.forward(length)
        return
    for angle in (60, -120, 60, 0):
        line(length / 3)
        turtle.left(angle)

line(270)
# turtle.begin_fill()
# turtle.color('firebrick3', 'wheat')
# for _ in range(3):
#     line(90)
#     turtle.right(120)
# turtle.end_fill()
turtle.done()
