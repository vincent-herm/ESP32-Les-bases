from machine import Pin
import time

led = Pin(2, Pin.OUT)
bp = Pin(25, Pin.IN)

while not bp.value() :            # continue tant que bp.value() == 0
    led.value(not led.value())
    time.sleep(0.5)