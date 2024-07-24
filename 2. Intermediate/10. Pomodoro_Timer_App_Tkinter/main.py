from tkinter import *
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
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    minutes = str(int(count / 60))
    seconds = str(count % 60)
    if int(minutes) < 10:
        minutes = "0" + minutes
    if int(seconds) < 10:
        seconds = "0" + seconds
    time = minutes + ":" + seconds
    canvas.itemconfig(timer_text, text=time)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(reps // 2):
            mark += "✅"
        check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(text="", font=(FONT_NAME, 10, "bold"), bg=YELLOW)
check_mark.grid(row=3, column=1)

window.mainloop()
