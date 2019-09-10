class Ball(object):
    def __init__(self, x, y, dx, dy, radius, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color
        
    def position(self):
        center_tup = (self.x, self.y)
        return center_tup
    
    def move(self):
        self.x += self.dx
        self.y += self.dy
    
    def bounding_box(self):
        box_tup = (self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius)
        return box_tup
    
    def get_color(self):
        return self.color
    
    def some_inside(self, maxx, maxy):
        if self.x + self.radius > 0 and self.x - self.radius < maxx and \
           self.y + self.radius > 0 and self.y - self.radius < maxy:
            return True
        else:
            return False
    
    def check_and_reverse(self, maxx, maxy):
        if self.x <= 0 or self.x >= maxx:
            self.dx *= -1
        if self.y <= 0 or self.y >= maxy:
            self.dy *= -1
        