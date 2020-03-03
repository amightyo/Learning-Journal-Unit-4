# Section 6.2 of your textbook describes incremental development. Do the exercise at the end of that section:

# As an exercise, use incremental development to write a function called hypotenuse that returns the length of the
# hypotenuse of a right triangle given the lengths of the other two legs as arguments.
# Record each stage of the development process as you go. (Downey, 2015)

# After the final stage of development, print the output of hypotenuse(3, 4) and two other calls to hypotenuse with
# different arguments.

# Include all of the following in your Learning Journal:

# An explanation of each stage of development, including code and any test input and output.
# The output of hypotenuse(3,4).
# The output of two additional calls to hypotenuse with different arguments.

import math


def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)


def main():
    print(hypotenuse(3, 4))
    print(hypotenuse(5, 4))
    print(hypotenuse(9, 3))


if __name__ == "__main__":
    main()
