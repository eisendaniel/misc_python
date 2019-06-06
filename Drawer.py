from tkinter import Canvas, Tk, OptionMenu, StringVar, Button, E, W
from tkinter.colorchooser import askcolor


class Drawer:
    def __init__(self, master):
        self.master = master
        master.title("Draw")

        margin = 5
        self.size = 512
        self.tmp = None
        self.tool = StringVar(master)
        self.tool.set("line")
        self.actions = []
        self.color = "black"
        self.pen_count = 0

        master.bind("<z>", self.undo)

        self.canvas = Canvas(master, width=self.size + (2 * margin), height=self.size + (2 * margin))
        self.canvas.config(bg="white", highlightthickness=0)
        self.canvas.bind("<Button-1>", self.mouse)
        self.canvas.bind("<B1-Motion>", self.mouse)
        self.canvas.bind("<ButtonRelease-1>", self.mouse)
        self.canvas.grid(row=0, columnspan=3)

        self.tools = OptionMenu(master, self.tool, "line", "pen", "rect", "oval")
        self.tools.grid(row=1, column=1)

        self.clr_btn = Button(master, text="Clear", command=lambda: [self.canvas.delete("all"), self.actions.clear()])
        self.clr_btn.grid(row=1, column=2, sticky=W)

        self.color_btn = Button(master, text="Color", command=self.choose_color)
        self.color_btn.grid(row=1, column=0, sticky=E)

    def mouse(self, event):
        if str(event.type) == "ButtonPress":
            self.pen_count += self.tool.get() == "pen"
            self.startx = event.x
            self.starty = event.y

        elif str(event.type) == "Motion":
            if self.tool.get() != "pen":
                self.canvas.delete(self.tmp)
            self.tmp = self.draw(self.startx, self.starty, event.x, event.y, self.tool.get())

        elif str(event.type) == "ButtonRelease":
            self.actions.append(self.draw(self.startx, self.starty, event.x, event.y, self.tool.get()))

    def draw(self, x0, y0, x1, y1, mode):
        if mode == "line":
            return self.canvas.create_line(x0, y0, x1, y1, fill=self.color, tags="line")

        elif mode == "pen":
            r = self.canvas.create_line(x0, y0, x1, y1, tags=("pen" + str(self.pen_count)))
            self.startx = x1
            self.starty = y1
            return r

        elif mode == "rect":
            return self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.color, width=0, tags="rect")

        elif mode == "oval":
            return self.canvas.create_oval(x0, y0, x1, y1, fill=self.color, width=0, tags="oval")

    def undo(self, event):
        if len(self.actions) == 0:
            return

        last = self.actions.pop()
        if "pen" in self.canvas.gettags(last)[0]:
            self.canvas.delete(("pen" + str(self.pen_count)))
            self.pen_count -= 1
        else:
            self.canvas.delete(last)
        self.canvas.delete(self.tmp)

    def choose_color(self):
        self.color = askcolor(color=self.color)[1]


root = Tk()
window = Drawer(root)
root.mainloop()
