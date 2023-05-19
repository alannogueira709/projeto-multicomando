import uasyncio as usc
from acts import Acts
from time import sleep_ms

class Composer():
    """
        This class is a representation of a interpretation
        of a moviment group registered to the robot.
    """
    
    
    def __init__(self, presentation, length):
        self.__acts = Acts()
        self.__presentation = presentation
        self.__length = length + 1
    
    
    def execute(self):
        for i in range(1, self.__length):
            act_key = "act" + str(i)
            print(f"Iniciando o ato: {act_key}\n")
            sleep_ms(1000)
            self.__filter(act_key)
    
    
    def __filter(self, act):
        act_object = self.__presentation[act]
        if "moviment" in act_object:
            usc.run(self.__single(act_object))
        elif "moviments" in act_object:
            usc.run(self.__many(act_object))
        elif "queue" in act_object:
            usc.run(self.__queue(act_object))
    

    async def single(self, act_object):
        moviment = act_object["moviment"]
        if moviment == "Motor":
            speed_A = act_object["speed"][0]
            speed_B = act_object["speed"][1]
            time_ms = acact_object["time"]
            usc.create_task(self.__acts.tank(speed_A,
                                             speed_B,
                                             time_ms))
        elif moviment == "Led":
            leds = act_object["leds"]
            time_ms = act_object["time"]
            repeat = act_object["repeat"]
            blink = True if repeat > 1 else False
            usc.create_task(self.__acts.led(leds,
                                            time_ms,
                                            repeat,
                                            blink = blink))
            

    async def many(self, act_object):
        moviments = act_object["moviments"]
        length = len(moviments)
        for i in range(0, length):
            moviment = moviments[i]
            details = act_object["details"][i]
            if moviment == "Motor":
                speed_A = details["speed"][0]
                speed_B = details["speed"][1]
                time_ms = details["time"]
                usc.create_task(self.__acts.tank(speed_A,
                                                 speed_B,
                                             time_ms))
            elif moviment == "Led":
                leds = details["leds"]
                time_ms = details["time"]
                repeat = details["repeat"]
                blink = True if repeat > 1 else False
                usc.create_task(self.__acts.led(leds,
                                                time_ms,
                                                repeat,
                                                blink = blink))


    async def queue(self, act_object):
        moviments = act_object["queue"]
        length = len(moviments)
        for i in range(0, length):
            moviment = moviments[i]
            details = act_object["details"][i]
            if moviment == "Motor":
                speed_A = details["speed"][0]
                speed_B = details["speed"][1]
                time_ms = details["time"]
                await self.__acts.tank(speed_A, speed_B, time_ms))
            
            elif moviment == "Led":
                leds = details["leds"]
                time_ms = details["time"]
                repeat = details["repeat"]
                blink = True if repeat > 1 else False
                await self.__acts.led(leds, time_ms, repeat, blink = blink))

    
