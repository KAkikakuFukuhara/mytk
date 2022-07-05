import tkinter as tk

class ScrollFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.value = tk.StringVar()
        
        self.listbox = tk.Listbox(self, listvariable=self.value, height=20)
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=self.scrollbar.set)

        self.listbox.grid(row=0, column=0)
        self.scrollbar.grid(row=0, column=1)
    
    def set_data(self, data:list):
        for d in data:
            self.listbox.insert('end', str(d))

    def delete_data(self):
        self.listbox.delete(0, 'end')

if __name__ == "__main__":
    app = tk.Tk()

    frame = ScrollFrame(app)
    frame.pack()
    frame.set_data([str(i) for i in range(10)])
    app.mainloop()