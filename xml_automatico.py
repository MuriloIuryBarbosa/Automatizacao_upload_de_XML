import pyautogui
import time

#pyautogui.alert('Shuzão é foda')
pyautogui.PAUSE = 1

pyautogui.press('winleft')
pyautogui.write('NW Corporativo')
pyautogui.press('enter')
time.sleep(20)
pyautogui.write('murilo')

pyautogui.press('tab')
pyautogui.write('Amor16')
pyautogui.press('enter')

time.sleep (8)

#fecha Alertas NW
pyautogui.press('esc')
time.sleep(1)
pyautogui.hotkey('ctrlright', 'e')
time.sleep(1)
pyautogui.write('IEC0010')
pyautogui.press('enter')
pyautogui.write('002')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('f9')
time.sleep(5)
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=570,y=511 )
time.sleep(1)
pyautogui.press('f9')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('f12')
pyautogui.hotkey('shiftright', 'tab')
pyautogui.press('enter')


