# Version 4.0
# Importing...
import tkinter
from tkinter import *
import tkinter.ttk
from tkinter.ttk import *
import re
import time
import sys, os
import traceback
import smTools

# | S.M 10 WILLIAM - COMPUTER SCIENCE | #
# Weather program @ Version 0.93

# // TO DO //
# REF 1 - Data window
# REF 2 - Drones
# REF 3 - Restart upon crash
# REF 4! - Averages - DONE!
# REF 5! - Use config - DONE!
# - Complete print method for all data-types. 2/3
# - CLEAN UP CODE.

# !! KNOWN BUGS !!
# REF 1b - If starting time is XX:30 30 is added to make XX:60 ✘
# fix this by checking if the starting time contrains ":30" ✔ <- DONE/FIXED
# REF 2b - If starting time is 10:00 then number is printed as 01:000 ✘
# fix this by using a different equation when increasing time. ✔ <- DONE/FIXED
# If the weather is "5.5" it is displayed as being "5" as it uses an integer.
# fix this by changing the display number to a float.

# == DEVELOPER MODE ==
# Developer mode allows you to see more real-time error messages.
# Instead of only presenting the error at the end, it will tell you beforehand whether the program will work.
# 

# -- BLACKLISTED COMMANDS --
# DEVELOPER MODE
# CUSTOM (DATA-TYPE)

# [][] UPDATES [][]
# - Started function to download missing files.
# - Added custom messages which can be editted from 'messages.txt'.
# - Fixed repeated error messages.

# ** PROGRAM REQUIREMENTS **
# The following are required for the program to run:
# config.txt
# messages.txt
# crash.txt
# Monday.txt
# Tuesday.txt
# Wednesday.txt
# Thursday.txt
# Friday.txt
# Background Yellow.png

# Function to exit the program.
def exitProgram():
        try:
            ready = False
            # Trying to destroy the first window.
            try:
                weather.destroy()
                weatherMenu()
                ready = True
                # If developer mode is enabled.
                if USING_DEV_MODE == True:
                    # Using the custom print method.
                    cprint(PREFIX + ' - ' + 'Developer -' + ' ' + 'Tried to destroy window one (passed)', 79)
            except:
                if USING_DEV_MODE == True:
                    cprint(PREFIX + ' - ' + 'Developer -' + ' ' + 'Tried to do destroy window one (failed)', 79)
            # Trying to destroy the second window.
            try:
                weather2.destroy()
                weatherMenu()
                ready = True
                if USING_DEV_MODE == True:
                    cprint(PREFIX + ' - ' + 'Developer -' + ' ' + 'Tried to destroy window two (passed)', 79)
            except:
                if USING_DEV_MODE == True:
                    cprint(PREFIX + ' - ' + 'Developer -' + ' ' + 'Tried to do destroy window two (failed)', 79)
            # Trying to destroy the third window.
            try:
                weather3.destroy()
                weatherMenu()
                ready = True
                if USING_DEV_MODE == True:
                    cprint(PREFIX + ' - ' + 'Developer -' + ' ' + 'Tried to destroy window three (passed)', 79)
            except:
                if USING_DEV_MODE == True:
                    cprint(PREFIX + ' - ' + 'Developer -' + ' ' + 'Tried to do destroy window three (failed)', 79)
            # Closing the program after 3 seconds.
            # If we're ready to do so.
            if ready == True:
                cprint("Closing program in 3 seconds...", 79)
                time.sleep(1)
                cprint("Closing program in 2 seconds...", 79)
                time.sleep(1)
                cprint("Closing program in 1 second...", 79)
                time.sleep(1)
                exit()
        except:
            exit()

# Function to restart the program.
def restartProgram():
    # Trying to destroy the first window.
    try:
        weather.destroy()
        weatherMenu()
        cprint(PREFIX + ' ' + "Successfully restarted the program!", 79)
        if USING_DEV_MODE == True:
            cprint(PREFIX + ' - ' + 'Developer -' + ' ' + 'Tried to destroy window one and launch window one (passed)', 79)
    except:
        if USING_DEV_MODE == True:
            cprint(PREFIX + ' - ' + 'Developer -' + ' ' + 'Tried to do destroy window one (failed)', 79)
    # Trying to destroy the second window.
    try:
        weather2.destroy()
        weatherMenu()
        if USING_DEV_MODE == True:
            cprint(PREFIX + ' - ' + 'Developer -' + ' ' + 'Tried to destroy window two and launch window one (passed)', 79)
    except:
        if USING_DEV_MODE == True:
            cprint(PREFIX + ' - ' + 'Developer -' + ' ' + 'Tried to do destroy window two (failed)', 79)
    # Trying to destroy the third window.
    try:
        weather3.destroy()
        weatherMenu()
        if USING_DEV_MODE == True:
            cprint(PREFIX + ' - ' + 'Developer -' + ' ' + 'Tried to destroy window three and launch window one (passed)', 79)
    except:
        if USING_DEV_MODE == True:
            cprint(PREFIX + ' - ' + 'Developer -' + ' ' + 'Tried to do destroy window three (failed)', 79)

def errorWindow(error):
    if error == 'MISSING_CONFIG':
        fatal = 'Y'
        emessage = 'The configuration file (config.txt) could not be found or opened.'
        emessage_ = 'The program cannot be launched.'
    if error == 'MISSING_MESSAGES':
        fatal = 'N'
        emessage = 'The messages file (messages.txt) could not be found or opened.'
        emessage_ = 'The program can still be launched but default messages will be used, continue?'
    if error == 'MISSING_DATA':
        fatal = 'N'
        emessage = 'The data could not be retrieved for some/all days.'
        emessage_ = 'The program can still be launched but some data may not be presentable.'
    if error == 'MISSING_BACKGROUND':
        fatal = 'Y'
        emessage = 'The background image (Background Yellow.png) could not be loaded.'
        emessage_ = 'The program will not run untill the error is fixed.'
    if error == 'FILE_OPEN':
        fatal = 'N'
        emessage = 'A file could not be opened.'
        emessage_ = 'Restart program?'
    if error == 'WINDOW_LOAD':
        fatal = 'Y'
        emessage = 'A GUI window could not be loaded.'
        emessage_ = 'The program cannot be launched.'
    error_w = Tk()
    error_w.configure(bg="lightgray")
    error_w.geometry('450x200')
    error_w.title("ERROR" + ' ' + "(" + error + ")")
    error_w.wm_iconbitmap('error.ico')
    lb = tkinter.Label(error_w, bg="lightgray").pack()
    l = tkinter.Label(error_w, text="ERROR", font="Arial 15 bold", bg="lightgray").pack()
    l2 = tkinter.Label(error_w, text=emessage, bg="lightgray").pack()
    l3 = tkinter.Label(error_w, text=emessage_, bg="lightgray").pack()
    lb2 = tkinter.Label(error_w, bg="lightgray").pack()
    lb3 = tkinter.Label(error_w, bg="lightgray").pack()
    if fatal == 'N':
        b = Button(error_w, text="OK", command=lambda: restartProgram()).pack()
    elif fatal == 'Y':
        b = Button(error_w, text="OK", command=lambda: exitProgram()).pack()
    error_w.mainloop()
    # f = tkinter.Frame(error_w, bg="white")
    # f.grid(row=2, column=0)
    # l4 = tkinter.Label(f, text="Test")
    # l4.grid(row=0, column=0)

