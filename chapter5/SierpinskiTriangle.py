import turtle

def collect(t, size):
    vertices = []
    # t.up()
    vertices.append(t.position())
    t.fd(size)
    t.lt(120)
    vertices.append(t.position())
    t.fd(size)
    t.lt(120)
    vertices.append(t.position())
    t.fd(size)
    t.lt(120)
    return vertices

def calculateMid(A, B):
    return ( (A[0] + B[0])/2, (A[1] + B[1])/2)

def calculateMids(vertices):
    mids = []
    (A, B, C) = vertices
    mids.append(calculateMid(A, B))
    mids.append(calculateMid(B, C))
    mids.append(calculateMid(C, A))
    return mids

def SierpinskiTriangle(t, size, vertices, colorIndex):
    if size > 10:
        if colorIndex >= len(colors):
            colorIndex = 0
    # if colorIndex < len(colors):
        mids = calculateMids(vertices)

        t.up()
        t.goto(mids[0])
        t.down()

        t.fillcolor(colors[colorIndex])
        t.begin_fill()
        t.goto(mids[1])
        t.goto(mids[2])
        t.goto(mids[0])
        t.end_fill()
        SierpinskiTriangle(t, size/2, [vertices[0], mids[0], mids[2]], colorIndex + 1)
        SierpinskiTriangle(t, size/2, [mids[0], vertices[1], mids[1]], colorIndex + 1)
        SierpinskiTriangle(t, size/2, [mids[2], mids[1], vertices[2]], colorIndex + 1)



t = turtle.Turtle()
win = turtle.Screen()

t.up()
t.goto(-250, -200)
t.down()

initial_trianle_size = 500
colors = ['red', 'purple', 'blue', 'green', 'orange']
colors = ['blue', 'purple', 'red', 'green', 'orange']

vertices = collect(t, initial_trianle_size)
# print(vertices)

SierpinskiTriangle(t, initial_trianle_size, vertices, 0)
t.up()
t.goto(0,0)

win.exitonclick()
