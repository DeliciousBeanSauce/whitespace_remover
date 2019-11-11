#! shebang
import pyperclip
from pynput import keyboard
import time


COMBINATIONS = [
    {keyboard.Key.ctrl_l, keyboard.KeyCode(char='c')},
    {keyboard.Key.ctrl_r, keyboard.KeyCode(char='c')}
]

# The currently active modifiers
current = set()

def on_press(key):
    if any([key in comb for comb in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in comb) for comb in COMBINATIONS):
            time.sleep(0.2)
            main_function()
            

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass

def main_function():
    copy = pyperclip.paste()
    text = copy.strip()
    pyperclip.copy(text)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