def downloadFile(file):
        file = file
        # Links for other files:
        Monday = "https://www.dropbox.com/s/k613j09s6rr4dhm/Monday.txt"
        Tuesday = "https://www.dropbox.com/s/40ygkktioozil64/Tuesday.txt"
        Wednesday = "https://www.dropbox.com/s/eqeplcf922yjuou/Wednesday.txt"
        Thursday = "https://www.dropbox.com/s/nnw0y08almr285x/Thursday.txt"
        Friday = "https://www.dropbox.com/s/zc9yhblrcc34qqx/Friday.txt" 
        Messages = "https://www.dropbox.com/s/ifie1oaxb9ovu7l/Messages.txt"
        Crash = "https://www.dropbox.com/s/a2h2ddsxdno1yvn/Crash.txt"
        Config = "https://www.dropbox.com/s/k48yn96cwpnqviw/Config.txt"
        Icon = "https://www.dropbox.com/s/flx0jd8mdgmpkrh/logo.ico"
        Error = "https://www.dropbox.com/s/2ey8e61g2j3zieb/error.ico"

        if file == "Monday":
                file = "Monday.txt"
                file = "https://dl.dropboxusercontent.com/s/k613j09s6rr4dhm/Monday.txt"
                size = 313
        if file == "Tuesday":
                file = "Tuesday.txt"
                file = "https://dl.dropboxusercontent.com/s/40ygkktioozil64/Tuesday.txt"
                size = 313
        if file == "Wednesday":
                file = "Wednesday.txt"
                file = "https://dl.dropboxusercontent.com/s/eqeplcf922yjuou/Wednesday.txt"
                size = 313
        if file == "Thursday":
                file = "Thursday.txt"
                file = "https://dl.dropboxusercontent.com/s/nnw0y08almr285x/Thursday.txt"
                size = 313
        if file == "Friday":
                file = "Friday.txt"
                file = "https://dl.dropboxusercontent.com/s/zc9yhblrcc34qqx/Friday.txt"
                size = 313
        if file == "Messages":
                file = "Messages.txt"
                file = "https://dl.dropboxusercontent.com/s/ifie1oaxb9ovu7l/Messages.txt"
                size = 1048
        if file == "Crash":
                file = "Crash.txt"
                file = "https://dl.dropboxusercontent.com/s/a2h2ddsxdno1yvn/Crash.txt"
                size = 3934
        if file == "Config":
                file = "Config.txt"
                file = "https://dl.dropboxusercontent.com/s/k48yn96cwpnqviw/Config.txt"
                size = 455
        if file == "logo":
                file = "logo.ico"
                file = "https://dl.dropboxusercontent.com/s/flx0jd8mdgmpkrh/logo.ico"
                size = 215486
        if file == "error":
                file = "error.ico"
                file = "https://dl.dropboxusercontent.com/s/2ey8e61g2j3zieb/error.ico"
                size = 67646
        if file == "Background":
                file = "Background Yellow.png"
                file = "https://dl.dropboxusercontent.com/s/e9xs3juigxmaxji/Background%20Yellow.png"
                size = 2647
        else:
                print("Invalid file name.")

        # Downloading the file...
        main = smTools.Main()
        # main.Download("https://www.dropbox.com/s/e9xs3juigxmaxji/Background%20Yellow.png", 220752)
        main.Download(file, size)

        # Re-naming the file...
        try:
            for filename in os.listdir("."):
                if filename.startswith("Background"):
                    os.rename(filename, file)
                    print("File renamed successfully!")
                    done = 1
        # If the file already exists.
        except FileExistsError:
            try:
                if done == 0:
                    print("The file:", file, "already exists!")
            except:
                pass
        # If any other error occurs.
        except Exception as e:
            print(e.__class__.__name__)
            print("Could not rename file.")


# Checking if required files exist.
required = True
if required == True:
    delay = .5
    print("Checking requirements...")
    try:
        print("Trying to open config.txt...")
        file = open('Config.txt', 'r+')
        file.close()
        time.sleep(delay)
        print("OK - Configuration file was loaded successfully.")
        time.sleep(delay)
    except:
        time.sleep(delay)
        print("FATAL - Configuration file could not be loaded.")
        time.sleep(delay)
        downloadFile("Config")
    try:
        print("Trying to open messages.txt...")
        file = open('messages.txt', 'r+')
        file.close()
        time.sleep(delay)
        print("OK - Custom messages file was loaded successfully.")
        time.sleep(delay)
    except:
        time.sleep(delay)
        print("FATAL - Custom messages file could not be loaded.")
        time.sleep(delay)
        downloadFile("Messages")
    try:
        print("Trying to open Monday-Friday.txt...")
        file = open('Monday.txt', 'r+')
        file.close()
        file = open('Tuesday.txt', 'r+')
        file.close()
        file = open('Wednesday.txt', 'r+')
        file.close()
        file = open('Thursday.txt', 'r+')
        file.close()
        file = open('Friday.txt', 'r+')
        file.close()
        time.sleep(delay)
        print("OK - All data files were loaded successfully.")
        time.sleep(delay)
    except:
        time.sleep(delay)
        print("FATAL - Some data files could not be loaded.")
        time.sleep(delay)
    try:
        print("Trying to open Background Yellow.png...")
        file = open("Background Yellow.png", 'r')
        time.sleep(delay)
        print("OK - Background image was loaded successfully.")
        time.sleep(delay)
    except:
        time.sleep(delay)
        print("FATAL - Could not load background image.")
        downloadFile("Background")
        time.sleep(delay)
    try:
        print("Trying to open crash.txt...")
        file = open("crash.txt", 'r')
        time.sleep(delay)
        print("OK - Crash file was loaded successfully.")
        time.sleep(delay)
    except:
        time.sleep(delay)
        print("FATAL - Could not load crash file.")
        time.sleep(delay)
        downloadFile("Crash")
try:
    if fatal_background:
        print("")
        print("Program cannot be launched with background image missing.")
        print("")
        errorWindow('MISSING_BACKGROUND')
        time.sleep(1)
except:
    pass

# || RETRIEVING MESSAGES ||
# Opening the custom messages file.
messages = open('messages.txt', 'r+')
# Reading all the lines.
mline = messages.readlines()
# Looking for "true" (true/false boolean)
if 'true' in mline[7]:
    cmsg = True
