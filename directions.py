import itertools
import random

from utils import WORDS

DIR_LETTERS = {
  'C': ['SW', 'SE'],
  'D': ['SE', 'SW', 'N', 'N'],
  'E': ['E', 'W', 'S', 'E', 'W', 'S', 'E'],
  'F': ['E', 'W', 'S', 'E', 'W', 'S'],
  'G': ['W', 'S', 'S', 'E', 'N', 'W'],
  'H': ['S', 'S', 'N', 'E', 'S', 'N', 'N'],
  'I': ['S', 'S'],
  'N': ['N', 'N', 'SE', 'SE', 'N', 'N'],
  'O': ['E', 'E', 'S', 'S', 'W', 'W', 'N', 'N'],
  'R': ['N', 'N', 'E', 'S', 'W', 'SE'],
  'S': ['W', 'S', 'E', 'S', 'W'],
  'T': ['E', 'S', 'S', 'N', 'N', 'E'],
  'U': ['S', 'S', 'E', 'N', 'N'],
  'V': ['SE', 'SE', 'NE', 'NE'],
  'W': ['S', 'S', 'NE', 'SE', 'N', 'N'],
  'X': ['SE', 'SW', 'NE', 'NE', 'SW', 'SE'],
  'Z': ['E', 'E', 'SW', 'SW', 'E', 'E'],
}

COMPASS_DIRECTIONS = ['N', 'E', 'S', 'W', 'NE', 'NW', 'SE', 'SW', '?']
COMPASS_LOOKUP = {
  sym: [] for sym in COMPASS_DIRECTIONS
}

for word in WORDS:
  if word.startswith('E'):
    COMPASS_LOOKUP['E'].append(word)
  elif word.startswith('W'):
    COMPASS_LOOKUP['W'].append(word)
  elif word.startswith('NE'):
    COMPASS_LOOKUP['NE'].append(word)
  elif word.startswith('NW'):
    COMPASS_LOOKUP['NW'].append(word)
  elif word.startswith('N'):
    COMPASS_LOOKUP['N'].append(word)
  elif word.startswith('SE'):
    COMPASS_LOOKUP['SE'].append(word)
  elif word.startswith('SW'):
    COMPASS_LOOKUP['SW'].append(word)
  elif word.startswith('S'):
    COMPASS_LOOKUP['S'].append(word)
  else:
    COMPASS_LOOKUP['?'].append(word)


def flatten(arrs):
  ans = []
  for arr in arrs:
    ans.extend(arr)
  return ans

class Directions:
  def __init__(self, message):
    self.message = message
    self.enc_message = flatten([DIR_LETTERS[c] + ['?'] for c in message])
    self.index = 0
  
  def generate(self, first_letter=None):
    cur_sym = self.enc_message[self.index]
    
    if first_letter is not None and first_letter != cur_sym[0]:
      return None

    good_words = COMPASS_LOOKUP[cur_sym]
    
    if not good_words:
      return None
      
    # update state
    self.index = (self.index + 1) % len(self.enc_message)

    return random.choice(good_words)


if __name__ == '__main__':
  generator = Directions("FOURTHSIX")
  for _ in range(100):
    print(generator.generate())