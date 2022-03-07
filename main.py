
from cgitb import text
import math
import re
from tkinter import *
from turtle import title
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global my_timer
    global reps
    reps = 0
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    checkmark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Long Break")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Short Break")
    else:
        count_down(work_sec)
        label.config(text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds == 0:
        count_seconds = "00"
    elif count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    
    if count_minutes == 0:
        count_minutes = "00"
    elif count_minutes < 10:
        count_minutes = f"0{count_minutes}"
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        checkmark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
# window.minsize(width=500, height=500)
# window.maxsize(width=500, height=500)
window.config(padx=100, pady=50, bg=GREEN)

# width of canvas is a value in pixels
canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
# placing the image in the center of the canvas, by providing x and y values half of that of the canvas
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Verdana", 35, "bold"))
canvas.grid(column=1, row=1)
# count_down(5)


label = Label()
label.config(text="Timer", font=("Cambria", 25, "bold"), fg=YELLOW, bg=GREEN)
label.grid(column=1, row=0)

button_start = Button(text="Start")
button_start.config(highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset")
button_reset.grid(column=2, row=2)
button_reset.config(highlightthickness=0, command=reset_timer)

checkmark = Label(text="")
checkmark.grid(column=1, row=3)

window.mainloop()
