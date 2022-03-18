from collections import defaultdict

WORDLIST = 'wordlists/final.txt'
WORDS = list(set([line.strip().upper() for line in open(WORDLIST, 'r')]))

WORDS_BY_LENGTH_AND_START = defaultdict(list)

for word in WORDS:
  WORDS_BY_LENGTH_AND_START[(len(word), word[0])].append(word)
  WORDS_BY_LENGTH_AND_START[(len(word), '*')].append(word)
  WORDS_BY_LENGTH_AND_START[('*', word[0])].append(word)

NTHS = [
  "FIRST",
  "SECOND",
  "THIRD",
  "FOURTH",
  "FIFTH"
]

NUMS = [
  "ZERO",
  "ONE",
  "TWO",
  "THREE",
  "FOUR",
  "FIVE",
  "SIX",
  "SEVEN",
  "EIGHT",
  "NINE"
]
