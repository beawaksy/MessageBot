from pynput.keyboard import Key, Controller
keyboard = Controller()
import time

spam = input("spam mesajını girin ==> ")
count = input("spam mesajını kaç kere yazdırmak istediğinizi girin ==> ")

countdown = 5
while (countdown != 0):
    print(countdown)
    countdown = countdown - 1
    time.sleep(0.1)

spamCount = 1
while (spamCount != count):
    time.sleep(1)
    keyboard.type(spam)
    keyboard.press(Key.enter)
    spamCount = spamCount + 1

print("done :3")
