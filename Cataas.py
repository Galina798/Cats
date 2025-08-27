from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image():



window = Tk()
window.title("Cats!")
window.geometry("600x480")

label = Label().pack()

url = "https://cataas.com/cat"
img = load_image(url)

if img:
    label.config(image=img)
    label.image = img

window.mainloop()


