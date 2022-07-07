import tkinter as tk
from typing import Callable

from PIL import Image, ImageTk
import numpy as np

class CanvaCustom(tk.Canvas):
    def __init__(self, master=None, wsize:int=640, hsize:int=480):
        super().__init__(master, width=wsize, height=hsize)
        self.wsize = wsize
        self.hsize = hsize
        self.cx = wsize // 2
        self.cy = hsize // 2
        self.resize_ratio = 1.0

        self.imgtk = None

        bg_img = np.zeros((hsize, wsize, 3), dtype="uint8")
        self.create_canvas_bg(bg_img)

        self.bind("<Button-1>", self.click_canvas)
        self.click_callback = None


    def create_canvas_bg(self, rgb_img:np.ndarray):
        self.bg_img = rgb_img
        self.bg_imgtk = self.resize_img2canvas(rgb_img)
        self.create_image((self.cx, self.cy), image=self.bg_imgtk)


    def set_image(self, rgb_img:np.ndarray):
        self.src_img = rgb_img
        self.imgtk = self.resize_img2canvas(rgb_img)
        self.create_image((self.cx, self.cy), image=self.imgtk)


    def resize_img2canvas(self, rgb_img:np.ndarray):
        src_hsize, src_wsize = rgb_img.shape[:2]
        if src_hsize > src_wsize:
            self.resize_ratio = self.hsize / src_hsize
        else:
            self.resize_ratio = self.wsize / src_wsize
        out_wsize = int(self.resize_ratio * src_wsize)
        out_hsize = int(self.resize_ratio * src_hsize)
        out_img = Image.fromarray(rgb_img).resize((out_wsize, out_hsize))
        return ImageTk.PhotoImage(out_img)


    def get_image(self) -> np.ndarray:
        return self.src_img


    def click_canvas(self, event:tk.Event):
        px = event.x
        py = event.y
        org_px, org_py = self.resize_point(px, py)
        if self.click_callback is not None:
            self.click_callback(org_px, org_py, self.resize_ratio)

    def resize_point(self, px:int, py:int):
        if self.imgtk is None:
            return px, py

        pad_x = round((self.wsize - self.imgtk.width()) / 2)
        pad_y = round((self.hsize - self.imgtk.height()) / 2)

        org_px = px - pad_x
        org_py = py - pad_y
        return org_px, org_py


    def set_click_callback(self, func:Callable):
        self.click_callback = func


if __name__ == "__main__":
    def callback(px, py, resize_ratio):
        print(f"px:{px}, py:{py}, ratio:{resize_ratio}")

    root = tk.Tk()
    canvas = CanvaCustom(root)
    canvas.pack()
    canvas.set_click_callback(callback)
    root.mainloop()