# testing
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import *
import time
import os
import pygame

ms = 0
second = 0
minute = 0
hour = 0
stop = 0 
starts = 0
music = 0
    
loading=Tk()

location = os.getcwd()
width_of_window = 427
height_of_window = 250
screen_width = loading.winfo_screenwidth()
screen_height = loading.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
loading.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))


loading.overrideredirect(1)


s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress=Progressbar(loading,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)



def new_win():
    global location, ms, second, minute, hour, stop, starts, music
    stopwatch = Tk()
    stopwatch.title('Stopwatch')
    stopwatch.geometry('500x500')


    icon = PhotoImage(file=f'{location}\\bg.png')
    stopwatch.iconphoto(False, icon)
    stopwatch.config(background="#a0dfe6")


    photo = PhotoImage(file= f"{location}\\bg.png")

    pic = Canvas(stopwatch,
            width=500, 
            height=500,
            bg='black', 
            relief=RAISED, 
            bd=10,)

    pic.pack(padx=0,pady=0, 
        expand=True)  
    pic.create_image(0,0, 
        image = photo, 
        anchor = "nw",)
    pic.create_text(150,30, 
                text="4k03h L4n6 703H's Stopwatch", 
                font=("Arial", 14), 
                fill="white")


    # merv




    pygame.mixer.init()
    def start():
        global ms, second, minute, hour, stop, starts, music
        ms += 1
        if ms == 100:
            ms = 0
            second += 1
        elif second == 60:
            second = 0 
            minute += 1
        elif minute == 60:
            minute = 0
            hour += 1
        if stop == 0:
                    xms = f"0{ms}" if ms < 10 else f"{ms}"
                    xsecond = f"0{second}" if second < 10 else f"{second}"
                    xminute = f"0{minute}" if minute < 10 else f"{minute}"
                    xhour = f"0{hour}" if hour < 10 else f"{hour}"
                    TkText = Label(stopwatch, text= xhour +":"+xminute+":"+xsecond+":"+xms, font = ("Times 20"))
                    TkText.after(10, start)
                    TkText.place(x=95, y=111)

    def stop_watch():
        global stop
        stop = 1
        start_button['state'] = NORMAL
        pygame.mixer.music.pause()

    def reset_watch():
        global ms, second, minute, stop, music
        ms, second, minute, stop, start, music = 0, 0, 0, 1, 0, 0
        TkText = Label(stopwatch, text= "00:00:00:00", font = ("Times 20"))
        TkText.place(x=95, y=111)
        start_button['state'] = NORMAL
        pygame.mixer.music.stop()

    def continue_watch():
        global stop, music
        music += 1
        if music == 1:
            pygame.mixer.music.load(f"{location}\\SxF.mp3")
            pygame.mixer.music.play(loops = -1)
        elif music > 1:
            pygame.mixer.music.unpause()
        stop = 0
        start()
        start_button['state'] = DISABLED

    start_bttn = PhotoImage(file = f"{location}\\red.png")
    stop_bttn = PhotoImage(file = f"{location}\\stop.png")
    start_button = Button(stopwatch, image = start_bttn, command=continue_watch)
    start_button.place(x =113, y = 62)
    stop_button = Button(stopwatch, image = stop_bttn, command= stop_watch)
    stop_button.place(x=181, y = 63)
    reset_button = Button(stopwatch, text="Reset", command=reset_watch)
    reset_button.place(x=125, y = 150)
    # merv




    stopwatch.mainloop()




def run():

    l4=Label(loading,text='Loading...',fg='white',bg=a)
    lst4=('Calibri (Body)',10)
    l4.config(font=lst4)
    l4.place(x=18,y=210)
    
    
    r=0
    for i in range(100):
        progress['value']=r
        loading.update_idletasks()
        time.sleep(0.03)
        r=r+1
    
    loading.destroy()
    new_win()
        
    
progress.place(x=-10,y=235)

def exit():
    loading.destroy()
    

'''

def rgb(r):
    return "#%02x%02x%02x" % r
#Frame(w,width=432,height=241,bg=rgb((100,100,100))).
'''
a='#249794'

Frame(loading,width=427,height=241,bg=a,).place(x=0,y=0)  #249794
b1=Button(loading,width=10,height=1,text='Get Started',command=run,border=3,fg=a,bg='white')
b1.place(x=70,y=180)

b2=Button(loading,width=10,height=1,text='Exit',command=exit,border=3,fg=a,bg='white')
b2.place(x=270,y=180)


l1=Label(loading,text='4k03h L4n6 703H',fg='white',bg=a)
lst1=('Calibri (Body)',18,'bold')
l1.config(font=lst1)
l1.place(x=50,y=80)

'''
l2=Label(loading,text='SCREEN',fg='white',bg=a)
lst2=('Calibri (Body)',18)
l2.config(font=lst2)
l2.place(x=155,y=82)
'''

l3=Label(loading,text='STOPWATCH',fg='white',bg=a)
lst3=('Calibri (Body)',13)
l3.config(font=lst3)
l3.place(x=50,y=110)



loading.mainloop()