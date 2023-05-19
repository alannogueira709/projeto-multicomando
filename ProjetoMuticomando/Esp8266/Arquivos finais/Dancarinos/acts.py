from led import Led
from createMotor import CreateMotor
import uasyncio as usc

class Acts:
    
    def __init__(self):
        self.__led = Led()
        self.__motorA = CreateMotor("Motor A", 5, 0)
        self.__motorB = CreateMotor("Motor B", 4, 2)
        
    
    async def led(self, leds, time_ms, repeat, blink = False):
        for i in range(0, repeat):
            self.__led.shift(leds)
            await usc.sleep_ms(time_ms)
            if blink:
                self.__led.shift("00000000")
                await usc.sleep_ms(time_ms)
            
    async def motorA(self, speed, time_ms):
        self.__motorA.speed(speed)
        await asc.sleep_ms(time_ms)
        
    
    async def motorB(self, speed, time_ms):
        self.__motorB.speed(speed)
        await usc.sleep_ms(time_ms)
        
    
    async def tank(self, speed_A, speed_B, time_ms):
        self.__motorA.speed(speed_A)
        self.__motorB.speed(speed_B)
        await usc.sleep_ms(time_ms)
    
    def finish(self):
        self.__led.shift("00000000")
        self.__motorA.speed(0)
        self.__motorB.speed(0)
