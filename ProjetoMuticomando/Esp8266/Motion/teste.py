from machine import Pin
from time import sleep_ms, ticks_ms, ticks_diff
from mpu import MPU6050

mpu = MPU6050(Pin(5), Pin(2))

msOld = ticks_ms()
mpu.calibrate()

while True:
    mpu.get_values()
    
    dt = ticks_diff(ticks_ms(), msOld)/1000.0
    msOld = ticks_ms()
    
    theta, phi, rho = mpu.get_complimentary_values(dt)
    if(abs(rho) >= 90):
        break
    else:
        sleep_ms(100)