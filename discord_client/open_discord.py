import pyautogui as pg
import time

'''
The function uses the pyautogui library to emulate user actions.
A specific key combination open the discord application and the combination of
ctrl+k open the search functionality to search for a specific channel.
'''


def launch_discord():
    print("Launching Discord...")
    pg.hotkey('win', '5')  # key combination to launch discord application
    time.sleep(20)
    print("selecting channel...")
    pg.hotkey('ctrl', 'k')  # open search option
    time.sleep(2)
    pg.write("# ai_project_images")  # write channel's name
    time.sleep(2)
    pg.press('enter')
    print("Channel selected")
    print("Ready\n")

