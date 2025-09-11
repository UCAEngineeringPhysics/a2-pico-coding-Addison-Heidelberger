from machine import Pin, PWM
import time

#SETUP
dimmer = PWM(Pin(15))
dimmer.freq(1000)

button = Pin(14, Pin.IN, Pin.PULL_DOWN)

# I attempted to figure out the following on my own and could not,
# so I had Gemini help learn the modes and the elif statements

# Global variables to manage the state
mode = 0
MAX_MODES = 3  # 0: Off, 1: On, 2: Fade

#INTERRUPT HANDLER
def button_handler(pin):
    global mode
    
    mode = (mode + 1) % MAX_MODES
    
    time.sleep_ms(50)

# Attach the interrupt to the button pin
button.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

#MAIN LOOP
while True:
    if mode == 0:
        dimmer.duty_u16(0)
    
    elif mode == 1:
        dimmer.duty_u16(65535)

    elif mode == 2:

        for duty in range(0, 65536, 25):
            # Check if the mode has changed to exit the loop early
            if mode != 2:
                break
            dimmer.duty_u16(duty)
            time.sleep_us(500)  # Use microseconds for a smoother fade
        
        for duty in range(65535, -1, -25):
            if mode != 2:
                break
            dimmer.duty_u16(duty)
            time.sleep_us(500)
