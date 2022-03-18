import random

from utils import NTHS, NUMS, WORDS

EVEN_WORDS = [word for word in WORDS if len(word) % 2 == 0]

def get_bigram_words(bigram):
    return [word for word in EVEN_WORDS if word[len(word)//2-1:len(word)//2+1] == bigram and len(word) > 2]

def get_bigrams(word):
    return [word[i-1:i+1] for i in range(1, len(word))]

def random_bigram(word):
    ind = random.randint(1, len(word)-1)
    return word[ind-1:ind+1]

BIGRAMS = set()
for word in NTHS + NUMS:
    for bigram in get_bigrams(word):
        BIGRAMS.add(bigram)

BIGRAM_LOOKUP = {
    bigram: get_bigram_words(bigram) for bigram in BIGRAMS
}

def parse_message(message):
    for nth in NTHS:
        if message.startswith(nth):
            return nth, message[len(nth):]

class MiddleBigrams:
  def __init__(self, message):
    self.message = message
    self.nth, self.num = parse_message(message)
    self.index = 0
  
  def generate(self, first_letter=None):
    cur_word = self.nth if self.index == 0 else self.num

    if first_letter is not None:
      good_words = []
      for bigram in get_bigrams(cur_word):
        good_words += [word for word in BIGRAM_LOOKUP[bigram] if word[0] == first_letter]
    else:
      bigram = random_bigram(cur_word)  
      good_words = BIGRAM_LOOKUP[bigram]
    
    if not good_words:
      return None
      
    # update state
    self.index ^= 1
    
    return random.choice(good_words)
