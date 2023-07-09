from termcolor import colored

#Building Data
# the function goes through the Data file and find 1000 limit words with 5 characters by default
def generate_word_frequency(file_path, word_len: int = 5, limit: int = 1000):
    #building data: a list of tuples of words with their corresponding counts
    words_freq = []
    with open(file_path) as f:
        for line in f:
            word, frequency = line.split(', ')
            frequency = int(frequency)
            words_freq.append((word, frequency))

    #sort data: sorting the list based on the most frequent items
    #sort is by default ascending, hence were we use reverse to make it descending
    words_freq = sorted(words_freq, key=lambda w_freq: w_freq[1], reverse=True)

    #limit data: getting data up to the limited number
    words_freq = words_freq[:limit]

    #drop frequency data
    words = [w_freq[0] for w_freq in words_freq]

    #filter data with len of 5 characters
    words = list(filter(lambda w: len(w) == word_len, words))

    return words

file_path = './Data/words_frequency.txt'
word_len = 5
limit = 1000

words = generate_word_frequency(file_path, word_len=word_len, limit=limit)

#--------------------------------------------------------------------
#Select a random word
import random
random.seed(42)
word = random.choice(words)
word = word.upper()

#--------------------------------------------------------------------
#Wordle Process
def print_success(text, end='\n'):
    print(colored(text, 'green', attrs=['reverse']), end=end)

def print_warning(text, end='\n'):
    print(colored(text, 'yellow', attrs=['reverse']), end=end)

def print_error(text, end='\n'):
    print(colored(text, 'red', attrs=['reverse']), end=end)

def print_grey(text, end='\n'):
    print(colored(text, 'grey', attrs=['reverse']), end=end)


num_try = 6
success = False

while num_try:
    guess_word = input(f'Enter a {word_len} letter word (or qto exit):')
    if guess_word.lower() == 'q':
        break
    guess_word = guess_word.upper()

    #word length
    if len(guess_word) != 5:
        print(f'Word must have {word_len} letters. You entered {len(guess_word)}!')
        continue

    # Check valid word
    if guess_word.lower() not in words:
        print_warning('Word is not valid!')
        continue

    # Check valid, invalid positions, invalid characters
    for w_letter, g_letter in zip(word, guess_word):
        if w_letter == g_letter:
            print_success(g_letter, end='')
        elif g_letter in word:
            print_warning(g_letter, end='')
        else:
            print_grey(g_letter, end='')
    print()

    # Check success
    if word == guess_word:
        print_success('Congradulations!')
        success = True
        break

    num_try -=1

if not success:
    print_warning(f'Game over: The word was "{word}"!')