# If custom messages are going to be used.
if cmsg == True:
    # Welcome message.
    WELCOME_MSG_E = mline[9]
    # Title of GUI window.
    WINDOW_TITLE_E = mline[11]
    # Main prefix.
    PREFIX_E = mline[13]
    # Prefix for errors.
    ERROR_PREFIX_E = mline[15]
    # Crash messages.
    CRASH_MESSAGE_E = mline[17]
    # Error message for not being able to retrieve the data.
    ERROR_DATA_RETRIEVE_E = mline[19]
    # Error message for not being able to view the data.
    ERROR_DATA_PRESENT_E = mline[21]
    # Error message for not being able to present the GUI window.
    ERROR_WINDOW_LOAD_E = mline[23]
    # Error message for unknown errors.
    ERROR_UNKNOWN_E = mline[25]
    # Error message for the time being unlogical.
    ERROR_TIME_E = mline[27]
    # Error message for a feature has not been created yet.
    ERROR_DEV_E = mline[29]
    # Restart message.
    RESTART_E = mline[31]
    # Warning message.
    WARNING_CONFIG_E = mline[33]
    # Developer message prefix.
    DEV_PREFIX = mline[35]

    # Stripping what we don't need.
    WELCOME_MSG = WELCOME_MSG_E.replace('WELCOME_MSG: ', '')
    WINDOW_TITLE = WINDOW_TITLE_E.replace('WINDOW_TITLE: ', '')
    PREFIX = PREFIX_E.replace('PREFIX: ', '')
    ERROR_PREFIX = ERROR_PREFIX_E.replace('ERROR_PREFIX: ', '')
    CRASH_MESSAGE = CRASH_MESSAGE_E.replace('CRASH_MESSAGE: ', '')
    ERROR_DATA_RETRIEVE = ERROR_DATA_RETRIEVE_E.replace('ERROR_DATA_RETRIEVE: ', '')
    ERROR_DATA_PRESENT = ERROR_DATA_PRESENT_E.replace('ERROR_DATA_PRESENT: ', '')
    ERROR_WINDOW_LOAD = ERROR_WINDOW_LOAD_E.replace('ERROR_WINDOW_LOAD: ', '')
    ERROR_UNKNOWN = ERROR_UNKNOWN_E.replace('ERROR_UNKNOWN: ', '')
    ERROR_TIME = ERROR_TIME_E.replace('ERROR_TIME: ', '')
    ERROR_DEV = ERROR_DEV_E.replace('ERROR_DEV: ', '')
    RESTART = RESTART_E.replace('RESTART: ', '')
    WARNING_CONFIG = WARNING_CONFIG_E.replace('WARNING_CONFIG: ', '')
    DEV_PREFIX = DEV_PREFIX.replace('DEV_PREFIX: ', '')

    # Stripping just the right side of the string.
    WELCOME_MSG = WELCOME_MSG.rstrip()
    WINDOW_TITLE = WINDOW_TITLE.rstrip()
    PREFIX  = PREFIX .rstrip()
    ERROR_PREFIX = ERROR_PREFIX.rstrip()
    CRASH_MESSAGE = CRASH_MESSAGE.rstrip()
    ERROR_DATA_RETRIEVE = ERROR_DATA_RETRIEVE.rstrip()
    ERROR_DATA_PRESENT = ERROR_DATA_PRESENT.rstrip()
    ERROR_WINDOW_LOAD = ERROR_WINDOW_LOAD.rstrip()
    ERROR_UNKNOWN = ERROR_UNKNOWN.rstrip()
    ERROR_TIME = ERROR_TIME.rstrip()
    ERROR_DEV = ERROR_DEV.rstrip()
    RESTART = RESTART.rstrip()
    WARNING_CONFIG = WARNING_CONFIG.rstrip()
    DEV_PREFIX = DEV_PREFIX.rstrip()

    # Stripping the ""
    WELCOME_MSG = WELCOME_MSG.strip('\"')
    WINDOW_TITLE = WINDOW_TITLE.strip('\"')
    PREFIX = PREFIX.strip('\"')
    ERROR_PREFIX = ERROR_PREFIX.strip('\"')
    CRASH_MESSAGE = CRASH_MESSAGE.strip('\"')
    ERROR_DATA_RETRIEVE = ERROR_DATA_RETRIEVE.strip('\"')
    ERROR_DATA_PRESENT = ERROR_DATA_PRESENT.strip('\"')
    ERROR_WINDOW_LOAD = ERROR_WINDOW_LOAD.strip('\"')
    ERROR_UNKNOWN = ERROR_UNKNOWN.strip('\"')
    ERROR_TIME = ERROR_TIME.strip('\"')
    ERROR_DEV = ERROR_DEV.strip('\"')
    RESTART = RESTART.strip('\"')
    WARNING_CONFIG = WARNING_CONFIG.strip('\"')
    DEV_PREFIX = DEV_PREFIX.strip('\"')

# ~~ CUSTOM CONFIG ~~
# Opening the config file.
try: 
    cfg = open('Config.txt', 'r+')
    li = cfg.readlines()
    cfg_next = True
    
# If no config file exists.
except FileNotFoundError:
    print("_" * 70, "\n")
    print(PREFIX + ' ' + WARNING_CONFIG)
    print("_" * 70)
    cfg_next = False
    
# If another error occurs (IndexError?)
except:
    print("_" * 70, "\n")
    print(PREFIX + ' ' + ERROR_UNKNOWN)
    print("_" * 70)
    cfg_next = False

# Opening settings from config file.
if cfg_next == True:
    if 'true' in li[1]:
        use_cfg = True
    elif 'false' in li[1]:
        use_cfg = False
    else:
        print("Tried looking for true/false @", li[1])
        print("Could not find, assuming custom config will not be used.")
        use_cfg = False
    if use_cfg == True:
        # Getting the resolution for all windows.
        RESOLUTION = li[4].rstrip()
        RESOLUTION = RESOLUTION.strip("resolution: ")
        RESOLUTION = str(RESOLUTION)
        # Checking for true/false on crash restart.
        if 'true' in li[13]:
            CRASH_RESTART = True
            CRASH_RESTART_C = "Yes"
        else:
            CRASH_RESTART = False
            CRASH_RESTART_C = "No"
        # Checking for true/false for forced developer mode.
        if 'true' in li[10]:
            FORCE_DEV_MODE = True
            USING_DEV_MODE = True
            FORCE_DEV_C = "Yes"
        else:
            FORCE_DEV_MODE = False
            FORCE_DEV_C = "No"
        # Checking for true/false for developer mode.
        if 'true' in li[7]:
            DEV_MODE = True
            DEV_MODE_C = "Yes"
        else:
            DEV_MODE = False
            DEV_MODE_C = "No"
    # If custom config will not be used.
    if use_cfg == False:
        # Default configuration setttings.
        RESOLUTION = "1300x720"
        DEV_MODE = True
        FORCE_DEV_MODE = False
        CRASH_RESTART = False
        DEV_MODE_C = "Yes"
        FORCE_DEV_C = "No"
        CRASH_RESTART_C = "No"
        
# Printing the current configuration settings.
print("")
print("Current config: ")
print("Resolution: " + RESOLUTION)
print("Developer mode option: " + DEV_MODE_C)
print("Force developer mode: " + FORCE_DEV_C)
print("Restart on crash: " + CRASH_RESTART_C)
        
# Temporary developer mode (on).
# Remove in final version.
USING_DEV_MODE = True

# Setting the attempt variable.
# Used when the program crashes multiple times.
attempt = 0

# Custom print method/design.
def cprint(str, int):
    print("")
    print("_" * int, "\n")
    print(str)
    print("_" * int)
    # Example:
    # cprint("Hello!", 30)
    # Will be printed as:
    # ______________________________
    #
    # Hello!
    # ______________________________
    # Maybe add a centering option?
    # This can be done using len(str)

        
# Function used to save crash messages.
def saveCrash(error="N/A", line="N/A", source="N/A", info="N/A"):
    try:
        # Opening the crash file.
        line = str(line)
        file = open('crash.txt', 'r+')
        # Getting the lines.
        lines = file.readlines()
        # Writing all details of the crash to the file.
        file.write("_" * 70)
        file.write("\n")
        file.write("")
        file.write("\n")
        # Writing the time.
        file.write("Time: ")
        file.write(time.strftime("%H:%M:%S"))
        file.write("\n")
        # Writing the date.
        file.write("Date: ")
        file.write(time.strftime("%d/%m/%Y"))
        file.write("\n")
        # Writing the name of the error.
        file.write("Error: ")
        file.write(error)
        file.write("\n")
        # Writing the line number of where the error occured.
        file.write("Line: ")
        file.write(line)
        file.write("\n")
        # Writing the source of the error.
        file.write("Source: ")
        file.write(source)
        file.write("\n")
        # Writing more information about the error.
        file.write("Information: ")
        file.write(info)
        file.write("\n")
        file.write("_" * 70)
        file.write("\n")
        file.close()
    # If saving crash information fails (file cannot be opened)
    except:
        print("_" * 70, "\n")
        # Add custom message here.
        print(PREFIX + " " + "Could not save crash information.")
        print("_" * 70)

