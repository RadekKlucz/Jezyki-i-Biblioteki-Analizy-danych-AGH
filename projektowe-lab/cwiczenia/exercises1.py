from re import findall

def check():
    while True:
        try:
            expr = input("Put your logical expresion: ") # eval() string to logical expresion
            return print(expr)
        except NameError as error:
            print(type(error), error, ", try again.")


def bracket():
    while True:
        try:
            expr = input("Put your logical expresion: ")
            eval(expr)
            return print(expr.replace(")", "").replace("(", ""))
        except (NameError, SyntaxError) as error:
            print(type(error), error, ", try again.")


def bal():
    pass

# def onp():
#     while True:
#         try:
#             expr = input("Put your logical expresion: ")
#             eval(expr)
#             precedence = {"^" : 4, "*" : 3, "/" : 3, "+" : 2, "-" : 2, ")" : 2, "(" : 1}
#             tokens = findall(r"\b\w*[\.]?w+\b|[\(\)\^\+\*\-\/])", expr)
#             stack = list()
#             postfix = list()
#             for t in tokens:
#                 if t.isalnum():
#                     postfix.append(t)
#                 elif t == "(":
#                     stack.append(t)
#                 elif t == ")":
#                     top = stack.pop()
#                     while top != "(":
#                         postfix.append(top)
#                         top = stack.pop()
        #     return 
        # except (NameError, SyntaxError) as error:
        #     print(type(error), error, ", try again.")

def onp():
    while True:
        try:
            expr = input("Put your logical expresion: ")
            # to check that the input doesn't have a NameError
            eval(expr)
         
            split_expr = expr.split()
            # to check that the input is correct 
            assert len(split_expr) > 1, "Remember about spaces"
            for i in split_expr:
                assert len(i) == 1, "Wrong input, remeber about spaces"
            
            scales = {"^" : 4, "*" : 3, "/" : 3, "%" : 3, "+" : 2, "-" : 2, ")" : 2, "(" : 1}
            output = []
            stock = []
            # ONP algorithm 
            for i in split_expr:
                if type(float(i)) == float:
                    output.append(i)
                elif type(i) == str:
                    stock.append(i)
                
        except (NameError, SyntaxError, AssertionError) as error:
            print(type(error), error, ", try again.")    


def main():
    # check()
    # bracket()
    onp()

if __name__ == "__main__":
    main()