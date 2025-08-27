from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# список тегов
Allowed_tags = ['sleep', 'jump', 'fight', 'black', 'white', 'cute']

# функция загрузки фото с сайта
def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

# функция создания выпадающего списка тегов и открытия каждой картинки в отдельном окне
def tag_combobox_cats():
    tag = tag_combobox.get()
    url_tag = f"https://cataas.com/cat/{tag}" if tag else "https://cataas.com/cat"
    img = load_image(url_tag)

    if img:
        new_window = Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry("600x480")

        label = Label(new_window, image=img)
        label.pack()
        label.image = img

# функция открытия рандомных изображений котов в отдельных окнах
def random_cat():
    url = "https://cataas.com/cat"
    img = load_image(url)

    if img:
        new_window = Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry("600x480")

        label = Label(new_window, image=img)
        label.pack()
        label.image = img

# функция закрытия программы
def exit():
    window.destroy()

# создание интерфейса
window = Tk()
window.title("Cats!")
window.geometry("600x520")

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "Файл", menu = file_menu)
file_menu.add_command(label = "Загрузить фото по тегу", command = tag_combobox_cats)
file_menu.add_command(label = "Загрузить случайное фото", command = random_cat)
file_menu.add_separator()
file_menu.add_command(label = "Выход", command = exit)

url = "https://cataas.com/cat"

tag_label = Label(text = "Выбери тег")
tag_label.pack(pady = 5)

tag_combobox = ttk.Combobox(values = Allowed_tags)
tag_combobox.pack(pady = 5)

load_button = Button(text = "Загрузить по тегу", command = tag_combobox_cats)
load_button.pack(pady = 10)

random_button = Button(text = "Загрузить случайного котика", command = random_cat)
random_button.pack(pady = 5)

window.mainloop()


