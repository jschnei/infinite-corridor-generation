import random

from utils import WORDS

# auto-acronym

ACRONYM_FORCE_PROB = 0.9
class AutoAcronym:
  def __init__(self, message):
    self.message = message
    self.index = 0
    self.forward_index = 0
    self.acronym_index = 0
    self.cur_prefix = []
  
  def generate(self, first_letter=None):
    while self.acronym_index < len(self.cur_prefix) and self.message[self.index] == self.cur_prefix[self.acronym_index]:
      self.acronym_index += 1
      self.index = (self.index + 1) % len(self.message)
  
    if self.acronym_index == len(self.cur_prefix):
      if first_letter is not None:
        good_words = [word for word in WORDS if len(word) == 5 and word[0] == first_letter]
      else:
        good_words = [word for word in WORDS if len(word) == 5]
      
      if not good_words:
        return None
      
      better_words = [word for word in good_words if self.message[self.forward_index] in word]
      if better_words and random.random() < ACRONYM_FORCE_PROB:
        word = random.choice(better_words)
      else:
        word = random.choice(good_words)
      
      for c in word:
        self.cur_prefix.append(c)
      for c in word[1:]:
        if c == self.message[self.forward_index]:
          self.forward_index = (self.forward_index + 1) % len(self.message)
      self.acronym_index += 1
      
      return word
    else:
      actual_first = self.cur_prefix[self.acronym_index]
      
      if first_letter is not None and first_letter != actual_first:
        return None
        
      good_words = [word for word in WORDS if len(word) == 5 and word[0] == actual_first]
      if not good_words:
        return None
      better_words = [word for word in good_words if self.message[self.forward_index] in word]
      if better_words and random.random() < ACRONYM_FORCE_PROB:
        word = random.choice(better_words)
      else:
        word = random.choice(good_words)

      for c in word:
        self.cur_prefix.append(c)   
        if c == self.message[self.forward_index]:
          self.forward_index = (self.forward_index + 1) % len(self.message)
      self.acronym_index += 1
      
      return word
