import pyautogui
import time
import CustomFunctions as func # Custom module containing custom functions


sell_all_ores_count = 0        # Counter for selling all ores
full_capacity_timer = 60*25    # Timer for capacity to reach 100% (In seconds)

# Image location paths
img_sell_center = "C:\\Users\\Victor\\Documents\\Visual Studio Code - Workplace\\MrMineBOT\\img\\sell_center\\sell_center.png"      #region=(330,480,300,300)
img_sell_all_ores = "C:\\Users\\Victor\\Documents\\Visual Studio Code - Workplace\\MrMineBOT\\img\\sell_center\\sell_all_ores.png"  #region=(500,730,230,60)
img_exit_btn = "C:\\Users\\Victor\\Documents\\Visual Studio Code - Workplace\\MrMineBOT\\img\\sell_center\\exit_btn.png"            #region=(1376,250,60,60)
img_cave_building = "C:\\Users\\Victor\\Documents\\Visual Studio Code - Workplace\\MrMineBOT\\img\\sell_center\\cave_building.png"  #region=(1795,260,66,400)
img_move_to_top = "C:\\Users\\Victor\\Documents\\Visual Studio Code - Workplace\\MrMineBOT\\img\\sell_center\\move_to_top.png"      #region=(64,144,90,90)

# State for vissibility for Sell Center
sell_center_inventory_is_vissible = False # Default = False


# Exit Forge Station inventory
def exit_sell_center_inventory():

    global sell_center_inventory_is_vissible

    # Find and click "Exit" button
    func.msg_time("Locating \"Exit-button\"...")
    if pyautogui.locateOnScreen(img_exit_btn, region=(1376,250,60,60), grayscale=True, confidence=0.75) != None:
        func.msg_time("\"Exit-button\" located!")
        x_exit_btn, y_exit_btn = pyautogui.locateCenterOnScreen(img_exit_btn, region=(1376,250,60,60), grayscale=True, confidence=0.75)
        func.click(x_exit_btn, y_exit_btn)
        sell_center_inventory_is_vissible = False
    else:
        sell_center_inventory_is_vissible = False
        func.msg_time("Unable to locate \"Exit-button\"...")
    
    time.sleep(0.1)

# Sell all ores at "Sell Center"
def sell_all_ores(*args):
    
    global sell_all_ores_count # Let function use "sell_all_ores_count" variable
    global sell_center_inventory_is_vissible

    if sell_center_inventory_is_vissible == False: # Check if Sell Center is vissible
        func.msg_time("Locating Sell Center...")

        # ----------| SELL CENTER |---------- #
        if pyautogui.locateOnScreen(img_sell_center, region=(330,480,300,300), grayscale=True, confidence=0.8) != None: # Press Sell Center, if vissible
            func.msg_time("Sell Center located!")
            x_sell_center, y_sell_center = pyautogui.locateCenterOnScreen(img_sell_center, region=(330,480,300,300), grayscale=True, confidence=0.8) # Assign x- & y-values of "Sell Center"
            func.click(x_sell_center, y_sell_center) # Click on Sell Center
            sell_center_inventory_is_vissible = True
        else: # If not vissible, press cave building & move to top
            sell_center_inventory_is_vissible = False
            func.msg_time("Unable to locate Sell Center...")

            time.sleep(0.1)

            # ----------| CAVE BUILDING|---------- #
            func.msg_time("Locating Cave Building...")
            if pyautogui.locateOnScreen(img_cave_building, region=(1795,260,66,400), grayscale=True, confidence=0.8) != None:
                func.msg_time("Cave Building located!")
                x_cave_building, y_cave_building = pyautogui.locateCenterOnScreen(img_cave_building, region=(1795,260,66,400), grayscale=True, confidence=0.8)
                func.click(x_cave_building, y_cave_building)
            else:
                func.msg_time("Unable to locate Cave Building...")

            time.sleep(0.1)

            # ----------| "GO-TO-TOP" BUTTON |---------- #
            func.msg_time("Locating \"Go-to-top\" button...")
            if pyautogui.locateOnScreen(img_move_to_top, region=(64,144,90,90), grayscale=True, confidence=0.8) != None: # Go to top
                func.msg_time("\"Go-to-top\" button located!")
                x_move_to_top, y_move_to_top = pyautogui.locateCenterOnScreen(img_move_to_top, region=(64,144,90,90), grayscale=True, confidence=0.8)
                func.click(x_move_to_top, y_move_to_top)
            else:
                func.msg_time("Unable to locate \"Go-to-top\" button...")
  
    time.sleep(0.1)

    # ----------| INVENTORY OF SELL CENTER |---------- #
    if sell_center_inventory_is_vissible == True:
        func.msg_time("Locating \"Sell all\" button")

        if pyautogui.locateOnScreen(img_sell_all_ores, region=(500,730,230,60), grayscale=True, confidence=0.8) != None:
            func.msg_time("\"Sell all\" button located!")
            x_sell_all_ores, y_sell_all_ores = pyautogui.locateCenterOnScreen(img_sell_all_ores, region=(500,730,230,60), grayscale=True, confidence=0.8)
            func.click(x_sell_all_ores, y_sell_all_ores)
            sell_all_ores_count += 1 # Increase counter for selling all ores
            sell_all_ores_msg = "All ores were sold " + str(sell_all_ores_count) + " times" # Create message for user
            func.msg_time(sell_all_ores_msg) # Print message
            exit_sell_center_inventory()
        else:
            sell_center_inventory_is_vissible = False
            func.msg_time("Unable to locate \"Sell all\" button...")
            
    time.sleep(0.1)
