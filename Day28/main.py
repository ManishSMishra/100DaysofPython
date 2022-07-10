
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
reps=0
check=''
my_timer = None


def reset_timer():
    global reps
    window.after_cancel(my_timer)
    canvas.itemconfigure(my_text,text="00:00")
    timer_label.config(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
    reps=0


def start_action():
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN *60
    
    if reps%8==0:
        timer_label.config(text="Break",fg=RED)
        countdown(long_break_sec)
        
    elif reps%2==0:
        timer_label.config(text="Break",fg=PINK)
        countdown(short_break_sec)
    else:
        timer_label.config(text="Work",fg=GREEN)
        countdown(work_sec)
        
        


def countdown(count):
    global check
    global my_timer
    mins, secs = divmod(count, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    canvas.itemconfigure(my_text,text=timer)
    if count>0:
        my_timer=window.after(1000,countdown,count-1)
    else:
        start_action()
        if reps%2==0:
            check +='✔'
            check_label.config(text=check)
        
        



window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


# Canvas
canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
my_image=PhotoImage(file="Day28\\tomato.png")
canvas.create_image(100,112,image=my_image)
my_text=canvas.create_text(100,130,text="00:00",fill='white',font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

# Timer Label
timer_label = Label(text="Timer",font=(FONT_NAME,50,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(row=0,column=1)


# Check Label

check_label = Label(text=check,font=(FONT_NAME,20,"bold"),fg=GREEN,bg=YELLOW)
check_label.grid(row=3,column=1)
check_label.config(pady=7)

# Start Buttons




start_button = Button(text="Start", command=start_action,highlightthickness=0)
start_button.grid(row=2,column=0)
start_button.config(width=8)
# Reset Buttons






reset_button = Button(text="Reset", command=reset_timer,highlightthickness=0)
reset_button.grid(row=2,column=2)
reset_button.config(width=8)


window.mainloop()