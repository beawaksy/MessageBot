from pynput.keyboard import Key, Controller
keyboard = Controller()
import time

spam = input("Enter the message you want ==> ")
count = input("How many times to message ==> ")
a = input("Enter waiting time ==> ")
countdown = 5
while (countdown != 0):
    print(countdown)
    countdown = countdown - 1
    time.sleep(a)

spamCount = 1
while (spamCount != count):
    time.sleep(a)
    keyboard.type(spam)
    keyboard.press(Key.enter)
    spamCount = spamCount + 1

print("finito :3")
