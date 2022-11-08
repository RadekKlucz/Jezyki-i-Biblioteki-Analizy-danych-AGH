"""
zajecia.py: The file contains two functions: Euclidean algorithm, Least common mul
tiple 
"""

__name__ = "__main__"
__author__ = "Radoslaw Kluczewski"
__version__ = "1.0"
__status__ = "accomplished"

def gcd(number_1, number_2):
    """
    Euclidean algorithm
    """
    if number_2 == 0:
        return number_1
    else:
        return gcd(number_2, number_1 % number_2)

def lcm(number_1, number_2):
    """
    Least common multiple
    """
    return int((number_1 * number_2 / gcd(number_1, number_2)))


def main():
    while True:
        try:
            number_1 = int(input("Put your number one: "))
            number_2 = int(input("Put your number two: "))
            assert number_1 > 0 and number_2 > 0, "Numbers must be positive"
            print(gcd(number_1, number_2))
            print(lcm(number_1, number_2))
            break
        except (AssertionError, ValueError, TypeError):
            print("Put correct numbers")
        

if __name__ == "__main__":
    main()
    