import random
from src.utils import print_error, print_success, print_warning

#random.seed(42)

class Wordle:
    def __init__(self, file_path: str, word_len: int = 5, limit: int = 10000):
        self.word_len = word_len
        self.words = self.generate_word_frequency(file_path, word_len, limit)

    #Building Data
    def generate_word_frequency(self, file_path, word_len: int, limit: int):
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

    def run(self, ):
        # Random Word
        word = random.choice(self.words)
        word = word.upper()

        # Start Game!
        num_try = 6
        success = False

        while num_try:
            guess_word = input(f'Enter a {self.word_len} letter word (or q to exit):')
            if guess_word.lower() == 'q':
                break
            guess_word = guess_word.upper()

            #word length
            if len(guess_word) != 5:
                print(f'Word must have {self.word_len} letters. You entered {len(guess_word)}!')
                continue

            # Check valid word
            if guess_word.lower() not in self.words:
                print_warning('Word is not valid!')
                continue

            # Check valid, invalid positions, invalid characters
            for w_letter, g_letter in zip(word, guess_word):
                if w_letter == g_letter:
                    print_success(f' {g_letter} ', end='')
                    print(' ', end='')
                elif g_letter in word:
                    print_warning(f' {g_letter} ', end='')
                    print(' ', end='')
                else:
                    print_error(f' {g_letter} ', end='')
                    print(' ', end='')
            print()

            # Check success
            if word == guess_word:
                print()
                print_success(' Congradulations! ')
                success = True
                break

            num_try -=1

        if not success:
            print_warning(f'Game over: The word was "{word}"!')

