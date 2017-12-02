from tkinter import *
import seriLi
import fileprint
import threading
from tkinter import messagebox
import sys


def startprint(port):
    fileprint.startp(port)


def kent():

    root = Tk()
    root.geometry("480x360")

    menu = Menu(root)

    portarray = seriLi.serial_ports()

    root.config(menu=menu)
    subMenu = Menu(menu)
    #subMenut = Menu(menu)

    #menu.add_cascade(label="ملف", menu=subMenut)
    #subMenut.add_command(label='تخزين')
    #subMenut.add_command(label="ايقاف التخزين")

    menu.add_cascade(label="منفذ", menu=subMenu)

    for index in portarray:
        subMenu.add_command(label=index, command=lambda: startprint(index))

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
            sys.exit()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
    root.mainloop()


def caled():

    threadk = threading.Thread(target=kent)
    threadk.start()

