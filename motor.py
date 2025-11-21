from machine import Pin
import time

#motor1a
motor1_pin_a = Pin(12, Pin.OUT)
motor1_pin_b = Pin(13, Pin.OUT)

#motor2a
motor2_pin_a = Pin(18, Pin.OUT)
motor2_pin_b = Pin(19, Pin.OUT)

motor1_pin_a.on()
motor1_pin_b.off()