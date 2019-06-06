from tkinter import Tk, Scale, Canvas, HORIZONTAL
import math


class Sierpinski:
    def __init__(self, master):
        self.master = master

        # Window dimensions and fields
        self.depth = 1
        self.index = 0
        self.colors = ["white", "#444444"]
        self.width = 600
        self.height = int(round(self.width * math.sqrt(3) / 2))
        self.margin = 10

        # Setup Tk
        Tk.config(master, bg=self.colors[self.index])
        master.title("Sierpinski")
        master.iconbitmap('tri.ico')
        master.bind("<space>", self.invert)
        master.bind("<Key-Up>", self.updatedepth)
        master.bind("<Key-Down>", self.updatedepth)
        master.bind("<Key-Right>", self.updatedepth)
        master.bind("<Key-Left>", self.updatedepth)

        # setup window
        self.canvas = Canvas(master, width=self.width + (2 * self.margin), height=self.height + (2 * self.margin))
        self.canvas.config(bg=self.colors[self.index], highlightthickness=0)
        self.canvas.bind("<Button-1>", self.invert)
        self.canvas.pack()

        # slider to set triangle depth
        self.level = Scale(master, from_=1, to=8, orient=HORIZONTAL, command=self.updatedepth)
        self.level.config(bg=self.colors[self.index], highlightthickness=0)
        self.level.pack()

        self.draw(self.level.get())

    def updatedepth(self, event):
        try:
            if event.keysym in ("Up", "Right"):
                self.depth = 8 if self.depth == 8 else self.depth + 1
            elif event.keysym in ("Down", "Left"):
                self.depth = 1 if self.depth == 1 else self.depth - 1
            self.level.set(self.depth)
        except AttributeError:
            self.depth = self.level.get()

        self.draw(self.depth)

    def invert(self, event):
        self.index = 1 if self.index == 0 else 0
        self.draw(self.depth)

    def draw(self, level):
        # clear canvas
        self.canvas.delete("all")

        x1 = self.margin
        y1 = self.margin + self.height
        x2 = self.margin + self.width / 2
        y2 = self.margin
        x3 = self.margin + self.width
        y3 = self.margin + self.height

        self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=self.colors[self.index], outline=self.colors[self.index - 1])
        self.recursion(int(level), x1, y1, x2, y2, x3, y3)

    def recursion(self, level, x1, y1, x2, y2, x3, y3):
        color = self.colors[self.index - 1]
        if level <= 1:
            self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=color)
        else:
            left_x = (x1 + x2) / 2
            left_y = (y1 + y2) / 2

            right_x = (x2 + x3) / 2
            right_y = (y2 + y3) / 2

            bottom_x = (x3 + x1) / 2
            bottom_y = (y3 + y1) / 2

            self.recursion(level - 1, x1, y1, left_x, left_y, bottom_x, bottom_y)
            self.recursion(level - 1, left_x, left_y, x2, y2, right_x, right_y)
            self.recursion(level - 1, bottom_x, bottom_y, right_x, right_y, x3, y3)


# create and start main window
root = Tk()
window = Sierpinski(root)
root.mainloop()
