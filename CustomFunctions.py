"""
A file containing randoms functions that are used in the code

Instead of copy'n'paste the same functions in each file, I just
have one main file - Makes it easiere if you want to edit the
functions.
"""


import time
import win32api, win32con


# Left-click for mouse
def click(x,y, clicks=1):

    for click in range(0, clicks): # Left-click X amount of times
        win32api.SetCursorPos((x,y)) # Set mouse-cursor position
        time.sleep(0.01) # Wait 0.01 second
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) # Press left click
        time.sleep(0.01) # Wait 0.01 second
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) # Release left click
        click += 1 # Increase total clicks
        time.sleep(0.1) # Wait 0.1 second

    time.sleep(0.5) # Wait 0.5 second. (Needed for click function to work properply in-game)

# Print time-stamp
def msg_time(text=""):
    print("[" + time.ctime()[11:19] + "] " + str(text))