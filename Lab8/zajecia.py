# def main():
#     while True:
#         action = input("Choose action: (1, 2, 3)\n")
#         match action:
#             case ("1"):
#                 print("Lista przedmiotów")
#             case ("2"):
#                 print("Najblizsze zajecia")
#             case "3":
#                 print("do widzenia")
#                 break
#             case _:
#                 print("Zla opcja")


# if __name__ == "__main__":
#     main()


def menu(options, handlers):
    for index, option in enumerate(options,  start=1):
        print(f"{index}. {option}")
    valid_choices = range(1, len(options) + 1)
    while True:
        try:
            choice = input("Choose option: ")
            assert choice in valid_choices
            func, args, kwargs = handlers[choice - 1]
            return func(*args, **kwargs)
        except (ValueError, AssertionError):
            pass 


def time_table():
    print("Lista przedmiotów")

def grades():
    print("Oceny z przedmiotów")




menu(["Sprawdz plan zajec", "Najblizsze zajecia", "Wyjdz"], [time_table, grades, exit])