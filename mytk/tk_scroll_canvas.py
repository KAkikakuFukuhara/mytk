import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.update_idletasks() # サイズ変更の更新

        # キャンバスの設定
        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.pack(side="left")
        self.canvas = tk.Canvas(self.canvas_frame, width=40, bg="white")
        self.canvas.grid(row=0, column=0)

        # スクロールバーの設定
        self.scrollbar = tk.Scrollbar(self.canvas_frame, orient="v", command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        
        # キャンバスの縦のサイズの更新
        self.canvas.config(height=self.winfo_height())
        
        # キャンバスにスクロールバーを反映
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        self.canvas.config(scrollregion=(0, 0, 0, 1000))

        # 図形の作成
        id0 = self.canvas.create_rectangle(0, 0, 40, 30, fill="black")
        id1 = self.canvas.create_rectangle(0, 30, 40, 60, fill="red")
        id2 = self.canvas.create_rectangle(0, 60, 40, 90, fill="blue")
        id3 = self.canvas.create_rectangle(0, 90, 40, 120, fill="green")
        id4 = self.canvas.create_rectangle(0, 120, 40, 150, fill="cyan")
        id5 = self.canvas.create_rectangle(0, 150, 40, 180, fill="magenta")

        # 図形へのイベントの設定
        self.canvas.tag_bind(id0, '<ButtonPress-1>', lambda event: print(event))
        self.canvas.tag_bind(id1, '<ButtonPress-1>', lambda event: print(event))

if __name__ == "__main__":
    app = App()
    app.mainloop()