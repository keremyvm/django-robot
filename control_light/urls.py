from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("leds/<str:command>/", views.leds, name="leds"),
    path("readGraph/", views.readGraph, name="readGraph"),
    path("servo/", views.servo, name="servo"),
    path("enviarServo/<str:command>/", views.enviarServo, name="enviarServo"),
]
