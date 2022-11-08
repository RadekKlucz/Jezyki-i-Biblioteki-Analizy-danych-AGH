def build(list_of_args):
    # I am looking for the biggest word on the list of args
    sorted_list_of_args = sorted(words, key=len)
    max_word = len(sorted_list_of_args[-1])

    # An empty dictonary has been created 
    trie = {key: [] for key in range(max_word)} 

    # Trie has been created with values
    for i in range(max_word):
        # I assume that the word lenght is not the same and an error has occurred
        error = True
        while error == True:
            try:
                for j in sorted_list_of_args:
                    # if an error has occurred the variable ,,next_index'' will be used 
                    next_index = i
                    if j[i] not in trie[i]:
                        trie[i].append(j[i])
                    error = False
            except IndexError:
                next_index -= 2
                sorted_list_of_args = sorted_list_of_args[next_index:]
    return trie

def search(trie_of_patterns, text):
    position = 0
    find_pattern = ""
    key = 0
    while True:
        for i in text:
            for value in trie_of_patterns[key]:
                if value == i:
                    find_pattern += i
                    key += 1
                    position = text.index(i)
                else:
                    k = i + 1
                    text = text[k:]                  
    return print(find_pattern)

if __name__ == "__main__":
    print(build(['abc', 'aab', "cba"]))