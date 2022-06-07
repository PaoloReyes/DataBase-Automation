import pyautogui
pyautogui.FAILSAFE = False

print(pyautogui.position())

#X
x=[515, 565, 610, 660, 710, 760]
x2=[1050, 1150, 1250, 1350, 1450, 1550]
tolx=30
#Y
y=[410, 430, 450, 470, 490, 510, 530, 550, 570, 590, 610, 630, 650, 670, 690, 710, 730, 750, 770, 790, 810, 830, 850, 870, 890, 910, 930, 950, 970, 990, 1005]
for i in range(len(y)):
    y[i]=y[i]-3
y2=[310, 330, 355, 375, 400, 425, 450, 470, 495, 525, 550, 570, 595, 615, 640, 660, 690, 710, 735, 760, 785, 805, 830, 850, 880, 900, 925, 950, 980, 310, 330]
for ypos in range(31):
    if ypos == 29:
        pyautogui.moveTo(1050, 995)
        for clicks in range(3):
                pyautogui.click()
        for i in range(27):
            pyautogui.press("down")
    for xpos in range(6):
        pyautogui.moveTo(x[xpos], y[ypos])
        pyautogui.click()
        pyautogui.dragTo(x[xpos]+tolx, y[ypos])
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.moveTo(x2[xpos], y2[ypos])
        for clicks in range(3):
            pyautogui.click()
        pyautogui.hotkey('ctrl', 'v')
    #input()