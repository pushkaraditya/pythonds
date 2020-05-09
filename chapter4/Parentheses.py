import sys
sys.path.append('../')

from basic import stack

def parChecker(str):
    if len(str) == 0:
        return True

    openings = "({[`""" # small bracker curly bracket big bracket single quote tick double quotes
    closings = ")}]'`"""

    s = stack.Stack()
    for c in str:
        if c in openings:
            s.push(c)
        elif c in closings:
            if s.isEmpty():
                return False
            if openings[closings.index(c)] != s.pop():
                return False
    return s.isEmpty()


print(parChecker('{ { ( [ ] "`"[ ] ) } ( ) }'))
print(parChecker('[ [ { { ( ( ) ) } } ] ]'))
print(parChecker('[ ] [ ] [ ] ( ) { }'))

# print(parChecker('{({([][])}())}'))
# print(parChecker('[{()]'))

# print(parChecker('([])'))
# print(parChecker('([)]'))
# print(parChecker(')('))

# print(parChecker('((()))'))
# print(parChecker('(()'))
