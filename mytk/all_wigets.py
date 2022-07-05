import tkinter as tk

def show_all_widgets():
    root = tk.Tk()

    # *** Known ***
    # canvas
    canvas = tk.Canvas(root, width=100, height=100, bg="black")
    canvas.grid(row=0, column=0)
    # label
    label = tk.Label(root, text="label")
    label.grid(row=1, column=0)
    # labelframe
    labelframe = tk.LabelFrame(root, text="labelframe", width=100, height=100)
    labelframe.grid(row=2, column=0)
    # frame
    frame = tk.Frame(root, width=100, height=100, bg="white")
    frame.grid(row=3, column=0)
    # button
    button = tk.Button(root, text="Button")
    button.grid(row=4, column=0)
    # scale
    scale = tk.Scale(root, orient="h")
    scale.grid(row=5, column=0)
    # radio
    radiobtn = tk.Radiobutton(root)
    radiobtn.grid(row=6, column=0)
    # menu
    menu = tk.Menu(root)
    menu.add_cascade(label="FILE")
    root.config(menu=menu)
    # entry
    entry = tk.Entry(root)
    entry.grid(row=7, column=0)

    # *** UnUse ***
    # checkbutton
    checkbutton = tk.Checkbutton(root)
    checkbutton.grid(row=0, column=1)
    # listbox
    listbox = tk.Listbox(root)
    listbox.grid(row=1, column=1)
    # scrollbar
    scrollbar = tk.Scrollbar(root)
    scrollbar.grid(row=2, column=1)
    # menubutton
    menubtn = tk.Menubutton(root, text="menu", relief=tk.RAISED)
    menubtn.grid(row=3, column=1)
    # Message
    message = tk.Message(root, text="aaaa")
    message.grid(row=4, column=1)
    # bitmap
    # text
    # spinbox
    # panedwindow

    root.mainloop()

if __name__ == "__main__":
    show_all_widgets()