import pyautogui

x, y = pyautogui.locateCenterOnScreen('images/calculator.png')
pyautogui.click(x, y)
pyautogui.typewrite('70! + 4!\n', 0.5)

x, y = pyautogui.locateCenterOnScreen('images/terminal.png')
pyautogui.click(x, y)
pyautogui.typewrite("python\n", 0.2)
pyautogui.typewrite("import math\n", 0.2)
pyautogui.typewrite('math.factorial(70) + math.factorial(4)\n', 0.1)
