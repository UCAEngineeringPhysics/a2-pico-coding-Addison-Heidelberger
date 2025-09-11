from machine import Pin, PWM, Timer
from time import sleep
import utime


# SETUP
dimmer = PWM(Pin(15))
dimmer.freq(1000)


# LOOP
while True:
    
    start_time = utime.ticks_ms()
    
    for duty in range(65535):
        dimmer.duty_u16(duty)
        sleep(0.0001)
    #print out how long it takes to reach max brightness
    #I used gemini to learn how to do this
    end_time = utime.ticks_ms()
    elapsed_time = utime.ticks_diff(end_time, start_time)

    print(f"Ramp up to max brightness took {elapsed_time} ms")
        
        
    for duty in range(65535, 0, -1):
        dimmer.duty_u16(duty)
        sleep(0.0001)
