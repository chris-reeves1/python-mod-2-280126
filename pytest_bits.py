# import pytest
# from pytest_files.my_functions import *

# def test_add_answser():
#     result = add(1, 2)
#     assert result == 3
#     assert add(1, 2) == 3
#     assert add(-1, -1) == -2
#     assert add(0, 0) == 0

# def test_divide_by_zero_raise_error():
#     with pytest.raises(ZeroDivisionError):
#         divide(10 / 0)

# # fixtures


# # @pytest.fixture
# # def x():
# #     return Area(10, 5)

# # def test_area(x):
# #     assert x.area() == 50

# @pytest.mark.parametrize("length, width, area", [(5, 10, 50), (5, 5, 25), (10, 10, 100)])
# def test_multi_area_calcs(length, width, area):
#     x = Area(length, width)
#     assert x.area() == area
    
# @pytest.mark.skip(reason="not ready to test this yet")
# def test_skip():
#     assert add(1, 2) == 3

def count(sequence, item):
  y = 0
  for n in sequence:
    if n == item:
      y += 1
  return y


def add(a, b):
    return a + b

def divide(a, b):
    return a / b

class Area:
    def __init__(self, length, width):
        self.length, self.width = length, width

    def area(self):
        return self.length * self.width
