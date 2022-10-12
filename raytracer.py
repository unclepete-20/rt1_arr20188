from cmath import pi, tan
from lib import *
import math
from Vector import *

class Raytracer(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clear_color = color_select(0, 0, 0)
        self.current_color = color_select(255, 255, 255)
        self.clear()
        
    def clear(self):    
        self.framebuffer = [
            [self.clear_color for x in range(self.width)]
            for y in range(self.height)
            
        ]
        
    def point(self, x, y, color = None): 
        if (y >= 0 and y < self.height and x >= 0 and x < self.width):
            self.framebuffer[y][x] = color or self.current_color
    
    def render(self):
        
        fov = int(pi / 2)
        aspect_ratio = self.width / self.height
        tana = tan(fov / 2)
        
        
        for y in range(self.height):
            for x in range(self.width):
                
                i = (2 * (x + 0.5) / self.width - 1) * aspect_ratio * tana
                j = (1 - (2 * (y + 0.5) / self.height)) * tana
                
                direction = V3(i, j, -1).norm()
                origin = V3(0, 0, 0)
                
                
                c = self.raycast(origin, direction)
                
                self.point(x, y, c)
    
    def write(self, filename):
        writeBMP(filename, self.width, self.height, self.framebuffer)
        
    def raycast(self, origin, direction):
        return color_select(255, 0, 0)

render = Raytracer(800, 600)
render.point(100, 100)
render.render()

render.write('r.bmp')