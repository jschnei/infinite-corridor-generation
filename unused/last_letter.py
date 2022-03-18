import random

from utils import WORDS

# last letters

class LastLetter:
  def __init__(self, message):
    self.message = message
    self.index = 0
  
  def generate(self, first_letter=None):
    last_letter = self.message[self.index]
  
    if first_letter is not None:
      good_words = [word for word in WORDS if word[0] == first_letter and word[-1] == last_letter]
    else:
      good_words = [word for word in WORDS if word[-1] == last_letter]

    if not good_words:
      return None

    self.index = (self.index + 1) % len(self.message)
    
    return random.choice(good_words)