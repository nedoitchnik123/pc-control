import pyautogui
from sound import Sound
import os
import screen_brightness_control as sbc
import ctypes
from pathlib import Path

def volume_down():
    pyautogui.press("volume_down")
    

def mute():
    Sound.mute()

def vloume_up():
    volume = Sound.current_volume()
    Sound.volume_set(volume+5)

def back():
    pyautogui.press("left")

def pause():
    pyautogui.press("k")

def forward():
    pyautogui.press("right")

def back_video():
    pyautogui.hotkey('shift', 'p')
    
def forward_video():
    pyautogui.hotkey('shift', 'n')

def subtiters():
    pyautogui.press("c")

def shutdown():
    os.system('shutdown /s /t 1')
    
def reboot():
    os.system('shutdown /r /t 1')

def hypernation():
    os.system('shutdown /h')

shift_amount = 50
min_brightness = 0
max_brightness = 100

def brightness_plus():
    current_brightness = sbc.get_brightness()[0]
    new_brightness = min(current_brightness + 10, max_brightness)
    sbc.set_brightness(new_brightness)
    
def brightness_minus():
    current_brightness = sbc.get_brightness()[0]
    new_brightness = max(current_brightness - 10, min_brightness)
    sbc.set_brightness(new_brightness)

def clear_bin():
    SHELL32 = ctypes.windll.shell32
    SHELL32.SHEmptyRecycleBinW(None, None, 0)

def block_pc():
    os.system("rundll32.exe user32.dll,LockWorkStation")

def screen_shot():
    desktop_path = Path.home() / "Desktop"
    screenshot = pyautogui.screenshot()
    screenshot_path = desktop_path / "screenshot.png"
    screenshot.save(screenshot_path)
    return screenshot
    
def mouse_left_click():
    pyautogui.click()

def mouse_midle_click():
    pyautogui.middleClick

def mouse_right_click():
    pyautogui.rightClick()

def mouse_down():
    current_x, current_y = pyautogui.position()
    pyautogui.moveTo(current_x, current_y + shift_amount, duration=0.25) 

def mouse_right():
    current_x, current_y = pyautogui.position()
    pyautogui.moveTo(current_x + shift_amount, current_y, duration=0.25)

def mouse_up():
    current_x, current_y = pyautogui.position()
    pyautogui.moveTo(current_x, current_y - shift_amount, duration=0.25)
    
def mouse_left():
    current_x, current_y = pyautogui.position()
    pyautogui.moveTo(current_x - shift_amount, current_y, duration=0.25) 

def mouse_wheel_down():
    pyautogui.scroll(-100)

def mouse_wheel_up():
    pyautogui.scroll(100)

def switch_language():
    pyautogui.hotkey('shift', 'alt')

def win():
    pyautogui.press("win")