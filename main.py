#!/usr/bin/env python
"""
Author(s):  D. Knowles
Date:       27 Jan 2020
Desc:       Coded poetry
"""

import pandas as pd
import random

class PoemCreator():
    def __init__(self):
        self.words = pd.read_csv("words.csv")

    def adj(self):
        n = self.words.count()["adj"]
        r = random.randint(0,n-1)
        return self.words["adj"][r]

    def noun(self):
        n = self.words.count()["noun"]
        r = random.randint(0,n-1)
        return self.words["noun"][r]

    def article(self):
        n = self.words.count()["art"]
        r = random.randint(0,n-1)
        return self.words["art"][r]

    def verb(self):
        n = self.words.count()["verb"]
        r = random.randint(0,n-1)
        return self.words["verb"][r]

    def adverb(self):
        n = self.words.count()["adv"]
        r = random.randint(0,n-1)
        return self.words["adv"][r]

    def preposition(self):
        n = self.words.count()["prep"]
        r = random.randint(0,n-1)
        return self.words["prep"][r]

    def punctuation(self):
        n = self.words.count()["punc"]
        r = random.randint(0,n-1)
        return self.words["punc"][r]

    def compose(self,l):
        line = ""
        for w in l:
            if w == "adj":
                line += self.adj() + " "
            elif w == "noun":
                line += self.noun() + " "
            elif w == "verb":
                if line[-2] == 's':
                    line += self.verb() + " "
                else:
                    line += self.verb() + "s "
            elif w == "adv":
                line += self.adverb() + " "
            elif w == "art":
                line += self.article() + " "
            elif w == "prep":
                line += self.preposition() + " "
            elif w == "ger":
                line += self.verb() + "ing "
            else:
                print("error!!!!")

        line = line[:-1]
        line += self.punctuation() + "\n"
        return line

    def sentence(self):
        sent = [['art','adj','noun','verb','adv','prep','art','adj','noun'],
                ['ger','adv','art','noun','verb'],
                ['adj','noun'],
                ['ger'],
                ['noun','verb'],
                ['art','noun'],
                ['prep','noun','art','verb']]
        r = random.randint(0,len(sent)-1)
        return sent[r]

    def create(self,n):
        poem = ""
        for ii in range(n):
            poem += pc.compose(self.sentence())
        return poem


if __name__ == '__main__':
    pc = PoemCreator()
    poem = pc.create(8)
    print(poem)
