"""
Program is currently set to ONLY look after Forge Station Lv. 3
Change "img_forge_station_lv3" to preferred level in if-statement (Line 92 + 95)
"""

import pyautogui
import time
import CustomFunctions as func # Custom module containing custom functions


# Image location paths
img_underground_city = "C:\\Users\\Victor\\Documents\\Visual Studio Code - Workplace\\MrMineBOT\\img\\underground_city\\underground_city.png"          #region=(1795,260,66,400)
img_forge_station = "C:\\Users\\Victor\\Documents\\Visual Studio Code - Workplace\\MrMineBOT\\img\\underground_city\\forge_station.png"                #region=(170,450,500,450)
img_forge_station_lv2 = "C:\\Users\\Victor\\Documents\\Visual Studio Code - Workplace\\MrMineBOT\\img\\underground_city\\forge_station_lv2.png"        #region=(170,450,500,450)
img_forge_station_lv3 = "C:\\Users\\Victor\\Documents\\Visual Studio Code - Workplace\\MrMineBOT\\img\\underground_city\\forge_station_lv3.png"        #region=(170,450,500,450)
img_forge_red_gem = "C:\\Users\\Victor\\Documents\\Visual Studio Code - Workplace\\MrMineBOT\\img\\underground_city\\forge_red_gem.png"                #region=(620,584,200,50)
img_forge_blue_gem = "C:\\Users\\Victor\\Documents\\Visual Studio Code - Workplace\\MrMineBOT\\img\\underground_city\\forge_blue_gem.png"              #region=(860,584,200,50)
img_forge_green_gem = "C:\\Users\\Victor\\Documents\\Visual Studio Code - Workplace\\MrMineBOT\\img\\underground_city\\forge_green_gem.png"            #region=(1100,584,200,50)
img_forge_purple_gem = "C:\\Users\\Victor\\Documents\\Visual Studio Code - Workplace\\MrMineBOT\\img\\underground_city\\forge_purple_gem.png"          #region=(620,730,200,50)
img_forge_yellow_gem = "C:\\Users\\Victor\\Documents\\Visual Studio Code - Workplace\\MrMineBOT\\img\\underground_city\\exit_btn.png"                  #region=()
img_exit_btn = "C:\\Users\\Victor\\Documents\\Visual Studio Code - Workplace\\MrMineBOT\\img\\underground_city\\exit_btn.png"                          #region=(1376,190,60,60)

# Time to forge a gem (In seconds)        Default forge time:
red_gem_forge_time = 60*10                # 10 min
blue_gem_forge_time = 60*30               # 30 min
green_gem_forge_time = (60*60) * 4        # 4 hours
purple_gem_forge_time = (60*60) * 16      # 16 hours
yellow_gem_forge_time = (60*60) * 48      # 48 hours

# Total gem-slots in Forge Station
red_gem_slots = 12
blue_gem_slots = 6
green_gem_slots = 4
purple_gem_slots = 3

total_forged_gems = 0 # Counter for total forged gems

# States for vissibility for Underground City & inventory of Forge Station
undergroud_city_is_vissible = False
forge_inventory_is_vissible = False

# Reset vissibility state of "items" [Kind of a reset to "forge_gem" function]
def reset_vissible_states():
    global undergroud_city_is_vissible
    global forge_inventory_is_vissible 
    undergroud_city_is_vissible = False
    forge_inventory_is_vissible = False

# Exit Forge Station inventory
def exit_forge_inventory():

    global undergroud_city_is_vissible
    global forge_inventory_is_vissible

    # Find and click "Exit" button
    func.msg_time("Locating \"Exit-button\"...")
    if pyautogui.locateOnScreen(img_exit_btn, region=(1376,190,60,60), grayscale=True, confidence=0.8) != None:
        func.msg_time("\"Exit-button\" located!")
        x_exit_btn, y_exit_btn = pyautogui.locateCenterOnScreen(img_exit_btn, region=(1376,190,60,60), grayscale=True, confidence=0.8)
        func.click(x_exit_btn, y_exit_btn)
        forge_inventory_is_vissible = False
    else:
        reset_vissible_states()
        func.msg_time("Unable to locate \"Exit-button\"...")
    
    time.sleep(0.1)

