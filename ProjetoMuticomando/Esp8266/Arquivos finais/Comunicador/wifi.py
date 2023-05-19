import network

class Wifi():
    """
        This class simplify the Wi-fi
        connection and deliver more configurations
        to the ESP's user.
    """
    
    def __init__(self):
        """
            Just create a Wifi and network instance
            and the configurations will set up
            next by the user.
        """
        self.net = network.WLAN(network.STA_IF)
        self.net.active(True)
        
            
    def connect(self, ssid, pwd):
        """
            Try to connect with Wifi's information
            was passed as parameters.
        """
        self.net.connect(ssid, pwd)
            
        self.status()
        
        
    def status(self):
        """
            Represent the current status of
            the wirelles connection.
        """
        
        while not self.net.isconnected():                       
            pass    
        
        print("\nConnection successful!")
        print(self.net.ifconfig())