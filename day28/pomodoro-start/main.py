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

reps = 0
timer = None  # after() id

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer
    if timer:  # sadece geçerli bir after id varsa iptal et
        window.after_cancel(timer)
        timer = None
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MEKANİĞİ ---------------------------- #
def start_timer():
    global reps, timer

    # Aynı anda birden fazla sayaç başlatmayı engelle
    if timer is not None:
        return

    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # YALNIZCA BİR KEZ count_down çağır
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN ------------------------------- #
def count_down(count):
    global timer, reps

    minutes, seconds = divmod(count, 60)
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        # Bu döngü bitti; yeni seansı başlat
        timer = None  # yeni after planlamadan önce temizle
        # Check mark'ları güncelle
        marks = "✅" * math.floor(reps / 2)
        check_marks.config(text=marks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", bg=YELLOW, fg="black",
                      highlightbackground=YELLOW, highlightthickness=0,
                      command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Restart", bg=YELLOW, fg="black",
                      highlightbackground=YELLOW, highlightthickness=0,
                      command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
