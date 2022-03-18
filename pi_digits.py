import random

from utils import WORDS, WORDS_BY_LENGTH_AND_START

# pi

PI_FILE = 'pi.txt'
PI_DIGITS = open(PI_FILE, 'r').read().strip()
PI_DIGITS = [int(c) for c in PI_DIGITS if c in '0123456789']

PI_STATE = {
  'index': 0,
  'pi_index': 0
}

class PiDigits:
  def __init__(self, message):
    self.message = message
    self.index = 0
    self.pi_index = 0
  
  def generate(self, first_letter=None):
    cur_digit = PI_DIGITS[self.pi_index]
  
    if cur_digit != 0:
      if first_letter is not None:
        good_words = WORDS_BY_LENGTH_AND_START[(cur_digit, first_letter)] #[word for word in WORDS if len(word) == cur_digit and word[0] == first_letter]
      else:
        good_words = WORDS_BY_LENGTH_AND_START[(cur_digit, '*')] # [word for word in WORDS if len(word) == cur_digit]
      
      if not good_words:
        return None
      
      # update state
      self.pi_index += 1
      
      return random.choice(good_words)
    else:
      cur_letter = self.message[self.index]
      if first_letter is not None and first_letter != cur_letter:
        return None
      
      # update state
      self.pi_index += 1
      self.index = (self.index + 1) % len(self.message)
        
      return cur_letter
