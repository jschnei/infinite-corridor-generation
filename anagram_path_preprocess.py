import itertools
import pickle
import random

from collections import defaultdict, deque

from utils import NTHS, NUMS, WORDS

def anagram_sig(word):
    return ''.join(sorted(word))

ANAGRAM_LOOKUP = defaultdict(list)
for word in WORDS:
    ANAGRAM_LOOKUP[anagram_sig(word)].append(word)

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_edges(word):
    N = len(word)
    ans = {c : set() for c in ALPHABET}

    for l1 in range(3, N//2):
        for inds1 in itertools.combinations(range(N), l1):
            inds = list(inds1)
            w1 = anagram_sig(''.join(word[i] for i in inds1))
            if w1 in ANAGRAM_LOOKUP:
                inds2 = [i for i in range(N) if i not in inds1]
                for j in inds2:
                    w2 = anagram_sig(''.join(word[i] for i in inds2 if i != j))
                    if w2 in ANAGRAM_LOOKUP:
                        ans[word[j]].add((w1, w2))

    return ans

GRAPH = defaultdict(lambda: {c : set() for c in ALPHABET})

print("Building GRAPH...")
for sig in ANAGRAM_LOOKUP:
    edges = get_edges(sig)
    for c in ALPHABET:
        for w1, w2 in edges[c]:
            GRAPH[w1][c].add(w2)
            GRAPH[w2][c].add(w1)
print("Done building graph.")

def layer_graph(message):
    layered_graph = defaultdict(set)
    layered_graph_rev = defaultdict(set)
    M = len(message)
    for i, c in enumerate(message):
        for v in GRAPH:
            for w in GRAPH[v][c]:
                layered_graph[(v, i)].add((w, (i+1) % M))
                layered_graph_rev[(w, (i+1) % M)].add((v, i))
    
    # trim graph
    outdegrees = dict()
    for vx in layered_graph:
        outdegrees[vx] = len(layered_graph[vx])
    for vx in layered_graph_rev:
        outdegrees[vx] = len(layered_graph[vx])
    
    removal_queue = deque()

    for vx in outdegrees:
        if outdegrees[vx] == 0:
            removal_queue.append(vx)
    
    while removal_queue:
        vx = removal_queue.popleft()
        for nbr in layered_graph_rev[vx]:
            layered_graph[nbr].remove(vx)
            outdegrees[nbr] -= 1
            if outdegrees[nbr] == 0:
                removal_queue.append(nbr)
        layered_graph.pop(vx)
    
    return layered_graph

MESSAGES = [nth + num for nth in NTHS for num in NUMS]

for message in MESSAGES:
    message_graph = layer_graph(message)
    print(message, len(message_graph))
    pickle.dump(dict(message_graph),
                open('anagram_path_preprocess/{}.pkl'.format(message.lower()), 'wb'))


