import random
import pyautogui as pg
import time
animal=('monkey','dog','donkey')
time.sleep(8)
for i in range(500):
    a=random.choice(animal)
    pg.write(f"you are{animal}")
    pg.press('enter')