# def square(x):
#     return x * x

from squares import square # importing the square function


for i in range(10):
    print(f"The square of {i} is {square(i)}")

    # prints the squares of the numbers from 0 to 9

import squares

for i in range(10):
    print(f"The square gets {i} is {squares.square(i)}")
    # prints the squares of the numbers from 0 to 9
