import math


class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return ((self.width**2 + self.height**2)**.5)

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."

    h = 0
    w = 0

    string = ""
    for h in range(self.height):
      for w in range(self.width):
        string += "*"

        w += 1
      string += "\n"
      h += 1

    return string

  def get_amount_inside(self, shape):
    amount = 0

    rec_width = self.width
    rec_height = self.height
    shape_width = shape.width
    shape_height = shape.height

    if shape_width == shape_height:
      amount = int(
        math.floor((rec_width * rec_height) / shape_width) / shape_width)

      print(shape_width, rec_width, rec_height, amount)
      return amount
    else:
      w = int(math.floor(rec_width / shape_width))
      if w == 1:
        h = int(math.floor(rec_height / shape_height) - 1)
      else:
        h = int(math.floor(rec_height / shape_height))
      print(w, h)
      amount = w + h
      return amount

  def __repr__(self):
    return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, side):
    self.width = side
    self.height = side

  def set_height(self, side):
    self.width = side
    self.height = side

  def __repr__(self):
    return f"Square(side={self.width})"
