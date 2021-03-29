import RPi.GPIO as GPIO
import time

def convert_pin(n):
    if n == 0:
        return 10
    if n == 1:
        return 9
    if n == 2:
        return 11
    if n == 3:
        return 5
    if n == 4:
        return 6
    if n == 5:
        return 13
    if n == 6:
        return 19
    if n == 7:
        return 26

def decToBinList(decNumber):
    s = str(bin(decNumber))
    s = s[2:]
    s = str(0) * (8 - len(s)) + s
    arr = [0] * 8
    for i in range(8):
        arr[i] = int(s[i])
    return arr

def LightNumber(number):
    arr = decToBinList(number)
    for i in range(8):
        if arr[i]:
            ledNumber = convert_pin(7 - i)
            GPIO.setup(ledNumber, GPIO.OUT)
            GPIO.output(ledNumber, 1)

def num2dac():
    print('Enter number:')
    value  = int(input())
    LightNumber(value)5


def num2dac2(value):
    LightNumber(value)

def second_func():
    print('Enter the number of repetitions')
    repetitionsNumber = int(input())
    for i in range(repetitionsNumber):
        for j in range(0, 255):
            num2dac2(j)
            time.sleep(0.3)
        for j in range(255, 0):
                num2dac2(j)
                time.sleep(0.3)


GPIO.setmode(GPIO.BCM)
for i in range(8):
    GPIO.setup(convert_pin(i), GPIO.OUT)
    GPIO.output(convert_pin(i), 0)

# num2dac()
second_func()
