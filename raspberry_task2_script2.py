import RPi.GPIO as GPIO
import time
import math

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
    value = 0
    while value != -1:

        print('Enter number:')
        value  = int(input())
        for i in range(8):
            GPIO.setup(convert_pin(i), GPIO.OUT)
            GPIO.output(convert_pin(i), 0)
        LightNumber(value)
       


def num2dac2(value):
    LightNumber(value)
    time.sleep(0.01)
    for i in range(8):
        GPIO.setup(convert_pin(i), GPIO.OUT)
        GPIO.output(convert_pin(i), 0)

def num2dac3(value, period):
    LightNumber(value)
    time.sleep(period / 100)
    for i in range(8):
        GPIO.setup(convert_pin(i), GPIO.OUT)
        GPIO.output(convert_pin(i), 0)

def second_func():
    print('Enter the number of repetitions')
    repetitionsNumber = int(input())
    for i in range(repetitionsNumber):
        for j in range(0, 255):
            num2dac2(int(255*(math.sin(j)+1)))
        for j in range(255, 0, -1):
            num2dac2(int(255*(math.sin(j)+1)))

def third_func():
    print('Enter the frequency')
    frequency = float(input())
    print('Enter the time')
    time = int(input())
    period = 1/frequency
    for i in range(int(time * frequency)):
        j = 0
        while j <= period:
            num2dac3(int(127*(math.sin(j)+1)), period)
            j += period/100
    

def sin():
    print('Enter the time')
    time = int(input())
    print('Enter the frequency')
    frequency = int(input())
    print('Enter the samplingFrequency')
    samplingFrequency = int(input())




GPIO.setmode(GPIO.BCM)
for i in range(8):
    GPIO.setup(convert_pin(i), GPIO.OUT)
    GPIO.output(convert_pin(i), 0)

#num2dac()

# second_func()
print(time.time())
third_func()
