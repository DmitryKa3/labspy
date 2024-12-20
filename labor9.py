import tkinter as tk
from tkinter import colorchooser

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canvas.create_oval(x1, y1, x2, y2, outline=current_color, fill=current_color, width=brush_size.get())

def change_color():
    global current_color
    _, color = colorchooser.askcolor()
    if color:
        current_color = color

root = tk.Tk()
root.title("Рисование с мышью")

brush_size = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL)
brush_size.pack()

color_button = tk.Button(root, text="Изменить цвет", command=change_color)
color_button.pack()

canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()
canvas.bind("<B1-Motion>", paint)

current_color = "black"

root.mainloop()
