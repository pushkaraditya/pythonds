import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

A = [7,8,65,4,3,45,67,8,64]

fig, ax = plt.subplots()
ax.set_title('this is testing')
bar_rects = ax.bar(range(len(A)), A, align="edge")
text = ax.text(0.02, 0.95, "", transform = ax.transAxes)

iteration = [0]
def update_fig(A, rects, iteration):
    for rect, val in zip(rects, A):
        rect.set_height(val)
    iteration[0] += 1
    text.set_text("# of operations: {}".format(iteration[0]))

# anim = animation.FuncAnimation(fig, func=update_fig,
#     fargs=(bar_rects, iteration), frames=generator, interval=1,
#     repeat=False)
plt.show()

print('it worked!')