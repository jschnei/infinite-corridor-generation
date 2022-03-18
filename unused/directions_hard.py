import random

from utils import WORDS, WORDS_BY_LENGTH_AND_START

DIR_LETTERS = {
    'A': 'dddddddduuuurrrrrrdddduuuuuuuullllllrrrrrrrrr',
    'B': 'ddddddddrrrrrruuuullllllrrrrrruuuullllllrrrrrrrrr',
    'C': 'ddddddddrrrrrrlllllluuuuuuuurrrrrrrrr',
    'D': 'ddddddddrrrruuuuuuuullllrrrrrrr',
    'E': 'ddddddddrrrrrrlllllluuuurrrrrrlllllluuuurrrrrrrrr',
    'F': 'dddddddduuuurrrllluuuurrrrrrrrr',
    'G': 'ddddddddrrrrrruuuulllrrrddddlllllluuuuuuuurrrrrrrrr',
    'H': 'dddddddduuuurrrrrrdddduuuuuuuurrr',
    'I': 'dddddddduuuuuuuurrr',
    'J': 'rrrddddddddlllrrruuuuuuuurrrrrr',
    'K': 'dddddddduuuurrrddddrrrllluuuuuuuurrrrrr',
    'L': 'ddddddddrrrrrruuuurrruuuu',
    'M': 'dddddddduuuuuuuurrrdddddddduuuuuuuurrrdddddddduuuuuuuurrr',
    'N': 'dddddddduuuuuuuurrrddddrrrdddduuuuuuuurrr',
    'O': 'ddddddddrrrrrruuuuuuuullllllrrrrrrrrr',
    'P': 'dddddddduuuurrrrrruuuullllllrrrrrrrrr',
    'Q': 'ddddrrrrrrdddduuuuuuuullllllrrrrrrrrr',
    'R': 'dddddddduuuurrrddddrrrllluuuurrruuuullllllrrrrrrrrr',
    'S': 'ddddrrrrrrddddllllllrrrrrruuuulllllluuuurrrrrrrrr',
    'T': 'rrrdddddddduuuuuuuurrrrrr',
    'U': 'ddddddddrrrrrruuuuuuuurrr',
    'V': 'ddddrrrddddrrruuuuuuuurrr',
    'W': 'ddddddddrrruuuuuuuuddddddddrrruuuuuuuurrr',
    'X': 'rrrddddddddlllrrrrrrllluuuuuuuurrrrrr',
    'Y': 'ddddrrrdddduuuurrruuuurrr',
    'Z': 'rrrrrrddddllllllddddrrrrrrlllllluuuurrrrrruuuurrr'
}

def encode_directions(message):
  expanded = ''.join(DIR_LETTERS[c] for c in message)
  chunks = []
  
  cur_c = expanded[0]
  cur_run = 1

  for c in expanded[1:]:
    if c == cur_c:
      cur_run += 1
    else:
      chunks.append((cur_run, cur_c.upper()))
      cur_run = 1
      cur_c = c
  chunks.append((cur_run, cur_c.upper()))

  return chunks

class Directions:
  def __init__(self, message):
    self.message = message
    self.enc_message = encode_directions(message)
    self.index = 0
  
  def generate(self, first_letter=None):
    cur_run, cur_c = self.enc_message[self.index]
    
    if first_letter is not None and first_letter != cur_c:
      return None
    

    good_words = WORDS_BY_LENGTH_AND_START[(cur_run, cur_c)]
    
    if not good_words:
      return None
      
    # update state
    self.index = (self.index + 1) % len(self.enc_message)

    return random.choice(good_words)

blah = []
for k in DIR_LETTERS:
  for pr in encode_directions(k):
    blah.append(pr)

print(sorted(list(set(blah))))

# generator = Directions("FIRSTSEVEN")
# for _ in range(100):
#   print(generator.generate())