# Forge gem depending on given color
def forge_gem(gem_color="", *args):
    
    global undergroud_city_is_vissible
    global forge_inventory_is_vissible
    global total_forged_gems # Total forged gems

    # ----------| UNDERGROUD CITY |---------- #
    if undergroud_city_is_vissible == False: # If Underground City is not vissible, find and click it
        func.msg_time("Locating Underground City...") # Print message
        if pyautogui.locateOnScreen(img_underground_city, region=(1795,260,66,400), grayscale=True, confidence=0.8) != None: # Locate "Underground City" button
            func.msg_time("Underground City located!")
            x_undergroud_city, y_underground_city = pyautogui.locateCenterOnScreen(img_underground_city, region=(1795,260,66,400), grayscale=True, confidence=0.8) # Create x and y for center location of button
            func.click(x_undergroud_city, y_underground_city) # Click the "Underground City" button
            undergroud_city_is_vissible = True # Set vissible state of Underground City to TRUE
        else: # If not possible to find "Underground City" button, let user know (Kind of error-message)
            reset_vissible_states() # Reset vissibility states of "items"
            func.msg_time("Unable to locate Underground City...")
    
    time.sleep(0.1)

    # ----------| FORGE STATION |---------- #
    if forge_inventory_is_vissible == False and undergroud_city_is_vissible == True:
        func.msg_time("Locating Forge Station...")
        if pyautogui.locateOnScreen(img_forge_station_lv3, region=(170,450,500,450), grayscale=True, confidence=0.35) != None: # Confidence needs to be low due to in-game animations 
            func.msg_time("Forge Station located!")
            x_forge_station, y_forge_station = pyautogui.locateCenterOnScreen(img_forge_station_lv3, region=(170,450,500,450), grayscale=True, confidence=0.35)
            func.click(x_forge_station, y_forge_station)
            forge_inventory_is_vissible = True
        else:
            reset_vissible_states()
            func.msg_time("Unable to locate Forge Station...")
    
    time.sleep(0.1)

    # ----------| INVENTORY OF FORGE STATION |---------- #
    if forge_inventory_is_vissible == True:
        func.msg_time("Locating gem to forge...")
        
        # Check what color gem to forge:
        # ----------| RED GEM |---------- #
        if gem_color == "red": # Red gem
            if pyautogui.locateOnScreen(img_forge_red_gem, region=(620,584,200,50), grayscale=True, confidence=0.9) != None:
                x_forge_red_gem, y_forge_red_gem = pyautogui.locateCenterOnScreen(img_forge_red_gem, region=(620,584,200,50), grayscale=True, confidence=0.9)
                func.click(x_forge_red_gem, y_forge_red_gem, clicks=red_gem_slots)
                total_forged_gems += red_gem_slots # Increase total amount of forged gems
                red_gem_msg = str(red_gem_slots) + " red gems were forged\t" + str(total_forged_gems) + " gems were forged in total" # Create message for user
                func.msg_time(red_gem_msg) # Outprint message to user
                time.sleep(0.1)
                exit_forge_inventory() # Exit inventory
            else:
                reset_vissible_states()
                func.msg_time("Unable to locate red gem...")
 
        # ----------| BLUE GEM |---------- #
        elif gem_color == "blue": # Blue gem
            if pyautogui.locateOnScreen(img_forge_blue_gem, region=(860,584,200,50), grayscale=True, confidence=0.9) != None:
                x_forge_blue_gem, y_forge_blue_gem = pyautogui.locateCenterOnScreen(img_forge_blue_gem, region=(860,584,200,50), grayscale=True, confidence=0.9)
                func.click(x_forge_blue_gem, y_forge_blue_gem, clicks=blue_gem_slots)
                total_forged_gems += blue_gem_slots
                blue_gem_msg = str(blue_gem_slots) + " blue gems were forged\t" + str(total_forged_gems) + " gems were forged in total"
                func.msg_time(blue_gem_msg)
                time.sleep(0.1) 
                exit_forge_inventory()
            else:
                reset_vissible_states()
                func.msg_time("Unable to blue locate gem...")

        # ----------| GREEN GEM |---------- #
        elif gem_color == "green": # Green gem
            if pyautogui.locateOnScreen(img_forge_green_gem, region=(1100,584,200,50), grayscale=True, confidence=0.9) != None:
                x_forge_green_gem, y_forge_green_gem = pyautogui.locateCenterOnScreen(img_forge_green_gem, region=(1100,584,200,50), grayscale=True, confidence=0.9)
                func.click(x_forge_green_gem, y_forge_green_gem, clicks=green_gem_slots)
                total_forged_gems += green_gem_slots
                green_gem_msg = str(green_gem_slots) + " green gems were forged\t" + str(total_forged_gems) + " gems were forged in total"
                func.msg_time(green_gem_msg)
                time.sleep(0.1)
                exit_forge_inventory()
            else:
                reset_vissible_states()
                func.msg_time("Unable to locate green gem...")

        # ----------| PURPLE GEM |---------- #
        elif gem_color == "purple": # Purple gem
            if pyautogui.locateOnScreen(img_forge_purple_gem, region=(620,730,200,50), grayscale=True, confidence=0.9) != None:
                x_forge_purple_gem, y_forge_purple_gem = pyautogui.locateCenterOnScreen(img_forge_purple_gem, region=(620,730,200,50), grayscale=True, confidence=0.9)
                func.click(x_forge_purple_gem, y_forge_purple_gem, clicks=purple_gem_slots)
                total_forged_gems += purple_gem_slots
                purple_gem_msg = str(purple_gem_slots) + " purple gems were forged\t" + str(total_forged_gems) + " gems were forged in total"
                func.msg_time(purple_gem_msg)
                time.sleep(0.1)
                exit_forge_inventory()
            else:
                reset_vissible_states()
                func.msg_time("Unable to locate purple gem...")
    
    time.sleep(0.1)
