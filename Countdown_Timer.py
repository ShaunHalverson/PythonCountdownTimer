import time
from tkinter import *
from tkinter import messagebox

### Create the interface object
clockWindow = Tk()
clockWindow.geometry("500x500")
clockWindow.title("Countdown Timer")
clockWindow.configure(background='orange')

### Declare variables
hourString = StringVar()
minuteString = StringVar()
secondString = StringVar()

### Set strings to default value
hourString.set("00")
minuteString.set("00")
secondString.set("00")

### Get user input
hourTextbox = Entry(clockWindow, width=3, font=("Calibri", 20, ""), textvariable=hourString)
minuteTextbox = Entry(clockWindow, width=3, font=("Calibri", 20, ""), textvariable=minuteString)
secondTextbox = Entry(clockWindow, width=3, font=("Calibri", 20, ""), textvariable=secondString)

### Center textboxes
hourTextbox.place(x=170, y=180)
minuteTextbox.place(x=220, y=180)
secondTextbox.place(x=270, y=180)

def runTimer():
    try:
        clockTime = int(hourString.get())*3600 + int(minuteString.get())*60 + int(secondString.get())
    except:
        print("Incorrect values")

    while(clockTime > -1):
        
        totalMinutes, totalSeconds = divmod(clockTime, 60)

        totalHours = 0
        if(totalMinutes > 60):
            totalHours, totalMinutes = divmod(totalMinutes, 60)

        hourString.set("{0:2d}".format(totalHours))
        minuteString.set("{0:2d}".format(totalMinutes))
        secondString.set("{0:2d}".format(totalSeconds))

        ### Update the interface
        clockWindow.update()
        time.sleep(1)

        ### Let the user know if the timer has expired
        if(clockTime == 0):
            messagebox.showinfo("", "Your time has expired!")

        clockTime -= 1


setTimeButton = Button(clockWindow, text='Set Time', bd='5', command=runTimer)
setTimeButton.place(relx=0.5, rely=0.5, anchor=CENTER)

### Keep looping
clockWindow.mainloop()