# Array for days, used in drop down menu.
days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
    ]

# Array for data-type, used in drop down menu.
type = [
    "Average",
    "All"
    # "Custom" - Removed
    ]

# Array for starting time, used in drop down menu.
starting = [
    "08:00",
    "08:30",
    "09:00",
    "09:30",
    ]

# Array for ending time, used in drop down menu.
ending = [
    "08:30",
    "09:00",
    "09:30",
    "10:00"
    ]

# Clears any old logs in console.
print(" " * 5000)

# ✔ Day
# ✔ Data-type
# ✔ Starting time
# ✔ Ending time
# Prints the data to the user via console.
# // TO DO // .. Show the data in the tkinter window. # REF 1
def viewWeatherFull(day, type, st, et):
    global flast
    flast = et
    global dtype
    dtype = type
    global dayz
    dayz = day
    # Print all of the users options.
    print()
    print("_" * 70, "\n")
    print("Day:", day)
    print("Type:", type)
    print("Starting Time:", st)
    print("Ending Time:", et)
    print("_" * 70)
    # Remove the colon so it can be found in the file.
    first_time = st.replace(":", "")
    last_time = et.replace(":", "")
    # Checking the start and end time gap.
    # Data will be retrieved using getData(st, q)
    if first_time == "0800":
        if last_time == "0830":
            # Using the getData(st, q) function.
            getData("08:00", 1)
        if last_time == "0900":
            getData("08:00", 2)
        if last_time == "0930":
            getData("08:00", 3)
        if last_time == "1000":
            getData("08:00", 4)
    if first_time == "0830":
        if last_time == "0900":
            getData("08:30", 1)
        if last_time == "0930":
            getData("08:30", 2)
        if last_time == "1000":
            getData("08:30", 3)
        else:
            # Check if the starting time is later than the ending time.
            print("_" * 70, "\n")
            # If it is, then an error message is printed.
            print(ERROR_PREFIX + ' ' + ERROR_TIME)
            print("_" * 70)
    if first_time == "0900":
        if last_time == "0930":
            getData("09:00", 1)
        if last_time == "1000":
            getData("09:00", 2)
        else:
            print("_" * 70, "\n")
            print(ERROR_PREFIX + ' ' +  ERROR_TIME)
            print("_" * 70)
    if first_time == "0930":
        if last_time == "1000":
            getData("09:30", 1)
        else:
            print("_" * 70, "\n")
            print(ERROR_PREFIX + ' ' +  ERROR_TIME)
            print("_" * 70)
    # Open the file for the day containing the data.
    # // TO DO // .. Add drones to carry more data. # REF 2
    try:
        # Getting the data by using the time as a base number.
        # The numbers can be added or subtracted from.
        # This is to read the data from the other lines.
        # The time will be the only unique value. (location?)
        with open(day + '.txt') as myFile:
            for num, line in enumerate(myFile, 1):
                if first_time in line:
                    # Test code - removed.
                    # print("_" * 40, "\n")
                    # print('[LOG] - Line number for', num)
                    # print("_" * 40)
                    numz = int(num)
                    break
        with open(day + '.txt') as myFile:
            for num, line in enumerate(myFile, 1):
                if last_time in line:
                    # Test code - removed.
                    # print("_" * 40, "\n")
                    # print('[LOG] - Line number for', num)
                    # print("_" * 40)
                    numz = int(num)
                    break
        # Opening data file.
        f = open(day + '.txt', 'r+')
        # Getting the temperature.
        line2 = f.readlines()
        temp = line2[numz]
        temp2 = int(re.search(r'\d+', temp).group())
        temp2 = str(temp2)
        temp_f = str(temp2 + "°C")
        # Getting the wind speed.
        wind = line2[numz + 1]
        wind2 = int(re.search(r'\d+', wind).group())
        wind2 = str(wind2)
        wind_f = str(wind2)
        # Getting the location.
        loc = line2[numz + 2]
        loc2 = int(re.search(r'\d+', loc).group())
        loc2 = str(loc2)
        loc_f = str(loc2)
        # Printing the data to the user.

        # The printing method was moved to getData()
        # This is to deal with all/averages easily.
        # Not using the one-line presenting method (see below).

        # __________________________________________________
        #
        # MOVED TO getData()
        # __________________________________________________
        #

        # Alternative presenting method:
        # // ->>>>>> print("The temperature for", day, "at", st, "was", temp_f, "with a wind speed of", wind_f + "mph.") (use/remove?)

        # __________________________________________________
        #
        # MOVED TO getData()
        # __________________________________________________
        #
        
    # If data for a certain is missing, an error will be printed.
    # // TO DO // .. Restart program or take user back. # REF 3
    # DONE! Using the restartProgram() method.
    except FileNotFoundError:
        print("_" * 70, "\n")
        print(ERROR_PREFIX + ' ' + ERROR_DATA_RETRIEVE + day)
        print("_" * 70)
        restartProgram()
    # If a different error occurs then crash information will be saved to a file.
    except Exception as e:
        # Error, line, source, info.
        cprint(CORE + ' ' + CRASH_MESSAGE, 70)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        e_line = exc_traceback.tb_lineno
        e_name = exc_traceback.tb_frame.f_code.co_name
        e_info = traceback._some_str(exception)
        e_error = exc_type.__name__
        saveCrash(error=e_error, line=e_line, source=e_name, info=e_info)
        cprint(PREFIX + ' ' + 'Crash log was saved successfully!', 79)

