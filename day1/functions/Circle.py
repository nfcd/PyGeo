# import numpy library
import numpy as np

class Circle:
    """
    A class that implements a circle
    """
    # initialization requires center [x, y]
    # and radius of circle    
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    
    # other derived attributes
    
    # circumference
    def circumference(self):
        return 2 * np.pi * self.radius
    
    # area
    def area(self):
        return np.pi * self.radius ** 2
    
    # x and y coordinates defining circle
    def coordinates(self):
        theta = np.arange(0,360) * np.pi / 180
        x = self.radius * np.cos(theta) + self.center[0]
        y = self.radius * np.sin(theta) + self.center[1]
        return x, y
    
    # methods
    
    # shift center in x
    def shift_in_x(self, x_value):
        self.center[0] += x_value
    
    # shift center in y
    def shift_in_y(self, y_value):
        self.center[1] += y_value