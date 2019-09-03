from turtle import color, begin_fill, forward, left, right, pos, end_fill, done
color('red', 'yellow')
begin_fill()
for i in range(6):
    for _ in range(6):
        forward(200)
        left(170)
    left(120)
    forward(30)
end_fill()
done()