# ✔ Day
# ✔ Data-type
# ✘ Starting time
# ✘ Ending time
def viewWeatherType(day, type):
    # Making the window global so it can be closed from other functions.
    global weather3
    # Printing developer-exclusive errors.
    try:
        deverror1 = deverror
        if USING_DEV_MODE == True:
            if type == "Custom":
                deverror1 += 1
                deverror1 = str(deverror1)
                print("_" * 70, "\n")
                print("DEVELOPER - Custom data type has not been created!")
                print("Still continuing... " + "[" + deverror1 + "]")
                print("Program will not display any data.")
                print("_" * 70)
                deverror1 = int(deverror1)
    except:
        pass
    try:
        weather2.destroy()
        
    except:
        pass
    
    # Creating the third weather window.
    weather3 = Tk()
    weather3.geometry(RESOLUTION)
    weather3.title(WINDOW_TITLE)
    weather3.wm_iconbitmap('logo.ico')

    # Setting the background image.
    myImage3 = PhotoImage(file='Background Yellow.png')
    label = Label(image=myImage3)
    label.grid(row=0)
    label.image = myImage3
    
    # Creating the Frame for all the widgets.
    labelFrame = Frame(weather3)
    labelFrame.grid(row=0,column=1)

    # Variable key:
    # Button / bu
    # Label / l
    # Blank label / l_blank
    # Drop down box / om
    # Button (BACK/NEXT) / b
    
    # Creating all the widgets and adding them to the grid.
    l1 = Label(labelFrame, text="Weather", font="Arial 85 bold",  anchor="w")
    l1.grid(row=0, column=0)
    l2 = Label(labelFrame, text="  Please select a time period to continue", font="Arial 12 bold")
    l2.grid(row=1, column=0, sticky="w")
    l3_blank = Label(labelFrame, text="", anchor="e")
    l3_blank.grid(row=2, column=0)
    l3 = Label(labelFrame, text="  STARTING TIME", font="Arial 12 bold", anchor="w", foreground="lightyellow")
    l3.grid(row=3, column=0, sticky="w")

    # Creating the drop down box.
    om = Combobox(labelFrame, values=starting, width="39", state="readonly")
    om.set("08:00")
    om.grid(row=5, column=0, sticky="w")

    # Creating all the widgets and adding them to the grid
    l3_5_blank = Label(labelFrame, text="", anchor="e")
    l3_5_blank.grid(row=6, column=0)
    l4 = Label(labelFrame, text="  ENDING TIME", font="Arial 12 bold", anchor="w", foreground="lightyellow")
    l4.grid(row=7, column=0, sticky="w")

    # Creating the drop down box.
    om2 = Combobox(labelFrame, values=ending, width="39", state="readonly")
    om2.set("08:30")
    om2.grid(row=9, column=0, sticky="w")

    # Creating all the widgets and adding them to the grid
    l5_blank = Label(labelFrame, text="", anchor="e")
    l5_blank.grid(row=10, column=0, sticky="w")
    l7_blank = Label(labelFrame, text="", anchor="e")
    l7_blank.grid(row=11, column=0, sticky="w")
    b1 = Button(labelFrame, text="NEXT", width="10", command=lambda: viewWeatherFull(day, type, om.get(), om2.get()))
    b1.grid(row=12, column=0, sticky="n")
    b1 = Button(labelFrame, text="BACK", width="10", command=lambda: viewWeather("Monday"))
    b1.grid(row=12, column=0, sticky="w")
    l8_blank = Label(labelFrame, text="", anchor="e")
    l8_blank.grid(row=11, column=0, sticky="w")

# ✔ Day
# ✘ Data-type
# ✘ Starting time
# ✘ Ending time
def viewWeather(day):
    global dev
    global deverror
    # Making the window global so it can be closed from other functions.
    global weather2
    deverror = 0
    # Checking if developer mode is enabled/disabled.
    try:
        # 0 = Off, 1 = On
        if var1.get() == 1:
            # Setting developer mode to enab
            USING_DEV_MODE = True
            print("")
        else:
            # Setting developer mode to disabled.
            USING_DEV_MODE = False
        if USING_DEV_MODE == True:
            try:
                file = open(day + '.txt', 'r+')
            except FileNotFoundError:
                deverror += 1
                deverror = str(deverror)
                print("_" * 70, "\n")
                print("DEVELOPER - Data for", day, "could not be found!")
                print("Still continuing... " + "[" + deverror + "]")
                print("Program will not display any data.")
                print("_" * 70)
                deverror = int(deverror)
    except:
        pass

    # Trying to destroy the first and third window.
    try:
        weather.destroy()
        weather3.destroy()
        
    except:
        pass

    # Trying to destroy the 3rd weather window.
    try:
        weather3.destroy()
        
    except:
        pass
    
    # Creating the second weather window.
    weather2 = Tk()
    # Using the resolution (either custom or default)
    weather2.geometry(RESOLUTION)
    # Setting the window title(from messages.txt)
    weather2.title(WINDOW_TITLE)
    weather2.wm_iconbitmap('logo.ico')

    # Setting the background image.
    background = PhotoImage(file='Background Yellow.png')
    label = Label(image=background)
    label.grid(row=0)
    label.image = background
    variable = StringVar(weather2)
    
    # Creating the Frame for all the widgets.
    labelFrame = Frame(weather2)
    labelFrame.grid(row=0,column=1)

    # Variable key:
    # Button / bu
    # Label / l
    # Blank label / l_blank
    # Drop down box / om
    # Button (BACK/NEXT) / b

    # Creating all the widgets and adding them to the grid.
    l1 = Label(labelFrame, text="Weather", font="Arial 85 bold",  anchor="w")
    l1.grid(row=0, column=0)
    l2 = Label(labelFrame, text="  Please select a data-type to continue", font="Arial 12 bold")
    l2.grid(row=1, column=0, sticky="w")
    l3_blank = Label(labelFrame, text="", anchor="e")
    l3_blank.grid(row=2, column=0)
    l3 = Label(labelFrame, text="  TYPE", font="Arial 12 bold", anchor="w", foreground="lightyellow")
    l3.grid(row=3, column=0, sticky="w")

    # Creating the drop down box.
    om = Combobox(labelFrame, values=type, width="39", state="readonly")
    om.set("Average")
    om.grid(row=5, column=0, sticky="w")

    # Creating all the widgets and adding them to the grid.
    l5_blank = Label(labelFrame, text="", anchor="e")
    l5_blank.grid(row=6, column=0, sticky="w")
    l7_blank = Label(labelFrame, text="", anchor="e")
    l7_blank.grid(row=7, column=0, sticky="w")
    b1 = Button(labelFrame, text="NEXT", width="10", command=lambda: viewWeatherType(day, om.get()))
    b1.grid(row=10, column=0, sticky="n")
    b1 = Button(labelFrame, text="BACK", width="10", command=lambda: weatherMenu())
    b1.grid(row=10, column=0, sticky="w")
    l8_blank = Label(labelFrame, text="", anchor="e")
    l8_blank.grid(row=11, column=0, sticky="w")

