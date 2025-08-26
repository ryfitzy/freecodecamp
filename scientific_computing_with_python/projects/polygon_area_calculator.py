class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return self.__class__.__name__ + f'(width={self.width}, height={self.height})'
    
    def set_width(self, new_width):
        if type(self) == Square:
            self.height = new_width
        self.width = new_width
    
    def set_height(self, new_height):
        if type(self) == Square:
            self.width = new_height
        self.height = new_height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2)**0.5
    
    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'
        picture = ''
        for _ in range(self.height):
            picture += self.width * '*'
            picture += '\n'
        return picture

    def get_amount_inside(self, shape):
        return (self.height // shape.height) * (self.width // shape.width)

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def __str__(self):
        return self.__class__.__name__ + f'(side={self.width})'

    def set_side(self, new_side):
        self.height = new_side
        self.width = new_side

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
