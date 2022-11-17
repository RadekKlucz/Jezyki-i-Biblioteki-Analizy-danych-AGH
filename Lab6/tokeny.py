import random as rd
with open("nkjp.txt") as notebook:
    liczba = rd.randint(0, 1313)
    # str(notebook).split()
    print(notebook.read(liczba))
    


