import tkinter as tk


class Tk_Frame(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.geometry("500x500")
        #self.resizable(0, 0)

        frame_1 = Tk_Frame(self, background="black")
        frame_1.pack(fill=tk.BOTH, padx=5, pady=5, side=tk.TOP, expand=True)
        frame_2 = Tk_Frame(self, background="#0000ff")
        frame_2.pack(fill=tk.BOTH, padx=5, pady=5, side=tk.TOP, expand=True)
        tk.Label(frame_1, text="Frame1").pack(padx=10, side=tk.LEFT)
        tk.Label(frame_2, text="Frame2").pack()

        self.mainloop()


app = Application()

