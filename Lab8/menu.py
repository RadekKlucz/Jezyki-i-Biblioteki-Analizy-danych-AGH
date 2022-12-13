def menu(options):
    options = list(options.items())
    for num, option in enumerate(options, start=1):
        print("{}. {}".format(num, option[0]))
    correct_choices = range(1, len(options) + 1)
    while True:
        try:
            choice = int(input(">> "))
            assert choice in correct_choices
        except (ValueError, AssertionError):
            pass  # just repeating the while loop
        else:
            func, args, kwargs = options[choice - 1][1]
            return func(*args, **kwargs)


def foo():
    pass


while True:
    menu({
        "Wypożycz": (foo, (), {}),
        "Prolonguj": (print, ("OK",), {}),
        "Zarezerwuj": (print, ("Rezerwacja", "niemożliwa"), {"sep": "\t"}),
        "Wyjdź": (exit, (1,), {})
    })
