from django.shortcuts import render
import serial
import json
import time
from django.http import JsonResponse
import sys

arduino = serial.Serial("COM5", 9600)

def detectarConfiguracionArduino():
    return {
        "pinAzul": "12",
        "pinRojo": "13",
        "servoMotPin": "03"
    }

def index(request) :
    return render(request, "control_light/index.html")

def leds(request, command) :
    arduino.write((str(command) + ";" + str(request.POST.get("btn", ''))).encode())
    time.sleep(1)
    return render(request, "control_light/leds.html")

def servo(request): 
    return render(request, "control_light/servo.html")



def scaling(x, in_min, in_max, out_min, out_max) :
    denominador = (float(in_max) - float(in_min)) + float(out_min)
    numerador = (float(x) - float(in_min)) * (float(out_max) - float(out_min))
    if (denominador <= 0.0):
        return numerador
    return float((numerador / denominador))


def readGraph(request):
    datos = (arduino.readline().decode().strip()).split(":")
    volt = datos[0]
    temp = datos[1]
    # parsedTemp = scaling(float(temp), 0, 1023, 0, 50)
    return JsonResponse({"temp": temp, "volt": volt})

def enviarServo(request, command):
    configPinServo = detectarConfiguracionArduino()
    # jsonObj = json.dumps(jsonInfo,separators=(',', ':')).encode()
    arduino.write(str(configPinServo["servoMotPin"] + ":" + command).encode())
    
    time.sleep(1)
    return JsonResponse({
        "pin": configPinServo["servoMotPin"],
        "valor": command
    })