# ✘ Day
# ✘ Data-type
# ✘ Starting time
# ✘ Ending time
def weatherMenu():
    # Making the window global so it can be closed from other functions.
    global weather
    global var1
    # Catching any error that occures to make it easy to debug/resolve.
    try:
        try:
            weather2.destroy()
        except:
            pass
        
        # Creating the main/first weather window.
        weather = Tk()
        weather.geometry(RESOLUTION)
        weather.title(WINDOW_TITLE)
        weather.wm_iconbitmap('logo.ico')
        
        # Setting the background image.
        background = PhotoImage(file='Background Yellow.png')
        label_bg = Label(image=background)
        label_bg.grid(row=0)
        label_bg.image = background
        
        # Creating the Frame for all the widgets.
        labelFrame = Frame(weather)
        labelFrame.grid(row=0,column=1)

        infoFrame = tkinter.Frame(labelFrame, bg="yellow")
        infoFrame.grid(row=0, column=5)

        infoLabel = Label(infoFrame, text="Version 0.92 [15/03] - Latest")
        infoLabel.grid(row=10, column=1)

       # Frame for all other bars.
        bar_o = tkinter.Frame(weather)
        bar_o.grid(row=2, column=0)

        # Frame for the settings button.
        bar = tkinter.Frame(bar_o)
        bar.grid(row=2, column=1)

        # Frame for the blank space.
        bar2 = tkinter.Frame(bar_o)
        bar2.grid(row=2, column=2)
        
        # Frame for the restart button.
        bar3 = tkinter.Frame(bar_o)
        bar3.grid(row=2, column=3)

        # Frame for the blank space.
        bar4 = tkinter.Frame(bar_o)
        bar4.grid(row=2, column=4)
        
        # Frame for the close button.
        bar5 = tkinter.Frame(bar_o)
        bar5.grid(row=2, column=5)

        # Variable key:
        # Button / bu
        # Label / l
        # Blank label / l_blank
        # Drop down box / om
        # Button (BACK/NEXT) / b
        
        bu = Button(bar, text="SETTINGS")
        bu.grid(row=0, column=0)
        lbu1 = Label(bar2, text="                        ")
        lbu1.grid(row=0, column=0)
        bu2 = Button(bar3, text="RESTART", command=lambda: restartProgram())
        bu2.grid(row=0, column=0)
        lbu2 = Label(bar4, text="                        ")
        lbu2.grid(row=0, column=0)
        bu3 = Button(bar5, text="CLOSE", command=lambda: exitProgram())
        bu3.grid(row=0, column=0)
        
        # Creating all the widgets and adding them to the grid.
        l1 = Label(labelFrame, text="Weather", font="Arial 85 bold",  anchor="w")
        l1.grid(row=0, column=0)
        l2 = Label(labelFrame, text="  Please select a day to continue", font="Arial 12 bold")
        l2.grid(row=1, column=0, sticky="w")
        l3_blank = Label(labelFrame, text="", anchor="e")
        l3_blank.grid(row=2, column=0)
        l3 = Label(labelFrame, text="  DAY", font="Arial 12 bold", anchor="w", foreground="lightyellow")
        l3.grid(row=3, column=0, sticky="w")

        # Creating the drop down box.
        om = Combobox(labelFrame, values=days, width="39", state="readonly")
        om.set("Monday")
        om.grid(row=5, column=0, sticky="w")

        # Creating all the widgets and adding them to the grid.
        l5_blank = Label(labelFrame, text="", anchor="e")
        l5_blank.grid(row=6, column=0, sticky="w")
        l7_blank = Label(labelFrame, text="", anchor="e")
        l7_blank.grid(row=7, column=0, sticky="w")
        b1 = Button(labelFrame, text="NEXT", width="10", command=lambda: viewWeather(om.get()))
        b1.grid(row=10, column=0, sticky="n")
        b1 = Button(labelFrame, text="BACK", width="10", command=lambda: viewWeather(e1.get(), e2.get()))
        l8_blank = Label(labelFrame, text="", anchor="e")
        l8_blank.grid(row=11, column=0, sticky="w")
        var1 = IntVar()
        if DEV_MODE == True:
            c = Checkbutton(labelFrame, text="DEVELOPER MODE", variable=var1)
            c.grid(row=12, column=0, sticky="w")

    # If an error occurs, detailed information of the error will be printed to the console.
    except Exception as exception:
        # Prints the name of the error and the cause.
        # Prints the name of the function where the error happened.
        # This makes it easier for debugging.
        # Error | Line | Source | Info
        exc_type, exc_value, exc_traceback = sys.exc_info()
        e_line = exc_traceback.tb_lineno
        e_name = exc_traceback.tb_frame.f_code.co_name
        e_info = traceback._some_str(exception)
        e_error = exc_type.__name__
        saveCrash(error=e_error, line=e_line, source=e_name, info=e_info)
        # Printing the crash message using custom print method.
        cprint(PREFIX + ' ' + CRASH_MESSAGE, 79)
        try:
            if CRASH_RESTART == True:
                cprint("The program will now attempt to restart...", 79)
                time.sleep(1)
                cprint("Restarting in 3 seconds...", 79)
                time.sleep(1)
                cprint("Restarting in 2 seconds...", 79)
                time.sleep(1)
                cprint("Restarting in 1 second...", 79)
                time.sleep(1)
                restartProgram()
            else:
                exitProgram()
        except:
            exitProgram()
            
