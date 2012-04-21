from collections import defaultdict
import random
import string
from glob import glob
import os.path

def corpus_files():
    """Return a list of paths to standard corpus files.

    """
    my_dir = os.path.dirname(__file__)
    corpus_dir = os.path.join(my_dir, "corpus")
    filenames = glob(corpus_dir + '/*.txt')
    return filenames

def from_files(ipaths):
    """Given an iterable over pathnames, build and return a Markov
    which has been initialized from the text in those files.

    It is assumed that the files are small enough that reading each
    one in a single chunk is not excesively expensive.

    """
    words = []
    for path in ipaths:
        file_words = open(path).read().split()
        words.extend(file_words)

    return Markov(words)

class Markov:
    def __init__(self, words):
        """Injest the words (an iterable) and build a Markov table.

        """
        table = defaultdict(list)
        word1 = None
        word2 = None
        for word in words:
            key = (word1, word2)
            table[key].append(word)
            word1 = word2
            word2 = word
        self.table = table
        self.word1, self.word2 = random.choice(table.keys())

    def next_word(self):
        """Return the next word in the markov chain.

        """
        key = (self.word1, self.word2)
        words = self.table[key]
        word = random.choice(words)
        self.word1 = self.word2
        self.word2 = word
        return word

    def text(self, n):
        """Return a string containing the next n words, separated by
        spaces.

        """
        text = []
        for i in xrange(n):
            text.append(self.next_word())
        return " ".join(text)

    def sentence(self, min_words):
        """Similar to text(), except that some attempt is made to
        return a string which vaguely looks like it might be an
        English sentence.

        """
        word = 'x'
        while word[0] not in string.ascii_uppercase:
            word = self.next_word()

        text = [word]
        for i in xrange(min_words-1):
            text.append(self.next_word())

        while text[-1][-1] not in ".?!":
            text.append(self.next_word())

        return " ".join(text)

    def paragraph(self, min_words, min_sentences):
        """Return a paragraph.

        Each of the sentences in the paragraph will be at least
        min_words long, and there will be at least min_sentences in
        the paragraph.

        Sentences will be separated by two spaces.

        """
        sentences = []
        for i in range(min_sentences):
            sentences.append(self.sentence(min_words))

        # Add some random number of additional sentences, with longer
        # paragraphs being progressively less likely.
        while random.random() > 0.5:
            sentences.append(self.sentence(min_words))
            
        return "  ".join(sentences)
