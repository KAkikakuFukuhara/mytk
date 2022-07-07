import tkinter as tk

class ScrollFrame(tk.Frame):
    def __init__(self, master=None, hsize:int=20, wsize:int=20):
        super().__init__(master)
        
        self.value = tk.StringVar()
        
        self.listbox = tk.Listbox(self, listvariable=self.value, height=hsize, width=wsize)
        self.scrollbary = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=self.scrollbary.set)
        self.scrollbarx = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.listbox.xview)
        self.listbox.configure(xscrollcommand=self.scrollbarx.set)

        self.listbox.grid(row=0, column=0)
        self.scrollbary.grid(row=0, column=1, sticky="ns")
        self.scrollbarx.grid(row=1, column=0, sticky="we")

        self.listbox.bind("<Double-Button-1>", self.select_data)
        self.callback = None

    def set_data(self, data:list):
        for d in data:
            self.listbox.insert('end', str(d))


    def delete_data(self):
        self.listbox.delete(0, 'end')


    def select_data(self, *args):
        curr_value = self.listbox.get(self.listbox.curselection())
        if self.callback is None:
            print(curr_value)
        else:
            self.callback(curr_value)


    def set_callback(self, callback):
        self.callback = callback


if __name__ == "__main__":

    def print_value(value):
        print(f"CLICK:{value}")

    app = tk.Tk()
    frame = ScrollFrame(app, hsize=5, wsize=100)
    frame.pack()
    frame.set_data([str(i) for i in range(10)])
    frame.set_callback(print_value)
    app.mainloop()