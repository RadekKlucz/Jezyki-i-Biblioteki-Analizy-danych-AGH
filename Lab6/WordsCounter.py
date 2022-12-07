import string
from nltk import word_tokenize, FreqDist

class Counter:  # overkill - ta klasa ma jedną sensowną metodę i nie potrzebuje stanu - funkcja byłaby wygodniejsza w użyciu
    def __init__(self, filename):
        self.filename = filename


    def most_common_words(self, number=None):
        with open(self.filename) as input_file:
            contents = input_file.read()
            # remove all punctuation from text
            contents = contents.translate(str.maketrans("", "", string.punctuation))
            # split words into list of words
            contents = word_tokenize(contents.lower())
            length_of_list = len(contents)
            # The FreqDist class is used to count the number of occurrences of each word.
            common_words = FreqDist(contents)

            if number == ("all" or "All"):
                list_of_common_words = common_words.most_common(length_of_list)
                # save results to the output file
                with open("output.txt", "w", encoding="utf-8") as output_file:
                    output_file.write("\n".join("{} {}".format(*t) for t in list_of_common_words))
            else:
                number = int(number)
                print(common_words.most_common(number))
                

def main():
    while True:
        try:
            print("Put your book here:")
            file_name = input(">>")
            file_to_counter = Counter(file_name)
            print("Put number of common words that you want to find in your file. If you want to find all words type 'all'.")
            number_common_words = input(">>")
            file_to_counter.most_common_words(number_common_words)
            print("The results are in the output file.")
            break
        except (FileNotFoundError, ValueError):
                print("The file haven't been found in folder or put correct number of common words. Try again.")


if __name__ == "__main__":
    main()
