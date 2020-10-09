import matplotlib.pyplot as plt


graph_types_for_one = ['bar', 'box', 'hist', 'line', 'area']
graph_types_for_two = ['line', 'scatter', 'area', 'hexbin']
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']
color_index = 0


def plot_one(x, kind, db):
    if kind not in graph_types_for_one:
        print("Wrong kind of graph")
        return

    db[x].plot(kind=kind, color=colors[color_index], legend=True)
    configure()


def plot_two(x, y, kind, db):
    if kind not in graph_types_for_two:
        print("Wrong kind of graph")
        return
    db.plot(x=x, y=y, kind=kind, xlabel=x, ylabel=y, color=colors[color_index], legend=True, xticks=range(min(db[x]), max(db[x]), 20))
    configure()


def plot(db, kind, *args):
    if len(args) == 1:
        plot_one(args[0], kind, db)
    elif len(args) == 2:
        plot_two(args[0], args[1], kind, db)
    else:
        print("Must be one or two fields to make graphic")


def configure():
    global color_index
    if color_index == len(colors) - 1:
        color_index = 0
    else:
        color_index += 1
    plt.grid()


def show():
    plt.show()

