from tkinter import Canvas, Tk


class Flag:
    def __init__(self, master):
        self.master = master
        master.title("Pan")

        margin = 5
        golden = ((1 + 5 ** 0.5) / 2)
        self.height = 500
        self.width = int(self.height * golden)

        canvas = Canvas(master, width=self.width + (2 * margin), height=self.height + (2 * margin))
        
        canvas.create_rectangle(margin, margin, margin + self.width, margin + self.height * (1 / 3),
                                fill="#ff0054", width=0)
        canvas.create_rectangle(margin, margin + self.height * (1 / 3), margin + self.width, margin + self.height * (2 / 3),
                                fill="#ffde00", width=0)
        canvas.create_rectangle(margin, margin + self.height * (2 / 3), margin + self.width, margin + self.height,
                                fill="#007dff", width=0)
        canvas.pack()


root = Tk()
window = Flag(root)
root.mainloop()
