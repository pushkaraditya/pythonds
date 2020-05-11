import turtle

t = turtle.Turtle()
s = turtle.Screen()
colors = ['red', 'purple', 'blue', 'green', 'orange']

# for i in range(100):
#     t.pencolor(colors[i % 5])
#     t.width(i/10 + 1)
#     t.forward(i)
#     t.left(59)


# circle_size = 10
# for i in range(20):
#     t.fillcolor(colors[i%5])
#     t.begin_fill()
#     # t.pencolor(colors[i%5])
#     t.circle(circle_size)
#     t.end_fill()
#     t.lt(20)

# t.up()
# t.goto(0, -100)
# t.down()
# for angle in range(0, 360, 10):
#     t.setheading(angle)
#     t.fd(50)
#     t.write(str(angle))
#     t.bk(25)

for i in range(5):
    t.fd(100)
    t.rt(144)

s.exitonclick()