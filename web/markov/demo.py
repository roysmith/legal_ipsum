#!/usr/bin/env python

import textwrap
from glob import glob
import markov

filenames = glob('corpus/*.txt')
m = markov.from_files(filenames)

for p in range(5):
    text = m.paragraph(3, 4)
    for line in textwrap.wrap(text):
        print line
    print

# http://commons.wikimedia.org/wiki/File:%22Authority_of_Law%22_by_James_Earle_Fraser.jpg
