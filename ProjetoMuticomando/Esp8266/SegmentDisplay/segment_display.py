from machine import Pin
from time import sleep_ms

VALUES = {0: "1111110", 1: "0110000", 2: "1101101", 3: "1111001", 4: "0110011", 5: "1011011", 6: "1011111", 7: "1110000", 8: "1111111", 9: "1111011"}

"""
    G F - A B     - - A - - 
    | | | | |     F       B
    - - - - -     - - G - -
    - - - - -     E       C
    | | | | |     - - D - - Dot
    E D - C Dot
"""

class SegmentDisplay:
    """
        SegmentDisplay is a class that commands
        the module's led segments.
    """
    
    def __init__(self, *pins) -> None:
        self.__pins = {}
        self.__value = ""
        self.__dot = Pin(pins[-1], Pin.OUT)
        
        self.setPins(pins)
    
    
    def setPins(self, pins:tuple) -> None:
        """
            Correlate each pin with a integer
            to make easy to control the module.
        """
        for segment in range(8):
            pin = pins[segment]
            self.__pins[segment] = Pin(pin, Pin.OUT)
            
            
    def on(self) -> None:
        """
            Turn on the module with the last value.
        """
        for pin in self.__pins:
            pin_value = self.__value[pin]
            if pin_value == "1":
                self.__pins[pin].value(1)
                
                
    def off(self) -> None:
        """
            Turn off the module.
        """
        for pin in self.__pins:
            pin_value = self.__value[pin]
            if pin_value == "1":
                self.__pins[pin].value(0)
                
                
    def value(self, value) -> None:
        """
            Get the 0 and 1 values for the
            number or letter passed to turn on
            the corret module's led.
        """
        self.__value = VALUES[value]
        
        for pin in self.__pins:
            pin_value = self.__value[pin]
            if pin_value == "1":
                self.__pins[pin].value(1)
            elif pin_value == "0":
                self.__pins[pin].value(0)
            
    def dot(self, state) -> None:
        """
            Controle the dot led.
        """
        if state == 1:
            self.__dot.value(1)
        elif state == 0:
            self.__dot.value(0)
            
            
display = SegmentDisplay(13, 12, 14, 27, 26, 25, 15, 2)

for i in range(10):
    display.value(i)
    sleep_ms(100)
    
display.off()
display.dot(1)
