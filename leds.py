from machine import Pin
import time

led = Pin(12, Pin.OUT)
led.value(1) #Encender LED
led.off() #Apagar LED
time.sleep(1)

led = Pin(13, Pin.OUT)
led.value(1) #Encender LED
led.off() #Apagar LED
time.sleep(1)

led = Pin(18, Pin.OUT)
led.value(1) #Encender LED
led.off() #Apagar LED
time.sleep(1)

led = Pin(19, Pin.OUT)
led.value(1) #Encender LED
led.off() #Apagar LED
time.sleep(1)