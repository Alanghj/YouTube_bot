import pyautogui
import pyperclip
import time


# Get in on chrome!

pyautogui.PAUSE = 1

pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")

# Write on chrome
pyautogui.hotkey("ctrl", "l")
term_search = ['biscoito', 'agua']
pyautogui.write(term_search[0])
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(397, 416)





