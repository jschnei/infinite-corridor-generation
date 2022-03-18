import random

from utils import WORDS

# vowel binary

VOWELS = 'UOIEA'
VOWEL_WORDS = [word for word in WORDS if all(word.count(vowel) <= 1 for vowel in VOWELS)]

def vowel_sig(word):
  return ''.join(sorted([c for c in word if c in VOWELS], reverse=True))

VOWEL_SIGS = [
''.join([v for i, v in enumerate(VOWELS) if (j & (1 << i)) > 0])
for j in range(32)
]

SIG_WORDS = {
  sig: [] for sig in VOWEL_SIGS
}

for word in VOWEL_WORDS:
  SIG_WORDS[vowel_sig(word)].append(word)

# VOWEL_BINARY_MESSAGE = MESSAGE4

class VowelBinary:
  def __init__(self, message):
    self.message = message
    self.index = 0
  
  def generate(self, first_letter=None):
    cur_letter = self.message[self.index]
  
    cur_sig = VOWEL_SIGS[ord(cur_letter) - ord('A') + 1]
    
    if first_letter is not None:
      good_words = [word for word in SIG_WORDS[cur_sig] if word[0] == first_letter]
    else:
      good_words = SIG_WORDS[cur_sig]
    
    if not good_words:
      return None
      
    # update state
    self.index = (self.index + 1) % len(self.message)
    
    return random.choice(good_words)