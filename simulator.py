from __future__ import print_function
from collections import defaultdict

import json
import random

from utils import NTHS, NUMS, WORDS

from auto_acronym import AutoAcronym
from anagram_path import AnagramPath
from directions import Directions
from middle_bigrams import MiddleBigrams
from pi_digits import PiDigits
# from last_letter import LastLetter
# from morse_code import MorseCode
# from vowel_binary import VowelBinary


METAANSWER = 'HIREACONTRACTOR'
GEN_LENGTH = 10**5

PUZZLE_NAMES = {
  'A': 'Cafe Five',
  'B': 'Unchained',
  'C': 'Make Your Own Word Search',
  'D': 'Library of Images',
  'E': 'Infinite Corridor Simulator'
}

START_MESSAGE = 'DECODEEACHPUZZLE'

# generating puzzles

def make_puzzle(metaanswer, 
                metaoffset=None,
                breadcrumb=False,
                verbose=False):
  if metaoffset is None:
    metaoffset = random.randint(10000, GEN_LENGTH)

  digits = list(map(int, str(metaoffset)))
  messages = [
    NTHS[i] + NUMS[digits[i]] for i in range(5)
  ]
  random.shuffle(messages)

  generators = {
    'A': AnagramPath(messages[0]),
    'B': MiddleBigrams(messages[1]),
    'C': Directions(messages[2]),
    'D': PiDigits(messages[3]),
    'E': AutoAcronym(messages[4])
  }

  priorities = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': -3}

  answers = []
  for t in range(GEN_LENGTH):
    sorted_priorities = sorted(priorities.items(), 
                               key=lambda x: x[1] + random.randint(0, 3),
                               reverse=True)
    first_letter = None
    if t < len(START_MESSAGE):
      first_letter = START_MESSAGE[t]
    
    found = False
    for i in range(5):
      name, _ = sorted_priorities[i]
      word = generators[name].generate(first_letter)
      
      if word:
        answers.append((name, word))
        found = True
        
        # update priorities
        for k in priorities:
          priorities[k] += 1
        priorities[name] = 0
        
        break
    
    if not found:
      raise Exception('Error: failed to generate puzzle')

  # add final answer

  if breadcrumb:
    answers[metaoffset - 2] = ('D', 'ANSWER')
    answers[metaoffset] = ('A', 'ANSWER')
  
  answers[metaoffset - 1] = ('E', metaanswer)

  # display answers
  if verbose:
    for t, entry in enumerate(answers):
      name, word = entry
      puzzle_name = PUZZLE_NAMES[name]
      print('Puzzle {} ({}),\t{}'.format(t+1, puzzle_name, word))

  output = [(t+1, entry[0], entry[1]) for t, entry in enumerate(answers)]
  return output

def generate_data(puzzle_id, 
                  puzzle_answer, 
                  fname=None):
  random.seed(puzzle_id)

  if fname is None:
    return json.dumps(make_puzzle(puzzle_answer))
  else:
    json.dump(make_puzzle(puzzle_answer), open(fname, 'w'))


if __name__ == '__main__':
  # generate_data(17, 'RAISE', fname='infinite_tests/json/simulator17.json')
  make_puzzle(METAANSWER, verbose=True)