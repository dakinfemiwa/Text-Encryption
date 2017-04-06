# Importing required modules:
import tkinter
from tkinter import *
import tkinter.ttk
from tkinter.ttk import *
import os
import shutil

# Importing custom "Tools" class:
import Tools

print(os.getcwd())

# / TO DO /
# To go to a certain area press CTRL + F
# and enter the REF number.
# Example: "#REF2"
# Will take you to the TO DO for the crash file.

# REF
# 1 - Move downloading status to the tkinter GUI.
# 2 - Save more detailed information about errors in a crash file.
# 3 - Obtain custom resolution from the configuration file.
# 4 - Obtain custom window title from the configuration file.

# Function for presenting the error message.
# Can be called from anywhere.
def errorMessage():
    error.pack()
    three = tkinter.Label(main, text="CLOSING IN 3...", fg="#FF0000", font="Arial 10 ", bg="#141414")
    two = tkinter.Label(main, text="CLOSING IN 2...", fg="#FF0000", font="Arial 10 ", bg="#141414")
    one = tkinter.Label(main, text="CLOSING IN 1...", fg="#FF0000", font="Arial 10 ", bg="#141414")
    main.after(2000, lambda: (three.pack()))
    main.after(3000, lambda: (three.pack_forget(), two.pack()))
    main.after(4000, lambda: (two.pack_forget(), one.pack()))
    main.after(5000, lambda: (main.destroy()))
    main.after(6000, lambda: (exit()))
    
# Main function for updating the weather program.
# Downloading status is printed to console.
# / TO DO / [#REF1] - Move to tkinter window.
def updateWeather():
    update.pack_forget()
    cancel = Button(main, text="CANCEL", command=lambda: main.destroy()).pack()
    blank2.pack()
    check.pack()
    print("Initiated check for update for weather program...")
    core = Tools.Main()
    if core.isUpdate() == True:
        main.after(1000, lambda: foundMessage())
        main.after(2000, lambda: versionMessage())
    elif core.isUpdate() == False:
        no.pack()
    else:
        errorMessage()
        
# If an update is found a message will be presented.
def foundMessage():
    yes.pack()

# Presenting the latest version number to the user.
# If there is an error in the process, errorMessage() is called.
# / TO DO / [#REF2] - Save more detailed information in a crash file.
def versionMessage():
    try:
        versions = open('Versions.txt', 'r+')
        lines = versions.readlines()
        current = str(lines[0].rstrip())
        latest = str(lines[1].lstrip())
        message = "LATEST VERSION IS " + latest
        latest = tkinter.Label(main, text=message, font="Arial 10", fg="#1E90FF", bg="#141414").pack()
        main.after(1000, lambda: removeMessage())
    except:
        errorMessage()

# Function for removing the current file to make place for the newest file.
# If there is an error in the process, errorMessage() is called.
def removeMessage():
    try:
        old = os.getcwd() + "\Old"
        shutil.move("Weather.py", old)
        main.after(0, lambda: (delete.pack(), addMessage()))
    except:
        errorMessage()

def addMessage():
    try:
        os.rename("Weather%20GUI%20NEA.py", "Update file.py")
        os.rename("Update file.py", "Weather.py")
        main.after(1000, lambda: replace.pack())
        main.after(2000, lambda: (rename.pack(), successMessage()))
    except:
        errorMessage()

def successMessage():
    try:
        main.after(1000, lambda: success.pack())
    except:
        errorMessage()
    
# Main 'Updater' window.
main = tkinter.Tk()
# / TO DO / [#REF3] - Get resolution from configuration file.
main.geometry("1300x720")
# / TO DO / [#REF4] - Get window title from configuration file.
main.title("Updater - SM")
main.configure(bg="#141414")

# Blank label, used multiple times to space other labels out.
blank = tkinter.Label(main, bg="#141414").pack()

blank = tkinter.Label(main, bg="#141414").pack()

blank = tkinter.Label(main, bg="#141414").pack()

# Main title and sub-title.
title = tkinter.Label(main, text="UPDATER", font="Arial 70 bold", bg="#141414", fg="#ffffff").pack()
subtitle = tkinter.Label(main, text="SELECT THE PROGRAM YOU WISH TO UPDATE", font="Arial 20 bold", bg="#141414", fg="#ffffff").pack()

blank = tkinter.Label(main, bg="#141414").pack()
blank = tkinter.Label(main, bg="#141414").pack()
blank = tkinter.Label(main, bg="#141414").pack()

weather = tkinter.Label(main, text="WEATHER PROGRAM", font="Arial 13 bold", bg="#141414", fg="#ffffff").pack()

blank1 = tkinter.Label(main, bg="#141414")

blank1.pack()

update = Button(main, text="UPDATE", command=lambda: (updateWeather(), blank1.pack_forget()))

update.pack()

blank = tkinter.Label(main, bg="#141414").pack()

yes = tkinter.Label(main, text="AN UPDATE WAS FOUND", font="Arial 10", fg="#7CFC00", bg="#141414")

blank = tkinter.Label(main, bg="#141414")

no = tkinter.Label(main, text="AN UPDATE WAS NOT FOUND", font="Arial 10", fg="#FF0000", bg="#141414")

blank = tkinter.Label(main, bg="#141414")

check = tkinter.Label(main, text="LOOKING FOR AN UPDATE...", font="Arial 10", fg="#FF8C00", bg="#141414")

blank = tkinter.Label(main, bg="#141414")

latest = tkinter.Label(main, text="LATEST VERSION IS 0.96", font="Arial 10", fg="#1E90FF", bg="#141414")

# go = tkinter.Label(main, text="WOULD YOU STILL LIKE TO CONTINUE?", font="Arial 10 bold", fg="#1E90FF", bg="#141414").pack()

# consent = Combobox(main, values=["Yes", "No"], width="20", state="readonly").pack()

delete = tkinter.Label(main, text="REMOVING CURRENT VERSION", font="Arial 10", fg="#FF0000", bg="#141414")

replace  = tkinter.Label(main, text="ADDING LATEST FILE", font="Arial 10", fg="#FF8C00", bg="#141414")

rename = tkinter.Label(main, text="RENAMING FILE", font="Arial 10", fg="#FF8C00", bg="#141414")

success = tkinter.Label(main, text="UPDATE WAS SUCCESSFUL", font="Arial 10", fg="#7CFC00", bg="#141414")

error = tkinter.Label(main, text="AN ERROR OCCURED", font="Arial 10", fg="#FF0000", bg="#141414")

blank2 = tkinter.Label(main, bg="#141414")
