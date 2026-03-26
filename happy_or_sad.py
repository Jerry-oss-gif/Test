import tkinter as tk
from PIL import Image, ImageTk
import os
import pygame 

def center_window(win, width, height):
    # Get screen width and height
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # Calculate position x, y
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    win.geometry(f"{width}x{height}+{x}+{y}")

pygame.mixer.init()

window = tk.Tk()

window.title("Happy or Sad?")
center_window(window, 1080, 720)
main_icon = tk.PhotoImage(file=r"E:\D Computer\Python (pratice)\Tkinter\happy_or_sad\047b5491771ba7d54b33179e04164b22.PNG")
window.iconphoto(False, main_icon)

def happy():
    # Use Pillow to open the WEBP image
    image = Image.open(r"E:\D Computer\Python (pratice)\Tkinter\happy_or_sad\download.jpg")
    icon = ImageTk.PhotoImage(image)
    happy_window = tk.Toplevel(window)
    happy_window.title("Really Happy?")
    center_window(happy_window, 500, 300)
    happy_icon = tk.PhotoImage(file=r"E:\D Computer\Python (pratice)\Tkinter\happy_or_sad\98027-shiba-inu-doge-meme-photos.png")
    happy_window.iconphoto(False, happy_icon)

    happy_label = tk.Label(
        happy_window,
        image=icon,
        text="သူနဲ့အတူတူဆောက်ခဲ့တဲ့လေထဲကအိမ်လေးရော ? ",
        font=("pyidaung su", 15),
        fg="red",
        bg="black",
        compound=tk.BOTTOM
    )
    happy_label.image = icon  # keep a reference so it doesn’t get garbage-collected
    happy_label.pack(expand=True)
    pygame.mixer.music.load(r"E:\D Computer\Python (pratice)\Tkinter\happy_or_sad\Wink - Ya Par Tal (Raw).mp3")
    pygame.mixer.music.play(-1)  # -1 means loop forever

def sad():
     os.startfile(r"E:\D Computer\Python (pratice)\Tkinter\happy_or_sad\IMG_2744.MP4")

happy_btn = tk.Button(window, text="Happy", font=("Arial", 24), fg="white", bg="black", command=happy)
sad_btn = tk.Button(window, text="Sad", font=("Arial", 24), fg="white", bg="black", command=sad)

happy_btn.pack(side="bottom", expand=True)
sad_btn.pack(side="bottom", expand=True)

# Load JPEG using Pillow
image = Image.open(r"C:\Users\dartu\OneDrive\Desktop\Happy or sad.jpg")
photo = ImageTk.PhotoImage(image)

label = tk.Label(
    window,
    image=photo,
    text="Happy or Sad?",
    font=("Ink Free", 24),
    fg="white",
    bg="black",
    compound=tk.BOTTOM
)
label.pack()

window.mainloop()