import turtle

big_line = 100
little_line = 50
angle = 90

t = turtle.Turtle()
s = turtle.Screen()

t.left(angle)
t.forward(big_line)
count = 0
while count < 4:
    t.right(angle//2)
    if count != 3:
        t.forward(little_line)
    else:
        t.forward(big_line)
    count = count + 1
t.right(90)
t.forward(130)
s.exitonclick()