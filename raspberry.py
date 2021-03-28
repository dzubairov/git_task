import RPi.GPIO as GPIO
import time

def convert_pin(n):
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

def LightUp(ledNumber, period):
    ledNumber = convert_pin(ledNumber)
    GPIO.setup(ledNumber, GPIO.OUT)
    GPIO.output(ledNumber, 1)
    time.sleep(period)
    GPIO.output(ledNumber, 0)

def blink(ledNumber, blinkCount, blinkPeriod):
    ledNumber = convert_pin(ledNumber)
    GPIO.setup(ledNumber, GPIO.OUT)
    for i in range(blinkCount):
        GPIO.output(ledNumber, 1)
        time.sleep(blinkPeriod)
        GPIO.output(ledNumber, 0)
        time.sleep(blinkPeriod)

def reverse_blink(ledNumber, blinkCount, blinkPeriod):
    ledNumber = convert_pin(ledNumber)
    GPIO.setup(ledNumber, GPIO.OUT)
    for i in range(blinkCount):
        GPIO.output(ledNumber, 0)
        time.sleep(blinkPeriod)
        GPIO.output(ledNumber, 1)
        time.sleep(blinkPeriod)

def runningLight(count, period):
    ledNumber = convert_pin(0)
    GPIO.setup(ledNumber, GPIO.OUT)
    GPIO.output(ledNumber, 1)
    time.sleep(period)
    for i in range(1, count * 8):
        ledNumber = convert_pin(i % 8)
        GPIO.setup(ledNumber, GPIO.OUT)
        GPIO.output(ledNumber, 1)
        GPIO.output(convert_pin((i - 1) % 8), 0)
        time.sleep(period)

def runningDark(count, period):
    for i in range(8):
        ledNumber = convert_pin(i)
        GPIO.setup(ledNumber,GPIO.OUT)
        GPIO.output(ledNumber, 1)
    ledNumber = convert_pin(0)
    GPIO.setup(ledNumber, GPIO.OUT)
    GPIO.output(ledNumber,0)
    time.sleep(period)
    for i in range(1, count * 8):
        ledNumber = convert_pin(i % 8)
        GPIO.setup(ledNumber, GPIO.OUT)
        GPIO.output(ledNumber, 0)
        GPIO.output(convert_pin((i - 1) % 8), 1)
        time.sleep(period)
    for i in range(8):
        ledNumber = convert_pin(i)
        GPIO.setup(ledNumber,GPIO.OUT)
        GPIO.output(ledNumber, 0)

def decToBinList(decNumber):
    s = srt(bin(decNumber))
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

def cycle_shift(arr, M, N):
    M %= N
    for j in range(M):
        for i in range(N-1):
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

def runningPattern(pattern, direction):
    arr = decToBinList(pattern)
    q = int(direction/ abs(direction))
    for j in range(abs(direction)+1):
        for i in range(8):
            if arr[i]:
                ledNumber = convert_pin(7 - i)
                GPIO.setup(ledNumber, GPIO.OUT)
                GPIO.output(ledNumber, 1)
            if not arr[i]:
                ledNumber = convert_pin(7 - i)
                GPIO.setup(ledNumber, GPIO.OUT)
                GPIO.output(ledNumber, 0)
        time.sleep(1)
        cycle_shift(arr, 8, q)
        


# задание на 10
def pwm_(i):
    GPIO.setup(convert_pin(i), GPIO.OUT)

    p = GPIO.PWM(convert_pin(i), 50)  # channel=12 frequency=50Hz
    p.start(0)
    try:
        while 1:
            for dc in range(0, 101, 5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.1)
            for dc in range(100, -1, -5):
                p.ChangeDutyCycle(dc)
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    p.stop()
    GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
for i in range(8):
    GPIO.setup(convert_pin(i), GPIO.OUT)
    GPIO.output(convert_pin(i), 0)

pwm_(int(input()))