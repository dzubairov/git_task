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

def convert_pin_leds(n):
    if n == 0:
        return 24
    if n == 1:
        return 25
    if n == 2:
        return 8
    if n == 3:
        return 7
    if n == 4:
        return 12
    if n == 5:
        return 16
    if n == 6:
        return 20
    if n == 7:
        return 21


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


# Первый скрипт

# script_first

def hand_acp(value):
    while True:
        print("Enter value:")
        value = int(input())
        if value == -1:
            break
        for i in range(8):
            GPIO.setup(convert_pin(i), GPIO.OUT)
            GPIO.output(convert_pin(i), 0)
        LightNumber(value)
        s = str(value) + ' = ' + str(round(value / 255 * 3.3, 3)) + 'V'
        print(s)


# script_second
def simple_acp():
    while True:
        for value in range(255):
            for i in range(8):
                GPIO.setup(convert_pin(i), GPIO.OUT)
                GPIO.output(convert_pin(i), 0)
            LightNumber(value)
            GPIO.setup(4, GPIO.IN)
            time.sleep(0.001)
            if GPIO.input(4) == 0:
                print('Digital value: ', value, ' ', 'Analog value: ',
                      str(value) + ' = ' + str(round(value / 255 * 3.3, 3)) + 'V')
                break
            for i in range(8):
                GPIO.setup(convert_pin(i), GPIO.OUT)
                GPIO.output(convert_pin(i), 0)


# script_third

def f(value):
    for i in range(8):
        GPIO.setup(convert_pin(i), GPIO.OUT)
        GPIO.output(convert_pin(i), 0)
    LightNumber(value)
    GPIO.setup(4, GPIO.IN)
    time.sleep(0.001)
    v = GPIO.input(4)
    for i in range(8):
        GPIO.setup(convert_pin(i), GPIO.OUT)
        GPIO.output(convert_pin(i), 0)
    return v


def bin_acp():
    value_r = 256
    value_l = -1
    l = 1
    r = 0
    while True:
        value_m = (value_r + value_l+1) // 2
        m = f(value_m)
        if value_r - value_l <= 1:
            print('Digital value: ', value_m, ' ', 'Analog value: ',
                  str(value_m) + ' = ' + str(round(value_m / 255 * 3.3, 3)) + 'V')
            return value_m
            break
        if m != l:
            value_r = value_m
        elif r != m:
            value_l = value_m

#script fourth

def volume():
    for i in range(8):
        GPIO.setup(convert_pin_leds(i), GPIO.OUT)
        GPIO.output(convert_pin_leds(i), 0)
    v = bin_acp()
    v = v * 8 // 255
    for i in range(v):
        GPIO.setup(convert_pin_leds(i), GPIO.OUT)
        GPIO.output(convert_pin_leds(i), 1)
    for i in range(7, v, -1):
        GPIO.setup(convert_pin_leds(i), GPIO.OUT)
        GPIO.output(convert_pin_leds(i), 0)


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, 1)
for i in range(8):
    GPIO.setup(convert_pin(i), GPIO.OUT)
    GPIO.output(convert_pin(i), 0)

# hand_acp()
# simple_acp()
# while True:
#     bin_acp()
while True:
    volume()


for i in range(8):
    GPIO.setup(convert_pin(i), GPIO.OUT)
    GPIO.output(convert_pin(i), 0)