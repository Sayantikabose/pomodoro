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
reps=0
timer=NONE
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    window.after_cancel(timer)
    timer_label.config(text="TIMER", fg=GREEN, font=(FONT_NAME,30,"bold"))
    canvas.itemconfig(timer_text,text="00:00")
    checkmark.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def starttimer():  

    global reps 
    reps=reps+1 
    if (reps % 2 != 0 ):
        countdown(WORK_MIN*60) 
        timer_label.config(text="WORK", fg=GREEN)
        
    elif (reps%8==0): 
        countdown(LONG_BREAK_MIN*60)
        timer_label.config(text="BREAK", fg=RED)
        
    else :
        countdown(SHORT_BREAK_MIN*60)
        timer_label.config(text="BREAK", fg=RED)
        
        
    
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count): 
    global timer
    count_min=math.floor(count/60)
    countsec=count%60
    if countsec < 0:
        countsec=f"0{countsec}" 

    canvas.itemconfig(timer_text,text=f"{count_min}:{countsec}") 

    if count>0:
        timer = window.after(1000,countdown,count-1) 
    else:
        starttimer()
        mark=""
        work=math.floor(reps/2)
        for _ in range (work):
            mark+="✔" 
        checkmark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("POMODORO APP")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME,35,"bold"))

canvas.grid(row=1,column=1)

timer_label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,50,"bold"),bg=YELLOW)
timer_label.grid(row=0,column=1)

start_btn=Button(text="Start",highlightthickness=0,command=starttimer)
start_btn.grid(row=2,column=0)

reset_btn=Button(text="Reset",highlightthickness=0, command=reset_timer)
reset_btn.grid(row=2,column=2)


checkmark=Label(fg=GREEN,bg=YELLOW)
checkmark.grid(row=3,column=1)
window.mainloop()