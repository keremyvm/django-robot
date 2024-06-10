from django.shortcuts import render
import serial
import json
import time
from django.http import JsonResponse

arduino = serial.Serial("COM5", 9600)


def index(request) :
    return render(request, "control_light/index.html")

def readGraph(request):
    # arduino = serial.Serial("COM5", 9600)
    datos = arduino.readline().decode().strip()
    objjson = json.loads(datos)
    # arduino.close()
    return JsonResponse(objjson)

def leds(request, command) :
    print(command.encode())
    arduino.write(str(command).encode())
    time.sleep(1)
        # arduino.close()
    return render(request, "control_light/leds.html")
