""" tkinterを用いたGUIによるファイル選択プログラム
"""
import tkinter as tk 
from tkinter import filedialog
import os

def get_file_path(dir_path:str, file_suffix="pickle") -> str:
    file_types = [("", f"*.{file_suffix}")]
    file_path = filedialog.askopenfilename(filetypes=file_types, initialdir=dir_path)
    if type(file_path) != str:
        file_path = None
    return file_path

def get_file_path_not_gui(dir_path:str, file_suffix="pickle") -> str:
    root = tk.Tk()
    root.withdraw()
    file_types = [("", f"*.{file_suffix}")]
    file_path = filedialog.askopenfilename(filetypes=file_types, initialdir=dir_path)
    if type(file_path) != str:
        file_path = None

    root.destroy()
    return file_path

def test():
    file_dir_path = os.path.abspath(os.path.dirname(__file__))
    load_dir_path = f"{file_dir_path}/source"
    res = get_file_path(load_dir_path)
    print(res)
    
if __name__ == "__main__":
    test()

