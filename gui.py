import os
import tkinter
from tkinter import filedialog


def choose_file():
    window = tkinter.Tk()
    window.withdraw()
    window.geometry('300x300')
    directory_path = filedialog.askdirectory(initialdir=os.getcwd())
    return directory_path
