from pickle import TRUE
from random import randint

# seed() - generator startuje z wybranego przez nas miejsca 

def game():
    random_number = randint(0, 100)
    while True:
        try:
            x = int(input("Put number from 0 to 100: "))
            assert x > 0, "Number must be int (between 0 to 100)"
            if x < random_number:
                print("Za malo")
            elif x > random_number:
                print("za duzo")
            else:
                break
        except (ValueError, AssertionError):
            print("Wrong type of input or number")
        # assert str(type(x)) == "<class 'int'>", "Put corect type (int)"
        


def gen():
    res = str()
    for i in range(4):
        res += str(randint(1, 6))
    return res 


def spr(kod, pr):
    kod = list(kod)
    pr = list(pr)
    lc = 0 
    for i in range(4):
        if kod[i] == pr[i]:
            lc += 1
            kod[i] = 'x'
            pr[i] = 'y'
    lb = 0
    for i in range(4):
        for j in range(4):
            if kod[i] == pr[i]:
                lb += 1
                kod[i] = 'x'
                pr[j] = 'y'


def main():  
    try:
        game()
        # for i in range(3):
        #     print(gen())
        # kod = gen()
        # print(kod)
        # while True:
        #     pr = input(">>")
        #     odp = spr(kod, pr)
        #     print(" " * 10, odp)
        #     if odp == (4, 0):
        #         break
        #     print("Wygrales")
    except TypeError:
        print("Something is wrong")



if __name__ == "__main__":
    main()
