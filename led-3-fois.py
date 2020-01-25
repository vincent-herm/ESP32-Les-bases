from machine import Pin
import time

led = Pin(2, Pin.OUT)       

for a in range (6) :
  led.value(not led.value())
  time.sleep(0.5)


