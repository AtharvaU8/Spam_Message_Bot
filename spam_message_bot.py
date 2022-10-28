import pyautogui as pg
import time 

mess = input("Enter Message: ")
limit = input("Enter Limit: ")
time.sleep(5)
i = 0
while i < int(limit):
    pg.typewrite(mess)
    pg.press('enter')
    i+=1