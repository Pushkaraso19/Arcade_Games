import tkinter
from tkinter import ttk
from tkinter.ttk import Button
from PIL import ImageTk, Image
import snakemain
import pongmain
import tcmain

root = tkinter.Tk()
root.title("Arcade Games")

width = 910
height = 450

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

root.geometry('%dx%d+%d+%d' % (width, height, x, y))

photo = ImageTk.PhotoImage(Image.open("icon.png"))
root.iconphoto(False, photo)

frame = ttk.Frame(root, padding=10)
root.config(bg="#2F2F2F")

def snake_call():
    """starts the snake game"""
    try:
        root.withdraw()
        snakemain.snake_main(root)
    except:
        pass

def pong_call():
    """starts the ping pong game"""
    try:
        root.withdraw()
        pongmain.pong_main(root)
    except:
        pass

def turtle_crossing_call():
    """starts the turtle crossing game"""
    try:
        root.withdraw()
        tcmain.turtle_crossing_main(root)
    except:
        pass


arcade_games_label = ttk.Label(root, text="ARCADE GAMES", background='#2F2F2F', foreground='white', font=("Arial", 20, "bold"))
arcade_games_label.grid(row=1000, column=20, padx=20, pady=20)

choice_label = tkinter.Label(root, text="Choose the games you want to play", background='#2F2F2F', foreground='white', font=("Arial", 16, "bold"))
choice_label.grid(row=1500, column=20, padx=20, pady=20)

snake_image = Image.open("snake_image.png")
ping_pong_image = Image.open("pingpong_image.png")
turtle_image = Image.open("turtle_image.png")

snake_image = snake_image.resize((200, 200))
ping_pong_image = ping_pong_image.resize((200, 200))
turtle_image = turtle_image.resize((200, 200))

snake_photo_image = ImageTk.PhotoImage(snake_image)
ping_pong_photo_image = ImageTk.PhotoImage(ping_pong_image)
turtle_photo_image = ImageTk.PhotoImage(turtle_image)

snake_button = Button(root, image=snake_photo_image, command=snake_call)
snake_button.grid(row=2000, column=10, padx=20, pady=20)

pong_button = ttk.Button(root, image=ping_pong_photo_image, command=pong_call)
pong_button.grid(row=2000, column=20, padx=20, pady=20)

turtle_crossing_button = ttk.Button(root, image=turtle_photo_image, command=turtle_crossing_call)
turtle_crossing_button.grid(row=2000, column=30, padx=20, pady=20)
root.mainloop()
