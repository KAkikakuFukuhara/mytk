import tkinter as tk
from typing import Callable, Tuple

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

        self.pil_img = None
        self.photoimg = None

        bg_img = np.zeros((hsize, wsize, 3), dtype="uint8")
        self.create_canvas_bg(bg_img)

        self.bind("<Button-1>", self.click_canvas)
        self.click_callback = None

        self.bind("<Button-4>", self.__zoom)
        self.bind("<Button-5>", self.__zoom)
        self.bind("<Button1-Motion>", self.__move_focus)

        self.scale_ratio = 1.0




    def create_canvas_bg(self, rgb_img:np.ndarray):
        self.bg_img = rgb_img
        self.bg_photoimg = ImageTk.PhotoImage(self.resize_img2canvas(rgb_img))
        self.create_image((self.cx, self.cy), image=self.bg_photoimg)


    def set_image(self, rgb_img:np.ndarray, do_resize:bool=True):
        self.src_img = rgb_img
        if do_resize:
            self.pil_img = self.resize_img2canvas(rgb_img)
        else:
            self.pil_img = Image.fromarray(rgb_img)
        self.photoimg = ImageTk.PhotoImage(self.pil_img)
        self.focus_px = self.cx
        self.focus_py = self.cy
        self.create_image((self.cx, self.cy), image=self.photoimg)


    def resize_img2canvas(self, rgb_img:np.ndarray):
        src_hsize, src_wsize = rgb_img.shape[:2]
        if src_hsize > src_wsize:
            self.resize_ratio = self.hsize / src_hsize
        else:
            self.resize_ratio = self.wsize / src_wsize
        out_wsize = int(self.resize_ratio * src_wsize)
        out_hsize = int(self.resize_ratio * src_hsize)
        out_img = Image.fromarray(rgb_img).resize((out_wsize, out_hsize))
        return out_img


    def get_image(self) -> np.ndarray:
        return self.src_img


    def click_canvas(self, event:tk.Event):
        px = event.x
        py = event.y
        org_px, org_py = self.resize_point(px, py)
        if self.click_callback is not None:
            self.click_callback(org_px, org_py, self.resize_ratio)


    def resize_point(self, px:int, py:int):
        if self.pil_img is None:
            return px, py

        pad_x = round((self.wsize - self.pil_img.width) / 2)
        pad_y = round((self.hsize - self.pil_img.height) / 2)

        org_px = px - pad_x
        org_py = py - pad_y
        return org_px, org_py


    def set_click_callback(self, func:Callable):
        self.click_callback = func


    def __zoom(self, event):
        if self.pil_img is None:
            return

        pil_img = self.resize_img2canvas(self.src_img)

        old_scale_ratio = self.scale_ratio
        if event.num == 4: # zoom in
            if self.scale_ratio < 3.0:
                self.scale_ratio = round(self.scale_ratio + 0.50, 1)
            else:
                return
        if event.num == 5: # zoom out
            if self.scale_ratio > 1.0:
                self.scale_ratio = round(self.scale_ratio - 0.50, 1)
            else:
                return

        # scaling
        out_wsize = int(pil_img.width * self.scale_ratio)
        out_hsize = int(pil_img.height * self.scale_ratio)
        pil_img = pil_img.resize((out_wsize, out_hsize))
        self.focus_px = self.focus_px * self.scale_ratio / old_scale_ratio
        self.focus_py = self.focus_py * self.scale_ratio / old_scale_ratio

        # crop around focus point
        crop_box = (
            self.focus_px - (self.wsize // 2 - 1), # left
            self.focus_py - (self.hsize // 2 - 1), # top
            self.focus_px + (self.wsize // 2),     # right
            self.focus_py + (self.hsize // 2)      # under
        )
        crop_pil_img = pil_img.crop(crop_box)
        pil_img = crop_pil_img
        self.set_pil_img((self.cx, self.cy), pil_img)


    def set_pil_img(self, pt:Tuple, pil_img:Image.Image):
        self.pil_img = pil_img
        self.photoimg = ImageTk.PhotoImage(pil_img)
        self.create_image(pt, image=self.photoimg)


    def __move_focus(self, event):
        if self.pil_img is None:
            return

        x = event.x
        y = event.y
        self.focus_px = x * self.scale_ratio
        self.focus_py = y * self.scale_ratio
        self.__zoom(event)


if __name__ == "__main__":
    def callback(px, py, resize_ratio):
        print(f"px:{px}, py:{py}, ratio:{resize_ratio}")

    root = tk.Tk()
    canvas = CanvaCustom(root)
    canvas.pack()
    canvas.set_click_callback(callback)

    dummy_img = np.full((480, 640, 3), 255, dtype="uint8")
    dummy_img[200:240, 300:340] = 0
    canvas.set_image(dummy_img)

    root.mainloop()