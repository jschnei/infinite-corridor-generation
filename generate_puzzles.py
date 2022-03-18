import json
from simulator import generate_data

RESERVED = []

def generate_puzzles(fpath, tag, cutoff=10**5, verbose=False):
    puzzles = json.load(open(fpath))
    for puzzle in puzzles:
        t, puzzle_tag, answer = puzzle
        if t > cutoff:
            break

        if t in RESERVED:
            continue

        if puzzle_tag == tag:
            print("Generating Puzzle {}...".format(t))
            generate_data(t, answer, fname='generated/simulator{}.json'.format(t))
        


if __name__ == '__main__':
    generate_puzzles('../supermeta.json', 'E', cutoff=100, verbose=True)