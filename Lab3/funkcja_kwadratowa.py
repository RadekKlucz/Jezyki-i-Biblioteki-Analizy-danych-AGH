def function(a, b, c, x_1, x_2):
    sum =  x_1 * x_1 * a + x_1 * b + c
    return sum

def main():
    while True:
        try:
            aa = float(input("wprowadz a:"))
            bb = float(input("wprowadz b: "))
            cc = float(input("wprowadz c: "))
            xx_1 = float(input("x_1: "))
            xx_2 = float(input("x_2: "))
            print(function(aa, bb, cc, xx_1, xx_2))
            # print(function("1", 1, 1, 1, 1))
            break
        except (ValueError, TypeError) as e:
            print(e)

if __name__ == "__main__":
    main()