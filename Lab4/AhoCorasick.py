# __name__ = "__main__"
__author__ = "Radoslaw Kluczewski"
__version__ = "1.0"
__status__ = "accomplished"

from collections import deque

class BuildSapling:
    def __init__(self, words) -> None:
        self.words = words
        # An empty list has been created with empty dictonary (0 state on diagram)
        self.trie = [{"następne stany": [], "farlink": 0, "wartość": "", "słowo końcowe": []}]


    def next(self, character, state):
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
            for i in self.trie[state]["następne stany"]:
                if self.trie[i]["wartość"] == character:
                    return i
            return 0
        except KeyError as error:
            # If the module in not main and the show_trie method was used before the search_pattern method, 
            # the function displays an error message
            print(type(error), error)
            print("Użyj wpierw metody search a następnie metody show trie")
            return KeyError


    def sapling(self, word):
        """
        The function creates a sapling without farlink. 

        Args:
            word (str): Enter a word from the word list
        """
        # Iterate through the state starting at state 0
        actual_state = 0    
        for i in word:
            # If the function "next" returns True overwrite the actual state
            if bool(self.next(i, actual_state)) is True:
                actual_state = self.next(i, actual_state)
            # If the function "next" does not return True, the condition appends to trie a new dictionary with the i character of the word. 
            # Otherwise append the new next states to the list of next states and change the actual state
            else:
                self.trie.append({"następne stany": [], "farlink": 0, "wartość": i, "słowo końcowe": []})
                self.trie[actual_state]["następne stany"].append(len(self.trie) - 1)
                actual_state = len(self.trie) - 1
        # If word has been spelled completely include it in the end word list
        self.trie[actual_state]["słowo końcowe"].append(word)


class BuildTrie(BuildSapling):
    def __init__(self, words) -> None:
        super().__init__(words)
        # Create a trie using the farlink function and the BuildTrie methods
        for word in self.words:
            self.sapling(word)
        self.farlink()


    def farlink(self):
        """
        The function that builds completely trie with the farlink arguments. 
        """
        # Create a enpty queue and append to it the node form the first dictionary in the trie 
        queue = deque(i for i in self.trie[0]["następne stany"])
        while bool(queue) is True:
            # Take the first node from the queue and remove it from the queue
            actual_node = queue[0]
            queue.remove(actual_node)
            # Check for the actual_node next nodes and add them to the queue
            for i in self.trie[actual_node]["następne stany"]:
                queue.append(i)
                # Check if the actual_node is the falink and add it to the state variable if is True
                state = self.trie[actual_node]["farlink"]
                while (state != 0 and bool(self.next(self.trie[i]["wartość"], state)) == False):
                    state = self.trie[state]["farlink"]
                #
                self.trie[i]["słowo końcowe"] += self.trie[self.trie[i]["farlink"]]["słowo końcowe"]
                self.trie[i]["farlink"] = self.next(self.trie[i]["wartość"], state)


    def show_trie(self):
        """
        The fuction to show the created trie.
        """
        # Delete the empty elements of the trie
        for i in range(len(self.trie)):
            if self.trie[i]['wartość'] == "":
                self.trie[i].pop('wartość')
            if self.trie[i]['farlink'] == 0:
                self.trie[i].pop('farlink')
            if len(self.trie[i]['słowo końcowe']) == 0:
                self.trie[i].pop('słowo końcowe')
            if len(self.trie[i]['następne stany']) == 0:
                self.trie[i].pop('następne stany')
        # Print the prepared trie
        for j in range(len(self.trie)):
            if self.trie[j] == self.trie[0]:
                for val in self.trie[0].values():
                    print(f'Korzeń zbudowanego drzewa, gdzie następnymi stanami są: {val}')
            else:
                print(f"Podkorzenie drzewa prezentują się następująco: {self.trie[j]}")


class SearchStrings(BuildTrie):
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
        print(f"Czy słowa {self.words} istnieją w tekście? {self.list_of_trues} ")
 
        
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
                    start_state = self.trie[start_state]["farlink"]
                except KeyError as error:
                    # If the module in not main and the show_trie method was used before the search_pattern method, 
                    # the function displays an error message
                    print(type(error), error)
                    print("Użyj wpierw metody search a następnie metody show trie")
                    return KeyError
            start_state = self.next(string[i], start_state)
            if bool(start_state) is not False:
                try:
                    for j in self.trie[start_state]["słowo końcowe"]:
                        if j not in output_words:
                            output_words[j] = []
                        position = i - len(j) + 1
                        output_words[j].append(position)
                except KeyError as error:
                    # If the module in not main and the show_trie method was used before the search_pattern method, 
                    # the function displays an error message
                    print(type(error), error)
                    print("Użyj wpierw metody search a następnie metody show trie")
                    return KeyError
            else:
                start_state = 0
        for key in output_words:
            for value in output_words[key]:
                print(f"Początek słowa: {key} został znaleziony na pozycji: {value}")

def main():
    """
    The main function to input patterns and the text. This function has two option to print the prefered output. 
    """

    input_patterns = input("Wprowadź listę wzroców (np słowa oddzielone spacjami): ")
    input_patterns = input_patterns.lower().split()
    input_string = input("Wprowadz tekst w którym szukasz wzorców: ")
    input_string = input_string.lower()
    aho_corastic = SearchStrings(input_patterns)
    aho_corastic.check_inside(input_string)

    while True:
        try:
            option = int(input("Wybierz opcje 1 (wyszukiwanie) lub 2 (wyrysowanie drzewa): "))
            assert option == 1 or option == 2
            if option == 1:
                aho_corastic.search_patterns(input_string)
                break
            elif option == 2:
                print("Stworzone drzewo \n -------------------------------------" )
                aho_corastic.show_trie()
                print("-------------------------------------")
                break
        except AssertionError:
            print("Wybrałeś złą opcję! Spróbuj ponownie: ")


if __name__ == "__main__":
    main()