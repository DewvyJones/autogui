import pygetwindow as gw
import pyautogui
import time
import subprocess
import keyboard

chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'

subprocess.Popen([chrome_path, '--new-window', 'http://localhost:3000/'])
time.sleep(0.5)

subprocess.Popen([chrome_path, '--new-window', 'http://localhost:3000/'])
time.sleep(0.5)

chrome_windows = gw.getWindowsWithTitle('Google Chrome')
if chrome_windows:
    kiosk_window = chrome_windows[0]
    dashboard_window = chrome_windows[1]
    
    username = 'kiosk'
    password = 'kiosk'
    
    # move kiosk to screen1
    kiosk_window.restore()
    time.sleep(0.5)
    kiosk_window.moveTo(0, 0)
    time.sleep(0.5)
    
    # move dashboard to screen2
    dashboard_window.restore()
    time.sleep(0.5)
    dashboard_window.moveTo(1920, 0)
    time.sleep(0.5)

    kiosk_window.activate() #focus kiosk window
    time.sleep(0.5)
    pyautogui.press('f11')
    time.sleep(0.5)
    pyautogui.click(x=1893, y=24) #logout1
    time.sleep(0.5)
    pyautogui.click(x=1873, y=74) #logout2
    time.sleep(0.5)
    pyautogui.click(x=977, y=184) #focus username
    time.sleep(0.5)
    keyboard.write(username, delay=0.1) #type username
    time.sleep(0.5)
    pyautogui.click(x=884, y=259) #focus password
    time.sleep(0.5)
    keyboard.write(password, delay=0.1) #type password
    time.sleep(0.5)
    pyautogui.click(x=923, y=311) #login submit
    time.sleep(3)
    pyautogui.click(x=1127, y=262) #alert password
    time.sleep(0.5)
    pyautogui.click(x=173, y=177) #enter kiosk
    time.sleep(0.5)

    dashboard_window.activate() #focus dashboard window
    time.sleep(0.5)
    pyautogui.press('f5')
    time.sleep(0.5)
    pyautogui.press('f11')
    time.sleep(0.5)
    pyautogui.click(x=2411, y=184) #enter dashboard
    time.sleep(0.5)
    pyautogui.click(x=2876, y=597) #sound check
    time.sleep(0.5)
    
    kiosk_window.activate() #focus kiosk window
    time.sleep(0.5)
else:
    print('Chrome window not found.')