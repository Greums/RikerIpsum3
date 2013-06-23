#!/usr/bin/env python

import pickle
import random

lines = None

def main(): 
    global lines
    lines = load_pickle()
    print generate_paragraph()


def generate_paragraph(): 
    sentence_count = random.choice(range(2, 10))
    paragraph = ''
    for i in range(sentence_count): 
        paragraph += ' ' + random.choice(lines)['text']
    return paragraph.strip()
    


def load_pickle(): 
    f = open('riker.pickle')
    return pickle.load(f)


if __name__ == '__main__': 
    main()
