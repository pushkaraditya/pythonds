import turtle

myTurtle = turtle.Turtle()
win = turtle.Screen()
# (X, Y) = win.screensize()
# myTurtle.penup()
# myTurtle.setx(-100)
# myTurtle.sety(250)
# myTurtle.pendown()

def drawSpiral(len):
    if len > 0:
        myTurtle.forward(len)
        myTurtle.right(72)
        drawSpiral(len - 5)

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-10,t)
        t.right(20)
        t.backward(branchLen)


def main(t):
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    
# drawSpiral(200)
main(myTurtle)
win.exitonclick()
