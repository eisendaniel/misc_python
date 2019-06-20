from tkinter import Tk, Canvas


def collatz(n):
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n *= 0.5
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq

class Window:
    def __init__(self, master):
        self.master = master
        master.title("Collatz")

        size = 512
        canvas = Canvas(master, width=size, height=size)
        canvas.pack()


        x = size
        y = size/2
        while x != 1:
            lastx = x
            lasty = y
            if x % 2 == 0:
                x *= 0.5
                y += 1
            else:
                x = 3 * x + 1
                y -= 1
            canvas.create_line(lasty, lastx, y, x)


root = Tk()
window = Window(root)
root.mainloop()
