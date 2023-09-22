# 导入 GUI 库
import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("简单绘图应用")

# 创建一个画布
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# 定义鼠标点击事件处理函数
def on_canvas_click(event):
    x, y = event.x, event.y
    canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue")

# 使用事件钩子绑定鼠标点击事件处理函数
canvas.bind("<Button-1>", on_canvas_click)

# 运行 GUI 主循环
root.mainloop()
