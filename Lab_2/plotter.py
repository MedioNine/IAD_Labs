import matplotlib.pyplot as plt
import math

graph_types_for_one = ['bar', 'box', 'hist', 'line', 'area', 'pie']
graph_types_for_two = ['line', 'scatter', 'area', 'hexbin']
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']
color_index = 0


def plot_one(x, kind, db, axes):
    if kind not in graph_types_for_one:
        print("Wrong kind of graph")
        return

    if kind == 'pie':
        db[x].value_counts().plot(kind=kind, legend=True, ax=axes)
    else:
        db[x].plot(kind=kind, color=colors[color_index], legend=True, ax=axes)
    configure()


def plot_two(x, y, kind, db, axes):
    if kind not in graph_types_for_two:
        print("Wrong kind of graph")
        return
    db.plot(x=x, y=y, kind=kind, xlabel=x, ylabel=y, color=colors[color_index], legend=True,
            xticks=range(min(db[x]), max(db[x]), 20), ax=axes)
    configure()


def plot(db, cols):
    nrows, ncols = 1, 1;

    if len(cols) > 2:
        nrows = 2

    ncols = math.ceil(len(cols)/2)
    fig = plt.figure()
    index = 1

    for col in cols:
        axes = fig.add_subplot(ncols, nrows, index)
        if len(col) == 1:
            if db[col[0]].dtype.name == 'int64':
                plot_one(col[0], 'line', db, axes)
            else:
                plot_one(col[0], 'pie', db, axes[y, x])
        else:
            if len(col) == 2:
                plot_two(col[0], col[1], 'scatter', db, axes)
        index += 1
    show()


def configure():
    global color_index
    if color_index == len(colors) - 1:
        color_index = 0
    else:
        color_index += 1
    plt.grid()


def show():
    plt.show()
