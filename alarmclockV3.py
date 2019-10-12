import sys
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import *
else:
    from tkinter import *
# import RPi.GPIO as GPIO
from datetime import datetime
import time

# Morning (6-8), Early (9-11), Day (12-4), Late(5-7), Evening(8-10), Night(11-5)
#      (6-8)         (9-11)       (12-16)   (17-19)        (20-22)     (23-5)
#  #707fd1         #5162c6       #3b4db1    #314091     #273270        #1d2450
 
root = Tk()
root.attributes('-fullscreen', True)
root.configure(background='#263238')


def getTimeAndDate():
	a = datetime.now()
	months=["January","February","March","April","May","June","July","August","September","October","November","December"]
	today=datetime.today()
	t = a.strftime("%I:%M")
	month = a.strftime(months[today.month-1])
	day = str(today.day)
	md = month + " " + day
	return (t, md)


while(True):
	a = datetime.now()
	(t, md) = getTimeAndDate()
	tHour = int(a.strftime("%H"))

	if tHour >= 6 and tHour <= 8:
		hrcolor = "#707fd1"
	elif tHour >= 9 and tHour <= 11:
		hrcolor = "#5162c6"
	elif tHour >= 12 and tHour <= 16:
		hrcolor = "#3b4db1"
	elif tHour >= 17 and tHour <= 19:
		hrcolor = "#314091"
	elif tHour >= 20 and tHour <= 22:
		hrcolor = "#273270"
	elif tHour == 23 or tHour == 24 or (tHour >= 0 and tHour <= 5):
		hrcolor = "#1d2450"
	root.configure(background=hrcolor)
	
	T= StringVar()
	MD= StringVar()
	T.set(t)
	MD.set(md)
	displayTime =  Label(root, textvariable=T, font=("Verdana",112), fg="#e6e6e6", bg=hrcolor)
	displayDay = Label(root, textvariable=MD, font=("Verdana",60), fg="#e6e6e6", bg=hrcolor)
	displayTime.pack()
	displayDay.pack()
	#displayTime.place(relx=0.5, rely=0.4, anchor='n')
	#displayDay.place(relx=0.5, rely=0.55, anchor='n')
	root.after(500, root.update())
	

		

