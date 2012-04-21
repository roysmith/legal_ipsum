#!/usr/bin/env python

import unittest2 as unittest
from pprint import pprint
from markov import Markov

class MarkovTestCase(unittest.TestCase):
    def test_create(self):
        m = Markov([])

    def assertNext(self, word1, word2, wordlist):
        m = self.markov
        words = m.next_words(word1, word2)
        self.assertEqual(words, wordlist)

    def test_one_word(self):
        self.markov = Markov(['foo'])
        self.assertNext(None, None, ['foo'])

    def test_chain(self):
        self.markov = Markov(['the', 'name', 'of', 'the', 'game'])
        pprint(dict(self.markov.table))
        self.assertNext(None, None, ['the'])
        self.assertNext(None, 'the', ['name'])

if __name__ == '__main__':
    unittest.main()
