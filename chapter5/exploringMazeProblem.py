import turtle

blockCell = 'X'
openCell = ''
startingCell = 'S'
class Maze():
    ch = 25 # cell height
    cw = 25 # cell width
    bc = 'grey' # color for blocked cell
    dc = 'white' # color of open cell
    wip = 'yellow'
    dead = 'red'
    path = 'green'

    def __init__(self, turtle, maze):
        self.m = maze
        self.t = turtle
        self.pos = self.t.pos()
        self.start = None
        self.draw()
        self.setStartPointer(self.start)
        self.solve()

    def getColor(self, v):
        color = self.dc
        if v == blockCell: # blocked
            color = self.bc
        elif v == startingCell:
            color = self.wip
        return color

    def drawCell(self, i, j, color):
        x, y = self.getCellStart(i, j)
        self.t.up()
        self.t.goto(x, y)
        self.t.down()
        self.t.fillcolor(color)
        self.t.begin_fill()
        self.t.goto(x + self.cw, y)
        self.t.goto(x + self.cw, y + self.ch)
        self.t.goto(x, y + self.ch)
        self.t.goto(x, y)
        self.t.end_fill()

    def getCellStart(self, i, j):
        y = self.pos[1] - i * self.cw
        x = self.pos[0] + j * self.ch
        return x, y

    def draw(self):
        i = 0
        for row in self.m:
            j = 0
            for c in row:
                if c == startingCell:
                    self.start = (i, j)
                    # print(self.start)
                color = self.getColor(c)
                self.drawCell(i, j, color)
                j += 1
            i += 1

    def setStartPointer(self, p):
        i, j = p
        x, y = self.getCellStart(i, j)
        self.t.up()
        self.t.goto(x, y)
        self.t.down()

    def copyMaze(self):
        self.cm = [[v for v in row] for row in self.m] # copied maze

    def evaluate(self, i, j):
        pass

    def solve(self):
        # i, j = self.start
        self.copyMaze()
        print(self.cm)
        self.drawCell(1, 1, self.wip)
        self.drawCell(2, 1, self.wip)
        self.drawCell(2, 1, self.path)
        self.drawCell(1, 1, self.path)




def main():
    t = turtle.Turtle()
    s = turtle.Screen()
    t.up()
    t.goto(-300, 220)
    t.down()


    x = blockCell
    S = startingCell
    o = openCell
    # m = [
    #         [x,x,x,x,x],
    #         [x,o,o,o,x],
    #         [o,o,x,o,x],
    #         [x,x,o,o,x],
    #         [x,x,o,x,x]
    # ]
    # m = [
    #         [x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x],
    #         [x,o,o,o,x,o,o,o,x,x,o,x,x,o,o,o,o,o,x,o,o,o],
    #         [x,o,x,o,o,o,x,o,o,o,o,o,o,o,x,x,x,o,x,o,x,x],
    #         [x,o,x,o,x,o,o,x,x,o,o,x,x,x,x,o,o,o,x,o,x,x],
    #         [x,x,x,o,x,x,x,x,x,x,o,o,o,o,x,x,x,o,x,o,o,x],
    #         [x,o,o,o,o,o,o,o,o,o,o,x,x,o,o,x,x,o,o,o,o,x],
    #         [x,x,x,x,x,o,x,x,x,x,x,x,o,o,o,x,x,x,x,x,o,x],
    #         [x,o,o,o,o,o,x,o,o,o,x,x,x,x,x,x,x,o,o,x,o,x],
    #         [x,o,x,x,x,x,x,x,x,o,o,o,o,o,o,S,o,x,o,o,o,x],
    #         [x,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,x,o,x,x,x],
    #         [x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,o,x,x,x],
    #     ]
    m = [
        [x,x,x],
        [x,S,x],
        [x,o,x]
    ]

    m = Maze(t, m)

    s.exitonclick()

main()