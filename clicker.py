import keyboard
import pyautogui
import time

play = True
c = 0

while play:
    if keyboard.is_pressed('shift'):
        time.sleep(0.5)

        while True:
            pyautogui.click(284, 534)
            c+=1
            if c == 10000:
                pyautogui.click(1629, 271)
                pyautogui.click(1755, 1065)
                pyautogui.click(1755, 1012)
                pyautogui.click(1755, 952)
                pyautogui.click(1755, 886)
                pyautogui.click(1755, 825)
                pyautogui.click(1755, 759)
                pyautogui.click(1755, 697)
                pyautogui.click(1755, 631)
                pyautogui.click(1755, 570)
                pyautogui.click(1755, 502)
                pyautogui.click(1755, 437)
                pyautogui.click(1755, 374)
                c = 0

            if keyboard.is_pressed('shift'):
                time.sleep(0.5)
                break

            if keyboard.is_pressed('esc'):
                play = False
                break

    if keyboard.is_pressed('esc'):
        play = False