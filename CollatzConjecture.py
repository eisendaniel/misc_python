from tkinter import Tk, Canvas
import numpy as np

GR = 1.61803398875
PI = np.pi


def collatz(start):
    n = int(start)
    seq = np.array([n])
    while n > 1:
        n = 3 * n + 1 if n % 2 else n / 2
        seq = np.append(seq, int(n))
    return seq[::-1]


def collatz_parity(start):
    n = int(start)
    seq = np.array([])
    while n > 1:
        if n % 2:
            n = 3 * n + 1
            seq = np.append(seq, PI / 15)
        else:
            n /= 2
            seq = np.append(seq, -PI / 30)
    return seq[::-1]


class Collatz:
    def __init__(self, master):
        self.master = master
        master.title("Collatz Conjecture")

        width = 512
        height = width * GR
        border = (width - width / GR) / 2
        origin = {"x": width / 2, "y": height - border}

        canvas = Canvas(master, width=width, height=height)
        canvas.pack()

        segment_len = 3
        parity = collatz_parity(871)
        x = origin["x"]
        y = origin["y"]
        for p in parity:
            a = segment_len * np.sin(PI/2 - p)
            b = segment_len * np.cos(PI/2 - p)
            canvas.create_line(x, y, x - b, y - a)
            x -= b
            y -= a


# canvas.create_line(origin["x"], origin["y"], 0, 0)


root = Tk()
window = Collatz(root)
root.mainloop()
