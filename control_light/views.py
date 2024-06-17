from django.shortcuts import render
import serial
import json
import time
from django.http import JsonResponse

arduino = serial.Serial("COM5", 9600)

def detectarConfiguracionArduino():
    return {
        "pinAzul": 12,
        "pinRojo": 11,
        "servoMotPin": 3
    }

def index(request) :
    return render(request, "control_light/index.html")

def readGraph(request):
    datos = arduino.readline().decode().strip()
    objjson = json.loads(datos)
    return JsonResponse(objjson)

def servo(request): 
    return render(request, "control_light/servo.html")


def enviarServo(request, command):
    configPinServo = detectarConfiguracionArduino()
    jsonInfo = {
        "pin": configPinServo["servoMotPin"],
        "valor": command
    }
    
    jsonObj = json.dumps(jsonInfo,separators=(',', ':')).encode()
    arduino.write(jsonObj)
    print(jsonObj)
    time.sleep(1)
    return JsonResponse(jsonInfo)

def leds(request, command) :
    print(command.encode())
    arduino.write(str(command).encode())
    time.sleep(1)
        # arduino.close()
    return render(request, "control_light/leds.html")

