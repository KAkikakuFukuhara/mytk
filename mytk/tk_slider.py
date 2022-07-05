import tkinter as tk



class SlideBarFrame(tk.LabelFrame):
    def __init__(self, master=None, title:str="slidebar", from_:int=0, to:int=255, length:int=300):
        super().__init__(master, text=title)
        self.var = tk.IntVar()
        self.var.set(from_)
        self.slidebar = tk.Scale(self, orient="h", variable=self.var, from_=from_, to=to, length=length)
        self.slidebar.pack()

class RangeSlideBarFrame(tk.LabelFrame):
    """ This is LableFrame Widget that contain two sliderbar widiget.

        Args:
            master : tk master;
            title : label frame name;
            from_ : bar min value;
            to : bar max value;
            length : bar widget length;
    """
    def __init__(self, master=None, title:str="slidebar", from_:int=0, to:int=255, length:int=300):

        super().__init__(master, text=title)
        self.var1 = tk.IntVar()
        self.var1.set(from_)
        self.slidebar1 = tk.Scale(self, orient="h", variable=self.var1, from_=from_, to=to, length=length, command=self.print_var)
        self.slidebar1.pack()

        self.var2 = tk.IntVar()
        self.var2.set(to)
        self.slidebar2 = tk.Scale(self, orient="h", variable=self.var2, from_=from_, to=to, length=length, command=self.print_var)
        self.slidebar2.pack()

    def print_var(self, _):
        """ print tow value that each scrollbar value
        """
        print(f"{self.var1.get()}-{self.var2.get()}")

    def set_slide_func(self, func):
        self.slidebar1.config(command=func)
        self.slidebar2.config(command=func)

class SingleSlideBarValue:
    def __init__(self, bar:SlideBarFrame):
        self.var = bar.var
        self.update()

    def update(self):
        self.value = self.var.get()

    def get_value(self):
        return self.value

class DoubleSlideBarValue:
    def __init__(self, bar:RangeSlideBarFrame):
        self.var1 = bar.var1
        self.var2 = bar.var2
        self.update()
        
    def update(self):
        self.value1 = self.var1.get()
        self.value2 = self.var2.get()

    def get_values(self):
        return self.value1, self.value2

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.canvas = tk.Canvas(self, width=300, height=150)
        self.canvas.pack()
        self.canvas.create_rectangle(0, 0, 300, 150, fill="#000000")

        self.var = tk.IntVar(self, value=0)
        self.slidebar = tk.Scale(self, orient="h", variable=self.var, from_=0, to=255, length=300, command=self.slide)
        self.slidebar.pack()

    def slide(self, var):
        self.canvas.delete()
        self.canvas.create_rectangle(0, 0, 300, 150, fill=f"#{int(var):02x}0000")

class App2(tk.Tk):
    def __init__(self):
        super().__init__()
        self.canvas = tk.Canvas(self, width=300, height=150)
        self.canvas.pack()
        self.canvas.create_rectangle(0, 0, 300, 150, fill="#000000")

        self.var_r = tk.IntVar(self, value=0)
        self.slidebar_r = tk.Scale(self, orient="h", variable=self.var_r, from_=0, to=255, length=300, command=self.slide)
        self.slidebar_r.pack()

        self.var_g = tk.IntVar(self, value=0)
        self.slidebar_g = tk.Scale(self, orient="h", variable=self.var_g, from_=0, to=255, length=300, command=self.slide)
        self.slidebar_g.pack()

        self.var_b = tk.IntVar(self, value=0)
        self.slidebar_b = tk.Scale(self, orient="h", variable=self.var_b, from_=0, to=255, length=300, command=self.slide)
        self.slidebar_b.pack()

    def slide(self, var):
        var_r = self.var_r.get()
        var_g = self.var_g.get()
        var_b = self.var_b.get()
        self.canvas.delete()
        self.canvas.create_rectangle(0, 0, 300, 150, fill=f"#{var_r:02x}{var_g:02x}{var_b:02x}")

class App3(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.h_slidebar = RangeSlideBarFrame(self, title="Hue")
        self.l_slidebar = RangeSlideBarFrame(self, title="Lightness")
        self.s_slidebar = RangeSlideBarFrame(self, title="Saturation")

        self.values = AppSlideBarValue(self)

        self.h_slidebar.pack() 
        self.l_slidebar.pack() 
        self.s_slidebar.pack() 

        self.h_slidebar.set_slide_func(self.update_value)
        self.l_slidebar.set_slide_func(self.update_value)
        self.s_slidebar.set_slide_func(self.update_value)

    def update_value(self, _):
        self.values.update()
        print(f"H_range:{self.values.h_range}")
        print(f"L_range:{self.values.l_range}")
        print(f"S_range:{self.values.s_range}")

class AppSlideBarValue:
    def __init__(self, bars:App3):
        self.h_values = DoubleSlideBarValue(bars.h_slidebar)
        self.l_values = DoubleSlideBarValue(bars.l_slidebar)
        self.s_values = DoubleSlideBarValue(bars.s_slidebar)

        self.h_range = None
        self.l_range = None
        self.s_range = None
        self.update()

    def update(self):
        self.h_values.update()
        self.l_values.update()
        self.s_values.update()

        self.h_range = self.h_values.get_values()
        self.l_range = self.l_values.get_values()
        self.s_range = self.s_values.get_values()

import cv2
import numpy as np
from PIL import Image, ImageTk
class ColorScale(tk.LabelFrame):
    def __init__(self, master=None):
        super().__init__(master, text="Color Scale")
        self.canvas = tk.Canvas(self, width=180, height=10)
        self.var = tk.IntVar()
        self.var.set(0)
        self.scale = tk.Scale(self, orient="h", from_=0, to=179, length=180, command=self.slide)
        self.scale.pack()
        self.canvas.pack()

        hls_l = 128
        hls_s = 255
        hls = [ [ [ hls_h, hls_l, hls_s ]  for hls_h in range(180) ] for _ in range(10) ]
        hls = np.array(hls, dtype="uint8")
        h_rgb = cv2.cvtColor(hls, cv2.COLOR_HLS2RGB)
        image = Image.fromarray(h_rgb)
        self.image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, image=self.image, anchor="nw")

    def slide(self, v):
        value = int(v)
        hls = np.array([[[value, 128, 255]]], dtype="uint8")
        rgb = cv2.cvtColor(hls, cv2.COLOR_HLS2RGB)
        rgb = rgb.flatten().tolist()
        rgb = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        self.scale.config(troughcolor=rgb)


def func(value):
    print(value ** 2)

if __name__ == "__main__":
    pass