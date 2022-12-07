# __name__ = "__main__"
__author__ = "Radoslaw Kluczewski"
__version__ = "1.0"
__status__ = "accomplished"

from collections import deque

class Trie:
    def __init__(self, words) -> None:  # czy ten obiekt jest gotowy do użycia?
        self.words = words
        # An empty list has been created with empty dictonary (0 state on diagram)
        self.trie = [{"next state": [], "fail link": 0, "value": "", "final word": []}]


    def next(self, character, state):  # przesłonięcie symbolu wbudowanego
        """
        The function returns the next state if the i sing of value in dictionary is equal to input character. 
        Otherwise, the function returns 0 value with meaning False value.

        Args:
            state (int): Current state
            character (str): Input character

        Returns:
            i or 0: i returns state and 0 value returns False
        """
        try:
            for i in self.trie[state]["next state"]:
                if self.trie[i]["value"] == character:
                    return i
            return 0
        except KeyError as error:
            # If the module in not main and the show_trie method was used before the search_pattern method, 
            # the function displays an error message
            print(type(error), error)
            print("Use the search method first and then the show trie method")


    def sapling(self, word):
        """
        The function creates a sapling without fail link. 

        Args:
            word (str): Enter a word from the word list
        """
        # Iterate through the state starting at state 0
        actual_state = 0    
        for i in word:
            # If the function "next" returns True overwrite the actual state
            if self.next(i, actual_state):
                actual_state = self.next(i, actual_state)
            # If the function "next" does not return True, the condition appends to trie a new dictionary with the i character of the word. 
            # Otherwise append the new next states to the list of next states and change the actual state
            else:
                self.trie.append({"next state": [], "fail link": 0, "value": i, "final word": []})
                self.trie[actual_state]["next state"].append(len(self.trie) - 1)
                actual_state = len(self.trie) - 1
        # If word has been spelled completely include it in the end word list
        self.trie[actual_state]["final word"].append(word)


class BuildTree(Trie):  # to jest nazwa dla funkcji, a nie klasy
    def __init__(self, words) -> None:
        super().__init__(words)
        self.representation = "Trie("
        # Create a trie using the fail link function and the BuildTrie methods
        for word in self.words:
            self.sapling(word)
        self.fail_link()


    def fail_link(self):
        """
        The function that builds completely trie with the fail link arguments. 
        """
        # Create a enpty queue and append to it the node form the first dictionary in the trie 
        queue = deque(i for i in self.trie[0]["next state"])
        while queue:
            # Take the first node from the queue and remove it from the queue
            actual_node = queue[0]
            queue.remove(actual_node)
            # Check for the actual_node next nodes and add them to the queue
            for i in self.trie[actual_node]["next state"]:
                queue.append(i)
                # Check if the actual_node is the falink and add it to the state variable if is True
                state = self.trie[actual_node]["fail link"]
                while (state != 0 and bool(self.next(self.trie[i]["value"], state)) == False):
                    state = self.trie[state]["fail link"]
                #
                self.trie[i]["final word"] += self.trie[self.trie[i]["fail link"]]["final word"]
                self.trie[i]["fail link"] = self.next(self.trie[i]["value"], state)


    def show_trie(self): # funkcja zostawiona ale nie uzywana, zastepuje ja teraz __repr__
        """
        The fuction to show the created trie.
        """
        # Delete the empty elements of the trie
        for i in range(len(self.trie)):
            if self.trie[i]['value'] == "":
                self.trie[i].pop('value')
            if self.trie[i]['fail link'] == 0:
                self.trie[i].pop('fail link')
            if len(self.trie[i]['final word']) == 0:
                self.trie[i].pop('final word')
            if len(self.trie[i]['next state']) == 0:
                self.trie[i].pop('next state')
        # Print the prepared trie
        for j in range(len(self.trie)):
            if self.trie[j] == self.trie[0]:
                for val in self.trie[0].values():
                    print(f"The root of the constructed tree, where the next states are: {val}")
            else:
                print(f"{self.trie[j]}")


    def __repr__(self):
        for j in range(len(self.trie)):
            self.representation = self.representation +  f"{self.trie[j]}"
        self.representation = self.representation + ")"
        return self.representation


class SearchStrings(BuildTree):  # przerost liczby klas
    def __init__(self, words) -> None:
        super().__init__(words)
        self.list_of_trues = []


    def check_inside(self, text):
        """
        The function checks if the input patterns exist in the input string.
        
        Args:
            text (str): A text which it will be checked.

        Returns:
            (bool): Print whether the patterns exist in the input text.
        
        """
        self.list_of_trues = [(i in text) for i in self.words]
        print(f"If the words {self.words} exist in the text? {self.list_of_trues} ")
 
        
    def search_patterns(self, string):
        """
        The function searches the input string for the patterns.
        
        Args:
            string (str): A text which it will be searched.
            Returns:
            (dict): A dictionary mapping patterns exist in the input string.
        """
        # Create a dictionary of existing patterns and add positions to them
        output_words = {}
        start_state = 0
        for i in range(len(string)):
            while (bool(self.next(string[i], start_state)) is False and start_state != 0):
                try:
                    start_state = self.trie[start_state]["fail link"]
                except KeyError as error:
                    # If the module in not main and the show_trie method was used before the search_pattern method, 
                    # the function displays an error message
                    print(type(error), error)
                    print("Use the search method first and then the show trie method")
                    # return KeyError
            start_state = self.next(string[i], start_state)
            if bool(start_state) is not False:
                try:
                    for j in self.trie[start_state]["final word"]:
                        if j not in output_words:
                            output_words[j] = []
                        position = i - len(j) + 1
                        output_words[j].append(position)
                except KeyError as error:
                    # If the module in not main and the show_trie method was used before the search_pattern method, 
                    # the function displays an error message
                    print(type(error), error)
                    print("Use the search method first and then the show trie method")
                    # return KeyError
            else:
                start_state = 0
        for key in output_words:
            for value in output_words[key]:
                print(f"The beginning of the word: {key} was find at the position: {value}")


def main():
    """
    The main function to input patterns and the text. This function has two option to print the prefered output. 
    """

    input_patterns = input("Enter a list of patterns (e.g. words separated by spaces):\n>>")
    input_patterns = input_patterns.lower().split()
    input_string = input("Enter the text in which you are looking for patterns:\n>>")
    input_string = input_string.lower()
    aho_corastic = SearchStrings(input_patterns)
    aho_corastic.check_inside(input_string)

    while True:
        option = int(input("Select option 1 (search) or 2 (draw tree):\n>>"))  # a co z ValueError?
        
        if option == 1:
            aho_corastic.search_patterns(input_string)
            break
        elif option == 2:
            print("Created tree \n -------------------------------------" )
            # aho_corastic.show_trie()
            print(repr(aho_corastic))
            print("-------------------------------------")
            break
        else:
            print("You chose the wrong option! try again:\n>>")


if __name__ == "__main__":
    main()
