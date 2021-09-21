from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK_MARK = "✔"
reps = 0
tick_add = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def timer_reset():
    title['text'] = 'Timer'
    tick.config(text="")
    global reps
    reps = 0

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def timer_start():
    global reps
    reps += 1

    work_min = WORK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_min)
        title['text'] = 'Work'

    elif reps % 2 == 0 and reps < 8:
        count_down(short_break)
        title['text'] = "Break"
        title['fg'] = YELLOW
    elif reps == 8:
        count_down(long_break)
        title['text'] = "Long Break"
        title['fg'] = YELLOW
    else:
        title['text'] = "Congratulations!"
        pass



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    minute = math.floor(count/60)
    second = count % 60

    if int(second) < 10:
        sec = second
        second = f"0{sec}"

    time_display = f"{minute}:{second}"
    canvas.itemconfig(timer_text, text=time_display)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        timer_start()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += TICK_MARK
        tick.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=100,bg=PINK)

title = Label(text='Timer', fg=GREEN, font=(FONT_NAME,50,'bold'), bg=PINK)
title.grid(row=0,column=1)
title.config(pady=20)

canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130 , text='00:00',fill='white',font=(FONT_NAME, 24, 'bold'))
canvas.grid(row=1,column=1)


start_butt = Button(text='Start',width=8,font=('Courier',8,'normal'),
                    highlightthickness=0, command=timer_start
)
start_butt.grid(row=2,column=0)


tick = Label(text=tick_add, bg=PINK, fg=GREEN)
tick.grid(row=2,column=1)
tick.config(pady=10)


reset_butt = Button(text='Reset',width=8,font=('Courier',8,'normal'),
                    command=timer_reset,highlightthickness=0
)
reset_butt.grid(row=2,column=2)

















window.mainloop()