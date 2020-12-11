import pyautogui
import time

#Make sure that your chrome browser is pin to the taskbar

pyautogui.moveTo(1777,13, duration=1)
pyautogui.click()
pyautogui.moveTo(222,1054, duration=1)
pyautogui.click()
pyautogui.moveTo(466,63, duration=1)
pyautogui.click()
pyautogui.write("Google doodle hurdles", interval=0.1)
pyautogui.press('enter')
time.sleep(3)
pyautogui.moveTo(438,397, duration=1)
pyautogui.click()
time.sleep(5)
pyautogui.moveTo(950,385, duration=1)
time.sleep(5)
pyautogui.click()

for i in range(300):
    pyautogui.press('right')
    pyautogui.press('left')
