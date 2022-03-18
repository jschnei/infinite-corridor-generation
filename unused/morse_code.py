import random

from utils import WORDS

# morse code

DOT_WORDS = [word for word in WORDS if len(word) == 3]
DASH_WORDS = [word for word in WORDS if len(word) == 9]
SEP_WORDS = [word for word in WORDS if len(word) not in [3, 9]]

MORSE_WORDS_LOOKUP = {
  '.': DOT_WORDS,
  '-': DASH_WORDS,
  '/': SEP_WORDS
}

MORSE_ALPHABET = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split()
MORSE_ALPHABET = [cw + '/' for cw in MORSE_ALPHABET]

def encode_morse(message):
  return ''.join(MORSE_ALPHABET[ord(c) - ord('A')] for c in message)

class MorseCode:
  def __init__(self, message):
    self.message = message
    self.enc_message = encode_morse(message)
    self.index = 0
  
  def generate(self, first_letter=None):
    cur_symbol = self.enc_message[self.index]
    
    if first_letter is not None:
      good_words = [word for word in MORSE_WORDS_LOOKUP[cur_symbol] if word[0] == first_letter]
    else:
      good_words = MORSE_WORDS_LOOKUP[cur_symbol]
    
    if not good_words:
      return None
      
    # update state
    self.index = (self.index + 1) % len(self.enc_message)

    return random.choice(good_words)
