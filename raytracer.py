from lib import *

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
        if (y > 0 and y < self.height and x > 0 and x < self.width):
            self.framebuffer[y][x] = color or self.current_color
    
    def write(self, filename):
        writeBMP(filename, self.width, self.height, self.framebuffer)
        
    def render(self):
        self.write('render.bmp')
        

render = Raytracer(800, 600)
render.point(100, 100)
render.render()