import tkinter as tk
from tkinter import Message, Text
import cv2
import os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk

import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
from pathlib import Path
from tkinter import *

from PIL import Image, ImageTk

window = tk.Tk()
window.title("Sign_text_conversion")
window.configure(background='white')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
message = tk.Label(
    window, text="Sign_text_conversion",
    bg="green", fg="white", width=50,
    height=3, font=('times', 30, 'bold'))

message.place(x=200, y=20)

def open_camera():
    DATA_DIR = './data'
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    number_of_classes = 3
    dataset_size = 100



    cap = cv2.VideoCapture(0)
    for j in range(number_of_classes):
        if not os.path.exists(os.path.join(DATA_DIR, str(j))):
            os.makedirs(os.path.join(DATA_DIR, str(j)))

        print('Collecting data for class {}'.format(j))

        done = False
        while True:
            ret, frame = cap.read()
            cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                        cv2.LINE_AA)
            cv2.imshow('conversion', frame)
            if cv2.waitKey(25) == ord('q'):
                break

        counter = 0
        while counter < dataset_size:
            ret, frame = cap.read()
            cv2.imshow('frame', frame)
            cv2.waitKey(25)
            cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

            counter += 1

    cap.release()
    cv2.destroyAllWindows()

button1 = Button(window, text="Open Camera", command=open_camera)
button1.pack()

window.mainloop()