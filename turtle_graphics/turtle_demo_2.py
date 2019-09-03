from turtle import color, begin_fill, forward, right, end_fill, done, circle
color('red', 'yellow')
begin_fill()
for i in range(108):
    if i < 90:
        circle(25)
    forward(i)
    right(20)
end_fill()
done()
