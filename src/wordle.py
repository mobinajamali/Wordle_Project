class Wordle:
    def __init__(self, file_path: str, word_len: int = 5, limit: int = 10000):
        self.words = self.generate_word_frequency(file_path, word_len, limit)

    #Building Data
    def generate_word_frequency(file_path, word_len: int, limit: int):
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