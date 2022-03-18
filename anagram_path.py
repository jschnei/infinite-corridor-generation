import itertools
import pickle
import random

from collections import defaultdict, deque

from utils import NTHS, NUMS, WORDS

def anagram_sig(word):
    return ''.join(sorted(word))

ANAGRAM_LOOKUP = defaultdict(list)
for word in WORDS:
    ANAGRAM_LOOKUP[anagram_sig(word)].append(word)

class AnagramPath:
  def __init__(self, message):
    self.message = message
    preprocess_path = 'anagram_path_preprocess/{}.pkl'.format(message.lower())
    self.graph = pickle.load(
        open(preprocess_path, 'rb'),
        encoding='utf-8'
    )

    self.cur = None
    self.mid = None
  
  def generate(self, first_letter=None):
    if self.cur is None:
      if first_letter is None:
        poss_starts = [(word, index) for word, index in self.graph if index == 0]
      else:
        poss_starts = [(word, index) for word, index in self.graph if index == 0 and first_letter in word]
      self.cur = random.choice(poss_starts)

    if self.mid is not None:
      good_words = ANAGRAM_LOOKUP[self.mid]
    elif self.cur is not None:
      good_words = ANAGRAM_LOOKUP[self.cur[0]]

    if first_letter is not None:
      good_words = [word for word in good_words if word[0] == first_letter]

    if not good_words:
      return None

    if self.mid is not None:
      self.mid = None
    else:
      nxt = random.choice(list(self.graph[self.cur]))
      # print "cur:", self.cur
      # print "nxt:", nxt
      # print "letter:", self.message[self.cur[1]]
      self.mid = anagram_sig(self.cur[0] + nxt[0] + self.message[self.cur[1]])
      # print "mid:", self.mid
      self.cur = nxt
      

    return random.choice(good_words)


def test():
  generator = AnagramPath("FIRSTFIVE")
  for _ in range(50):
    print(generator.generate())