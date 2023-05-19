from machine import time_pulse_us


class ColorDB:
    """
        ColorDB is a class to represent
        a database that will store some
        colors defined by the user's test.
    """
    
    def __init__(self, db) -> None:
        """
            Create a empty dictionary by default.
            But, also create a database with initial
            values.
        """
        self.__db = db
        
    
    def add_color(self, name:str, red_scale:tuple, green_scale:tuple, blue_scale:tuple) -> None:
        """
            Create a new color in database.
        """
        if name in self.__db:
            raise BaseException("Color name already exists in database.")
        else:
            self.__db[name] = {"red": red_scale, "green": green_scale, "blue": blue_scale}
            
    
    def update_color(self, color_name:str, color_scale_names:list, color_scale_tuples:list) -> None:
        """
            Edit a color.
        """
        if color_name in self.__db:
            i = 0
            for scale_name in color_scale_names:
                self.__db[color_name][scale_name] = color_scale_tuples[i]
                i += 1
        else:
            raise BaseException("Color name doesn't exist in database.")
            
            
    def remove_color(self, name:str) -> None:
        """
            Remove a color.
        """
        if name in self.__db:
            self.__db.pop(name)
        else:
            raise BaseException("Color name doesn't exist in database.")
            
            
    def read_color(self, name:str) -> dict:
        """
            Read a specific color.
        """
        if name in self.__db:
            return self.__db[name]
        else:
            raise BaseException("Color name doesn't exist in database.")
        
        
    @property
    def colors_db(self) -> dict:
        """
           Return the entire database. 
        """
        
        return self.__db
        
        
class TCS230(ColorDB):
    """
        TCS230 is a class to represent
        the color sensor TCS-230. 
    """
    
    
    def __init__(self, s0, s1, s2, s3, data, freq=20, db={}, range_colors=10) -> None:
        """
            Get sensor's pin, frequency and color database
        """
        super().__init__(db)
        
        self.__s0 = s0
        self.__s1 = s1
        self.__s2 = s2
        self.__s3 = s3
        
        self.__data = data
        self.__freq = freq
        self.__range = range_colors
        
        self.setup()
        
    
    def setup(self) -> None:
        """
            Set up the sensor frequency.
        """
        if self.__freq == 2:
            self.__s0.value(0)
            self.__s1.value(1)
        elif self.__freq == 20:
            self.__s0.value(1)
            self.__s1.value(0)
        elif self.__freq == 100:
            self.__s0.value(1)
            self.__s1.value(1)
        else:
            raise BaseException("Invalid frequency value. Choose 2, 20 or 100.")
        
    
    def read_colors(self) -> dict:
        """
            Change s2 and s3 state to specific RGB color.
        """
        self.__s2.value(0)
        self.__s3.value(0)
        red = time_pulse_us(self.__data, 0)

        self.__s2.value(1)
        self.__s3.value(1)
        green = time_pulse_us(self.__data, 0)

        self.__s2.value(0)
        blue = time_pulse_us(self.__data, 0)
        
        return {"red": red, "green": green, "blue": blue}
        
        
    def turn_off_frequency(self) -> None:
        """
            Turn off the output frequency scaling.
        """
        self.__s0.value(0)
        self.__s1.value(0)
        
    
    def turn_on_frequency(self) -> None:
        """
            Turn on the output frequency scaling.
        """
        self.setup()
        
    
    @property
    def frequency(self) -> int:
        """
            Return the current frequency.
        """
        return self.__freq
    
    
    @frequency.setter
    def frequency(self, freq:int) -> None:
        """
            Set up a new frequency.
        """
        if freq in [2, 20, 100]:
            self.__freq = freq
            self.setup()
        else:
            raise BaseException("Invalid frequency value. Choose 2, 20 or 100.")
     
     
    @property
    def colors(self) -> dict:
        """
            Return the RGB colors as a dict.
        """
        
        return self.read_colors()
    
    
    @property
    def color_intensity(self) -> int:
        """
            Return the color intesity.
        """
        
        self.__s2.value(1)
        self.__s3.value(0)
        intensity = time_pulse_us(self.__data, 0)
        
        return intensity
    
    
    def range_color(self, color1, color2) -> bool:
        """
            Return if the color2 is in range of
            the color1.
        """
        min_color = color1 - self.__range
        max_color = color1 + self.__range
        
        return (min_color < color2) and (max_color > color2)
        

    def check_color(self, color_name) -> None:
        """
            Check if the color read is equal
            other color in database.
        """
        
        color_config = self.__db[color_name]
        color_read = self.read_colors()
        
        check_red = self.range_color(color_config["red"], color_read["red"])
        check_green = self.range_color(color_config["green"], color_read["green"])
        check_blue = self.range_color(color_config["blue"], color_read["blue"])
        
        return (check_red and check_green and check_blue)