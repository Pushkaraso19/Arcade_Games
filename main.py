import tkinter
from tkinter import ttk
from tkinter.ttk import Button
from PIL import ImageTk, Image
import snakemain
import pongmain
import tcmain

root = tkinter.Tk()
root.title("Arcade Games")

width = 900
height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))

photo = ImageTk.PhotoImage(Image.open("icon.png"))
root.iconphoto(False, photo)

frame = ttk.Frame(root, padding=10)
root.config(bg="#2F2F2F")

def snake_call():
    root.withdraw()
    snakemain.snake_main(root)

def pong_call():
    root.withdraw()
    pongmain.pong_main(root)

def turtle_crossing_call():
    root.withdraw()
    tcmain.turtle_crossing_main(root)

snake_button = Button(root, text="Snake", command=snake_call)
snake_button.grid(row=0, column=0, padx=20, pady=20)

pong_button = ttk.Button(root, text="Ping Pong", command=pong_call)
pong_button.grid(row=10, column=10, padx=20, pady=20)

turtle_crossing_button = ttk.Button(root, text="Turtle Crossing", command=turtle_crossing_call)
turtle_crossing_button.grid(row=20, column=20, padx=20, pady=20)
root.mainloop()
