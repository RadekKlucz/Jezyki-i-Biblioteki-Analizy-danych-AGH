import string

class Counter:
    def __init__(self, filename):
        self.filename = filename
        self.dictonary = {}

    def read_file(self):
        with open(self.filename, 'r') as f:
            text = f.read()
            text = text.translate(str.maketrans("", "", string.punctuation)) 
            text = text.split()
            return text


def read_file(filename):
    dictonary = {}
    with open(filename, 'r') as f:
        text = f.read()
        text = text.translate(str.maketrans("", "", string.punctuation))        
        text1 = text.split()
        only_one_word = set(text1)
        only_one_word = list(only_one_word)
        for j in only_one_word:
            for i in text1:
                num = text1.count(j)
                dictonary[j] = num
                # print(f"{j} occured {num}")
                break
    with open("wyjscie.txt", "w") as f:
        for key, val in dictonary.items():
            f.write(f"{key} : {val}\n")
    return "Zapisane do pliku."


if __name__ == '__main__':
    print(read_file('potop.txt'))  