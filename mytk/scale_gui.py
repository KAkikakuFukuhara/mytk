""" スケールをクリックした時とアップデートした時の違いの確認
"""
from typing import Optional
import tkinter as tk
from datetime import timedelta

ONE_HOUR_MS = int(3600*1e6)

class TimeScaleBar(tk.Frame):
    def __init__(self, 
            master:Optional[tk.Widget]=None,
            from_ms:int=0,
            to_ms:int=ONE_HOUR_MS,
            length=1200):
        """ microsecond seekbar

        Args:
            master (Optional[tk.Widget], optional): parent widght. Defaults to None.
            from_ms (int, optional): scale left value. Defaults to 0.
            to_ms (int, optional): scale righ value. Defaults to ONE_HOUR_MS(3600*1e6).
            length (int, optional): width window size. Defaults to 1200.
        """
        super().__init__(master)
        self.var = tk.IntVar()
        self.var.set(from_ms)
        self.scale = tk.Scale(
            self, orient="horizontal", variable=self.var, 
            from_=from_ms, to=to_ms, length=length, showvalue=False)

        inited_time = str(timedelta(microseconds=0))
        self.elapd_time_label = tk.Label(self, text=f"{inited_time:15}/")
        self.total_time_label = tk.Label(self, text=f"{inited_time:15}")

        self.scale.grid(row=0, column=0, columnspan=2)
        self.elapd_time_label.grid(row=1, column=0, sticky="e")
        self.total_time_label.grid(row=1, column=1, sticky="w")

        self.callback = None
        self.scale.bind("<ButtonRelease-1>", self.move_slider)
        self.scale.bind("<B1-Motion>", self.move_slider)


    def set_elapd_time_text(self, timedelta_:timedelta):
        """ change elapd time text

        Args:
            timedelta_ (timedelta): [description]
        """
        time_text = str(timedelta_)
        self.elapd_time_label.configure(text=f"{time_text:15}/")


    def set_total_time(self, timedelta_:timedelta):
        """ change total time text

        Args:
            timedelta_ (timedelta): [description]
        """
        time_text = str(timedelta_)
        self.total_time_label.config(text=f"{time_text:15}")

        time_ms = int(timedelta_.total_seconds()*1e6)
        self.scale.configure(to_=time_ms)


    def update_value(self, timedelta_:timedelta):
        """ update self.var and elapd time text

        Args:
            timedelta_ (timedelta): [description]
        """
        time_s = timedelta_.total_seconds()
        time_ms = int(time_s * 1e6)
        self.scale.set(time_ms)
        self.set_elapd_time_text(timedelta_)

    
    def move_slider(self, *args):
        print(args)
        curr_var = self.var.get()
        self.update_value(timedelta(microseconds=curr_var))


if __name__ == "__main__":
    root = tk.Tk()
    scale = TimeScaleBar(root)
    scale.pack()
    time_d = timedelta(seconds=1234.5678)
    scale.set_total_time(time_d)

    def move(*args):
        print(args)

    root.mainloop()