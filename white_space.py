from pynput import keyboard
import pyperclip
import time


def on_activate_strip():
    time.sleep(0.2)
    data = pyperclip.paste()
    text = data.strip()
    pyperclip.copy(text)


with keyboard.GlobalHotKeys({
        '<ctrl>+c': on_activate_strip}) as h:
    h.join()