# Function to retrieve and print the data.
# Starting time and amount of data wanted is required.
def getData(st, q):
    # st // Starting time (int/str)
    # q // Data quantity (int)
    first_time = st.replace(":", "")
    # Trying to open the data file.
    try:
        # Opening the days file.
        with open(dayz + '.txt') as myFile:
            for num, line in enumerate(myFile, 1):
                # Looking for the starting time in the file.
                if first_time in line:
                    # Test code - removed.
                    # print("_" * 40, "\n")
                    # print('[LOG] - Line number for', num)
                    # print("_" * 40)
                    numz = int(num)
                    break
    # If day file containing data can not be opened.
    except FileNotFoundError:
        if USING_DEV_MODE == True:
            cprint(DEV_PREFIX + ' ' + 'File could not be opened when looking for the line number for data.', 79)
            cprint(DEV_PREFIX + ' ' + 'Program will now be restarted.', 79)
            restartProgram()
    # Trying to retrieve and print the first bit of the data.
    try: 
        time_n = numz
        temp_n = numz
        wind_n = numz + 1
        loc_n = numz + 2
        data_f = open(dayz + '.txt', 'r+')
        line = data_f.readlines()
        temp_f = line[temp_n]
        wind_f = line[wind_n]
        loc_f = line[loc_n]
        # Looking for the integers.
        # Ignores:
        # "Temperature: "
        # "Wind speed: "
        # "Location: "
        temp = int(re.search(r'\d+', temp_f).group())
        wind = int(re.search(r'\d+', wind_f).group())
        loc = int(re.search(r'\d+', loc_f).group())
        temp_a = temp
        wind_a = wind
        temp = str(temp)
        wind = str(wind)
        loc = str(loc)
        # Printing the starting time data (unless data-type is Average)
        if dtype != "Average":
            print("_" * 70, "\n")
            print("Day:", dayz)
            print("Time:", st)
            print("Temperature:", temp + "°C")
            print("Wind spped:", wind + " mph")
            print("Location:", loc)
            print("_" * 70)

        # For reference:
        # REF 1b - FIXED
        # REF 2b - FIXED

        # When the user wants to view all the data.
        if "All" in dtype:
            # Checking for the amount of data that needs to be viewed.
            if q == 1:
                temp_n2 = numz + 5
                wind_n2 = numz + 6
                loc_n2 = numz + 7
                temp_f2 = line[temp_n2]
                wind_f2 = line[wind_n2]
                loc_f2 = line[loc_n2]
                temp2 = int(re.search(r'\d+', temp_f2).group())
                wind2 = int(re.search(r'\d+', wind_f2).group())
                loc2 = int(re.search(r'\d+', loc_f2).group())
                temp2 = str(temp2)
                wind2 = str(wind2)
                loc2 = str(loc2)
                timez = int(first_time)
                timez += 30
                timez = str(timez)
                timez = "0" + timez
                timezz = timez[:2] + ':' + timez[2:]
                print("")
                print("Day:", dayz)
                print("Time:", timezz)
                print("Temperature:", temp2 + "°C")
                print("Wind speed:", wind2 + " mph")
                print("Location:", loc2)
                print("_" * 70)

            # When the time quantity is two.
            # Example: 08:00 - (08:30) - 09:00
            if q == 2:
                temp_n2 = numz + 5
                wind_n2 = numz + 6
                loc_n2 = numz + 7
                temp_f2 = line[temp_n2]
                wind_f2 = line[wind_n2]
                loc_f2 = line[loc_n2]
                temp2 = int(re.search(r'\d+', temp_f2).group())
                wind2 = int(re.search(r'\d+', wind_f2).group())
                loc2 = int(re.search(r'\d+', loc_f2).group())
                temp2 = str(temp2)
                wind2 = str(wind2)
                loc2 = str(loc2)
                timez = int(first_time)
                timez += 30
                timez = str(timez)
                timez = "0" + timez
                timezz = timez[:2] + ':' + timez[2:]
                print("")
                print("Day:", dayz)
                print("Time:", timezz)
                print("Temperature:", temp2 + "°C")
                print("Wind speed:", wind2 + " mph")
                print("Location:", loc2)
                print("_" * 70)

                # //
                # //
                
                temp_n3 = numz + 10
                wind_n3 = numz + 11
                loc_n3 = numz + 12
                temp_f3 = line[temp_n3]
                wind_f3 = line[wind_n3]
                loc_f3 = line[loc_n3]
                temp3 = int(re.search(r'\d+', temp_f3).group())
                wind3 = int(re.search(r'\d+', wind_f3).group())
                loc3 = int(re.search(r'\d+', loc_f3).group())
                temp3 = str(temp3)
                wind3 = str(wind3)
                loc3 = str(loc3)
                timezzz = int(timez)
                timezzz += 70
                timezzz = str(timezzz)
                timezzz = "0" + timezzz
                timezzzz = timezzz[:2] + ':' + timezzz[2:]
                print("")
                print("Day:", dayz)
                print("Time:", timezzzz)
                print("Temperature:", temp3 + "°C")
                print("Wind speed:", wind3 + " mph")
                print("Location:", loc3)
                print("_" * 70)

                # //
                # //

            if q == 3:
                temp_n2 = numz + 5
                wind_n2 = numz + 6
                loc_n2 = numz + 7
                temp_f2 = line[temp_n2]
                wind_f2 = line[wind_n2]
                loc_f2 = line[loc_n2]
                temp2 = int(re.search(r'\d+', temp_f2).group())
                wind2 = int(re.search(r'\d+', wind_f2).group())
                loc2 = int(re.search(r'\d+', loc_f2).group())
                temp2 = str(temp2)
                wind2 = str(wind2)
                loc2 = str(loc2)
                timez = int(first_time)
                timez += 30
                timez = str(timez)
                timez = "0" + timez
                timezz = timez[:2] + ':' + timez[2:]
                print("")
                print("Day:", dayz)
                print("Time:", timezz)
                print("Temperature:", temp2 + "°C")
                print("Wind speed:", wind2 + " mph")
                print("Location:", loc2)
                print("_" * 70)

                # //
                # //
                
                temp_n3 = numz + 10
                wind_n3 = numz + 11
                loc_n3 = numz + 12
                temp_f3 = line[temp_n3]
                wind_f3 = line[wind_n3]
                loc_f3 = line[loc_n3]
                temp3 = int(re.search(r'\d+', temp_f3).group())
                wind3 = int(re.search(r'\d+', wind_f3).group())
                loc3 = int(re.search(r'\d+', loc_f3).group())
                temp3 = str(temp3)
                wind3 = str(wind3)
                loc3 = str(loc3)
                timezzz = int(timez)
                timezzz += 70
                timezzz = str(timezzz)
                timezzz = "0" + timezzz
                timezzzz = timezzz[:2] + ':' + timezzz[2:]
                print("")
                print("Day:", dayz)
                print("Time:", timezzzz)
                print("Temperature:", temp3 + "°C")
                print("Wind speed:", wind3 + " mph")
                print("Location:", loc3)
                print("_" * 70)

                # //
                # //

                temp_n6 = numz + 15
                wind_n6 = numz + 16
                loc_n6 = numz + 17
                temp_f6 = line[temp_n6]
                wind_f6 = line[wind_n6]
                loc_f6 = line[loc_n6]
                temp6 = int(re.search(r'\d+', temp_f6).group())
                wind6 = int(re.search(r'\d+', wind_f6).group())
                loc6 = int(re.search(r'\d+', loc_f6).group())
                temp6 = str(temp6)
                wind6 = str(wind6)
                loc6 = str(loc6)
                timezzz = int(timezzz)
                timezzz += 30
                timezzz = str(timezzz)
                timezzzzz = "0" + timezzz
                timezzzzz = timezzzzz[:2] + ':' + timezzzzz[2:]
                print("")
                print("Day:", dayz)
                print("Time:", timezzzzz)
                print("Temperature:", temp6 + "°C")
                print("Wind speed:", wind6 + " mph")
                print("Location:", loc6)
                print("_" * 70)

                # //
                # //

            if q == 4:
                temp_n2 = numz + 5
                wind_n2 = numz + 6
                loc_n2 = numz + 7
                temp_f2 = line[temp_n2]
                wind_f2 = line[wind_n2]
                loc_f2 = line[loc_n2]
                temp2 = int(re.search(r'\d+', temp_f2).group())
                wind2 = int(re.search(r'\d+', wind_f2).group())
                loc2 = int(re.search(r'\d+', loc_f2).group())
                temp2 = str(temp2)
                wind2 = str(wind2)
                loc2 = str(loc2)
                timez = int(first_time)
                timez += 30
                timez = str(timez)
                timez = "0" + timez
                timezz = timez[:2] + ':' + timez[2:]
                print("")
                print("Day:", dayz)
                print("Time:", timezz)
                print("Temperature:", temp2 + "°C")
                print("Wind speed:", wind2 + " mph")
                print("Location:", loc2)
                print("_" * 70)

                # //
                # //
                
                temp_n3 = numz + 10
                wind_n3 = numz + 11
                loc_n3 = numz + 12
                temp_f3 = line[temp_n3]
                wind_f3 = line[wind_n3]
                loc_f3 = line[loc_n3]
                temp3 = int(re.search(r'\d+', temp_f3).group())
                wind3 = int(re.search(r'\d+', wind_f3).group())
                loc3 = int(re.search(r'\d+', loc_f3).group())
                temp3 = str(temp3)
                wind3 = str(wind3)
                loc3 = str(loc3)
                timezzz = int(timez)
                timezzz += 70
                timezzz = str(timezzz)
                timezzz = "0" + timezzz
                timezzzz = timezzz[:2] + ':' + timezzz[2:]
                print("")
                print("Day:", dayz)
                print("Time:", timezzzz)
                print("Temperature:", temp3 + "°C")
                print("Wind speed:", wind3 + " mph")
                print("Location:", loc3)
                print("_" * 70)

                # //
                # //

                temp_n6 = numz + 15
                wind_n6 = numz + 16
                loc_n6 = numz + 17
                temp_f6 = line[temp_n6]
                wind_f6 = line[wind_n6]
                loc_f6 = line[loc_n6]
                temp6 = int(re.search(r'\d+', temp_f6).group())
                wind6 = int(re.search(r'\d+', wind_f6).group())
                loc6 = int(re.search(r'\d+', loc_f6).group())
                temp6 = str(temp6)
                wind6 = str(wind6)
                loc6 = str(loc6)
                timezzz = int(timezzz)
                timezzz += 30
                timezzz = str(timezzz)
                timezzzzz = "0" + timezzz
                timezzzzz = timezzzzz[:2] + ':' + timezzzzz[2:]
                print("")
                print("Day:", dayz)
                print("Time:", timezzzzz)
                print("Temperature:", temp6 + "°C")
                print("Wind speed:", wind6 + " mph")
                print("Location:", loc6)
                print("_" * 70)

                # //
                # //

                temp_n6 = numz + 20
                wind_n6 = numz + 21
                loc_n6 = numz + 22
                temp_f6 = line[temp_n6]
                wind_f6 = line[wind_n6]
                loc_f6 = line[loc_n6]
                temp6 = int(re.search(r'\d+', temp_f6).group())
                wind6 = int(re.search(r'\d+', wind_f6).group())
                loc6 = int(re.search(r'\d+', loc_f6).group())
                temp6 = str(temp6)
                wind6 = str(wind6)
                loc6 = str(loc6)
                timezzz = int(timezzz)
                timezzz += 30
                timezzz = str(timezzz)
                timezzzzz = "0" + timezzz
                timezzzzz = timezzzzz[:2] + ':' + timezzzzz[2:]
                print("")
                print("Day:", dayz)
                print("Time: 10:00")
                print("Temperature:", temp6 + "°C")
                print("Wind speed:", wind6 + " mph")
                print("Location:", loc6)
                print("_" * 70)
                
        # If the chosen data type is "Average"
        elif "Average" in dtype:
            if q == 1:
                # Getting the 2nd temperature / wind speed.
                temp_n2 = numz + 5
                wind_n2 = numz + 6
                temp_f2 = line[temp_n2]
                wind_f2 = line[wind_n2]
                temp2 = int(re.search(r'\d+', temp_f2).group())
                wind2 = int(re.search(r'\d+', wind_f2).group())

                # Calculating the average temperature.
                temp3 = (temp2 + temp_a) / 2

                # Calculating the average wind speed.
                wind3 = (wind2 + wind_a) / 2
                
                temp3 = float(temp3)
                wind3 = float(wind3)

                # Printing the data including the times chosen.
                print("")
                print("Day:", dayz)
                print("Time: " + st + " - " + flast)
                print("Average Temperature: {0:.2f} °C".format(temp3))
                print("Average Wind speed: {0:.2f} mph".format(wind3))
                print("_" * 70)
                
            if q == 2:
                # Getting the 2nd temperature / wind speed.
                temp_n2 = numz + 5
                wind_n2 = numz + 6
                temp_f2 = line[temp_n2]
                wind_f2 = line[wind_n2]
                temp2 = int(re.search(r'\d+', temp_f2).group())
                wind2 = int(re.search(r'\d+', wind_f2).group())

                # Getting the 3rd temperature / wind speed.
                temp_n3 = numz + 10
                wind_n3 = numz + 11
                temp_f3 = line[temp_n3]
                wind_f3 = line[wind_n3]
                temp3 = int(re.search(r'\d+', temp_f3).group())
                wind3 = int(re.search(r'\d+', wind_f3).group())

                # Calculating the average temperature.
                temp4 = (temp2 + temp3 + temp_a) / 3

                # Calculating the average wind speed.
                wind4 = (wind2 + wind3 + wind_a) / 3
                temp4 = float(temp4)
                wind4 = float(wind4)

                # Printing the data including the times chosen.
                print("")
                print("Day:", dayz)
                print("Time: " + st + " - " + flast)
                print("Average Temperature: {0:.2f} °C".format(temp4))
                print("Average Wind speed: {0:.2f} mph".format(wind4))
                print("_" * 70)
                
            if q == 3:
                # Getting the 2nd temperature / wind speed.
                temp_n2 = numz + 5
                wind_n2 = numz + 6
                temp_f2 = line[temp_n2]
                wind_f2 = line[wind_n2]
                temp2 = int(re.search(r'\d+', temp_f2).group())
                wind2 = int(re.search(r'\d+', wind_f2).group())

                # Getting the 3rd temperature / wind speed.
                temp_n3 = numz + 10
                wind_n3 = numz + 11
                temp_f3 = line[temp_n3]
                wind_f3 = line[wind_n3]
                temp3 = int(re.search(r'\d+', temp_f3).group())
                wind3 = int(re.search(r'\d+', wind_f3).group())

                # Getting the 4th temperature / wind speed.
                temp_n4 = numz + 15
                wind_n4 = numz + 16
                temp_f4 = line[temp_n4]
                wind_f4 = line[wind_n4]
                temp4 = int(re.search(r'\d+', temp_f4).group())
                wind4 = int(re.search(r'\d+', wind_f4).group())


                # Calculating the average temperature.
                temp5 = (temp2 + temp3 + temp4 + temp_a) / 4

                # Calculating the average wind speed.
                wind5 = (wind2 + wind3 + wind4 + wind_a) / 4
                temp5 = float(temp5)
                wind5 = float(wind5)

                # Printing the data including the times chosen.
                print("")
                print("Day:", dayz)
                print("Time: " + st + " - " + flast)
                print("Average Temperature: {0:.2f} °C".format(temp5))
                print("Average Wind speed: {0:.2f} mph".format(wind5))
                print("_" * 70)

            if q == 4:
                # Getting the 2nd temperature / wind speed.
                temp_n2 = numz + 5
                wind_n2 = numz + 6
                temp_f2 = line[temp_n2]
                wind_f2 = line[wind_n2]
                temp2 = int(re.search(r'\d+', temp_f2).group())
                wind2 = int(re.search(r'\d+', wind_f2).group())

                # Getting the 3rd temperature / wind speed.
                temp_n3 = numz + 10
                wind_n3 = numz + 11
                temp_f3 = line[temp_n3]
                wind_f3 = line[wind_n3]
                temp3 = int(re.search(r'\d+', temp_f3).group())
                wind3 = int(re.search(r'\d+', wind_f3).group())

                # Getting the 4th temperature / wind speed.
                temp_n4 = numz + 15
                wind_n4 = numz + 16
                temp_f4 = line[temp_n4]
                wind_f4 = line[wind_n4]
                temp4 = int(re.search(r'\d+', temp_f4).group())
                wind4 = int(re.search(r'\d+', wind_f4).group())

                # Getting the 5th temperature / wind speed.
                temp_n5 = numz + 20
                wind_n5 = numz + 21
                temp_f5 = line[temp_n5]
                wind_f5 = line[wind_n5]
                temp5 = int(re.search(r'\d+', temp_f5).group())
                wind5 = int(re.search(r'\d+', wind_f5).group())

                # Calculating the average temperature.
                temp6 = (temp2 + temp3 + temp4 + temp5 + temp_a) / 5

                # Calculating the average wind speed.
                wind6 = (wind2 + wind3 + wind4 + wind5 + wind_a) / 5
                temp6 = float(temp6)
                wind6 = float(wind6)

                # Printing the data including the times chosen.
                print("")
                print("Day:", dayz)
                print("Time: " + st + " - " + flast)
                print("Average Temperature: {0:.2f} °C".format(temp6))
                print("Average Wind speed: {0:.2f} mph".format(wind6))
                print("_" * 70)
                
        # If the chosen data type is "Custom"
        # How the custom data-type will work:
        # Users can select to only see data if the temperature/wind speed is above a certain value.
        # Users can choose to see all the data for a specific time for all days.
        # This data can also be averaged out.
        # ...and more.
        elif "Custom" in dtype:
            # This has not been created, a custom error message will be shown.
            print("")
            print(PREFIX + ' ' + ERROR_DEV)
            print("_" * 70)
            
    # If an unknown error occurs:
    except:
        # Printing the unknown error message.
        # cprint()
        print("_" * 70, "\n")
        print(ERROR_PREFIX + ' ' + ERROR_UNKNOWN)
        print("_" * 70)
        # Printing the custom crash message along with the custom prefix.
        cprint(CORE + ' ' + CRASH_MESSAGE, 70)
        exc_type, exc_value, exc_traceback = sys.exc_info()
        # Getting the line number of the error.
        e_line = exc_traceback.tb_lineno
        # Getting the source of the error.
        e_name = exc_traceback.tb_frame.f_code.co_name
        # Getting information about the error.
        e_info = traceback._some_str(exception)
        # Getting the name of the error.
        e_error = exc_type.__name__
        # Using the custom saveCrash() function.
        saveCrash(error=e_error, line=e_line, source=e_name, info=e_info)
        
# Main function.
weatherMenu()
