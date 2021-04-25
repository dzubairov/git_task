from scipy.io import wavfile
import scipy.io
import matplotlib.pyplot as plt
import numpy as np
# wav='SOUND.wav'
# samplerate, data = wavfile.read(wav)
# length=data.shape[0]/samplerate
# time = np.linspace(0., length, data.shape[0])
# max=float('-inf')
# min=float('inf')
# ma=float('-inf')
# mi=float('inf')
# channel1=[]
# channel2=[]
# for i in range(data.shape[0]):
#     if data[i][1]<min:
#         min=data[i][1]
#     if data[i][1]>max:
#         max=data[i][1]
#     if data[i][0]<mi:
#         mi=data[i][0]
#     if data[i][0]>ma:
#         ma=data[i][0]
#     channel1.append(data[i][0])
#     channel2.append(data[i][1])
# h= (max(max,ma)-min(min,mi))
# for i in range(data.shape[0]):
#     channel1[i]=1.65+channel1[i]//(h//2)*1.65
#     channel2[i] = 1.65 + channel2[i] // (h // 2) * 1.65
# for j in range(len(channel1)):
#         num2dac(round(channel1[j]*256/3.3))
#         time.sleep(1/samplerate)
#         for k in range(8):
#                 GPIO.setup(convert_pinv(k), GPIO.OUT)
#                 GPIO.output(convert_pinv(k), 0)
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import numpy
import matplotlib.pyplot as plt

def convert_pinv(n):
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

def num2dac(number):
    arr = decToBinList(number)
    for i in range(8):
        if arr[i]:
            ledNumber = convert_pinv(7 - i)
            GPIO.setup(ledNumber, GPIO.OUT)
            GPIO.output(ledNumber, 1)
def sin(t,frequancy,samplingFrequancy):
    x=[]
    i=0
    while i<=t:
        x.append(i*2 *numpy.pi * frequancy)
        i+=1/samplingFrequancy
    y=numpy.sin(x)
    for i in range(len(y)):
        y[i]=1.65+1.65*y[i]
    for j in range(len(x)):
        num2dac(round(y[j]*256/3.3))
        time.sleep(1/samplingFrequancy)
        for k in range(8):
                GPIO.setup(convert_pinv(k), GPIO.OUT)
                GPIO.output(convert_pinv(k), 0)
    return x,y
def wav():
    wav='SOUND.wav'
    samplerate, data = wavfile.read(wav)
    length=data.shape[0]/samplerate
    time = np.linspace(0., length, data.shape[0])
    max_=float('-inf')
    min_=float('inf')
    ma=float('-inf')
    mi=float('inf')
    channel1=[]
    channel2=[]
    for i in range(data.shape[0]):
        # if data[i][1]<min_:
        #     min_=data[i][1]
        # if data[i][1]>max_:
        #     max_=data[i][1]
        # if data[i][0]<mi:
        #     mi=data[i][0]
        # if data[i][0]>ma:
        #     ma=data[i][0]
        channel1.append(data[i][0])
        channel2.append(data[i][1])
    # h=max(max_,ma)-min(min_,mi)
    h=64500
    for i in range(data.shape[0]):
        channel1[i]=1.65+channel1[i]/(h//2)*1.65
        channel2[i] = 1.65 + channel2[i] / (h // 2) * 1.65

    plt.plot(time, channel1, label="Left channel")
    plt.plot(time, channel2, label="Right channel")
    plt.show()
    for j in range(len(channel1)):
            num2dac(round(channel1[j]*256/3.3))
            time.sleep(1/samplerate)
            for k in range(8):
                    GPIO.setup(convert_pinv(k), GPIO.OUT)
                    GPIO.output(convert_pinv(k), 0)
wav()