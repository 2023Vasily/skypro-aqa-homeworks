import math
def square(side):
    if isinstance(side, int):
        return side ** 2
    else:
        return math.ceil(side**2)

side_length = 3.3
area = square(side_length)
print(area)