import pyautogui
import random
import time
import sys
import keyboard

# List of available keyboard keys (including num keys as regular numbers)
keys = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "esc", "*",
    "+", "--", "/", ",", "/", ";", "=", "{"
    , "}", "'",
]

specialKeys = [ "esc", "f1", "f2", "f3",
    "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12", "printscreen", "scrolllock", "pause", "insert",
    "home", "page up", "delete", "end", "page down", "right", "left", "down", "up", "num", "*",
    "+", "--", "/", ",", "/", ";", "=", "num enter", "{"
    , "}", "'", "Home"]

# List of specific key combinations
combinations = ["ctrl+c", "ctrl+v", "ctrl+x", "ctrl+z", "ctrl+y", "ctrl+a", "ctrl+l", "win+f1", "win+tab", "alt +tab"]

# Flag to control the script execution
running = True

def panic_button_event(e=None):
    running = False

# Listen for the panic button combination "Ctrl+Num9" to stop the script
keyboard.add_hotkey("ctrl+9", panic_button_event)
if pyautogui.hotkey("ctrl+9"):
    panic_button_event

while running:
    action = random.choice(["press_key", "press_combination", "erase_key", "change_language", "click_key", "special_key"])
    
    if action == "press_key":
        key = random.choice(keys)
        pyautogui.press(key)
    elif action == "special_key":
        specialKey = random.choice(specialKeys)
        pyautogui.hotkey(specialKey)

    elif action == "press_combination":
        combination = random.choice(combinations)
        pyautogui.hotkey(combination)
        
    elif action == "erase_key":
        pyautogui.press(["backspace", "delete"][random.randint(0, 1)])
        
    elif action == "change_language":
        # Simulate "Win+Space" to change language
        pyautogui.hotkey("win", "space")
    
    elif action == "click_key":
        key = random.choice(keys)
        pyautogui.typewrite(key)
    
    # Sleep for a random interval before the next action
    time.sleep(random.uniform(0.1, 2))

# Clean up and exit the script
keyboard.unhook_all()
