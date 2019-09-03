from turtle import forward, done, circle, left, pencolor, pensize
left(25)
for i in range(3, 59):
    pencolor((0.015 * i, 0.7 - 0.01 * i, 1 - 0.015 * i))
    pensize(1)
    circle(15)
    pensize(3)
    forward(20)
    left(30 - i)
done()
