"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    text_string = open(file_path).read()

    return text_string

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    chains = {}

    words = text_string.split()
    for i in range(len(words) - 2):
        word_tuple = (words[i], words[i + 1])
        
        if word_tuple in chains:
            chains[word_tuple].append(words[i + 2])
        else: # if it's NOT in the dict yet
            chains[word_tuple] = []
            chains[word_tuple].append(words[i + 2])
    
    return chains
    
       


    

def make_text(chains):
    """Return text from chains."""

    words = []
    first_words = choice(list(chains.keys()))
    while first_words[0].istitle() == False:
            first_words = choice(list(chains.keys()))
            if first_words[0].istitle() == True:
                words.append(first_words[0])
                words.append(first_words[1])
    third_word = choice(chains[first_words])
    words.append(third_word)
    new_tuple = first_words[1], third_word
    while new_tuple in chains:
        word = choice(chains[new_tuple])
        words.append(word)
        new_tuple = new_tuple[1], word
        if new_tuple not in chains:
            break

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
