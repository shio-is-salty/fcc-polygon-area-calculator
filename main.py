# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main

rect = shape_calculator.Rectangle(5, 10)
rect.set_width(7)
rect.set_height(3)
print(rect.get_picture())
print(rect)
print("*******\n*******\n*******\n")

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
sq.get_picture()
print(sq)

# Run unit tests automatically
main(module='test_module', exit=False)
