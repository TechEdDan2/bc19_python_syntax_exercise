# Step 2.1 & 2.2 
def print_upper_words(words):
    """Print all the words in the list to upper case
        each on their own line
    """

    for w in words:
        print(w.upper())


print_upper_words(["hello", "hi", "goodbye", "yo", "yes"])

#Step 2.3 
def print_upper_words_v2(words):
    """Print all the words in the list to upper case
        each on their own line
    """

    for w in words:
        if w.startswith("e") or w.startswith("E"):
            print(w.upper())

print_upper_words_v2(["hello", "hi", "England", "goodbye", "yo", "yes", "enchidna"])


#Step 2.4
def print_upper_words_v3(words, must_start_with):
    """Print all the words in the list to upper case
        each on their own line
    """

    for w in words:
        for letter in must_start_with:
            w_upper = w.upper()
            if w_upper.startswith(letter.upper()):
                print(w_upper)
                break

print_upper_words_v3(["apple", "hello", "hi", "England", "goodbye", "yo", "yes", "enchidna"], ["h", "y"])

