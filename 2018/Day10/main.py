from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import re

def read_input():
    input = open('2018/Day10/input.txt','r').read().splitlines()
    input_list = list()
    for line in input:
        position = list(map(int, line[10:24].split(', ')))
        velocity = list(map(int, line[36:42].split(', ')))
        input_list.append(position + velocity)
    return input_list
def read_sample_input():
    input = open('2018/Day10/input_sample.txt','r').read().splitlines()
    input_list = list()
    for line in input:
        input_list.append([int(s) for s in re.findall(r'-?\d+\.?\d*', line)])
    return input_list
def plot_sample(input):
    for index in range(4):
        x = [i[0] for i in input]
        y = [i[1] for i in input]
        plt.scatter(x, y)
        plt.show()
        for row in input:
            row[0] += row[2]
            row[1] += row[3]
def animate_scatter(input):
    fig = plt.figure()
    x = [i[0] for i in input]
    y = [i[1] for i in input]
    ax = fig.add_subplot(111)
    ax.grid(True, linestyle = '-', color = '0.75')
    ax.set_xlim([-20, 20])
    ax.set_ylim([-20, 20])
    scat = plt.scatter(x,y, c=x)
    scat.set_alpha(0.8)
    anim = animation.FuncAnimation(fig, _update_plot, fargs=(fig,scat), frames=100, interval=100)
    plt.show()
def _update_plot(i, fig, scat):
    for row in input:
        row[0] += row[2]*100
        row[1] += row[3]*100
    x = [i[0] for i in input]
    y = [i[1] for i in input]
    plt.clf()
    scat = plt.scatter(x,y)
    return scat,
def plot_message(input):
    for i in range(10391):
        for row in input:
            row[0] = row[0] + row[2]
            row[1] += row[3]
    x = [i[0] for i in input]
    y = [i[1] for i in input]
    plt.scatter(x,y )
    plt.show()


input = read_input()
input_s = read_sample_input()
input_copy = read_input()

#plot_sample(input_s)
#animate_scatter(input)
plot_message(input_copy)    # extend the window to read the message easily
                            # also it is mirrored, upside down?
