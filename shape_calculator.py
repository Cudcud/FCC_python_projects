from math import floor

class Rectangle:

  def __init__(self, width, height) :
    self.width  = width
    self.height = height

  def __str__(self) :
    return f'Rectangle(width={self.width}, height={self.height})'

  #methods below are simple geometrical calculation that the task asked for

  def set_width(self, n_width) :
    self.width = n_width

  def set_height(self, n_height) :
    self.height = n_height

  def get_area(self) :
    area = self.width * self.height
    return area

  def get_perimeter(self) :
    perimeter = 2*(self.width + self.height)
    return perimeter

  def get_diagonal(self) :
    diagonal = (self.width ** 2 + self.height ** 2) ** .5
    return diagonal

  def get_picture(self) :
    if self.width > 50 or self.height > 50 :
      return 'Too big for picture.'
    else :
      str_picture = ''
      for n in range(self.height):
        str_picture += '*'*self.width + '\n'
      return str_picture

  def get_amount_inside(self, other) :
    counter = 0
    if  self.width >= other.width and self.height >= other.height :
      counter += floor(self.width/other.width)*floor(self.height/other.height)
      return counter
    else :
      return counter

class Square(Rectangle):

  #sets side as both width and height of parent class
  def __init__(self, side):
        self.side = side
        super().__init__(side, side)

  def __str__(self) :
    return f'Square(side={self.side})'

  #basically set_side = set_width = set_height
  def set_side(self, n_side) :
    self.side = n_side
    super().set_width(n_side)
    super().set_height(n_side)

  def set_width(self, *args)  :
    return self.set_side(*args)

  def set_height(self, *args) :
    return self.set_side(*args)
