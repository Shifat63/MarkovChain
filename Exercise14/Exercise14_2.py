import numpy as np
import numpy.random as rnd

states = ['A', 'B', 'C']
indices = range(len(states))
occurence = [0] * len(states)

state2index = dict(zip(states, indices))
index2state = dict(zip(indices, states))
stateOccurences = dict(zip(states, occurence))

def generateStateSequence(X0, P, tau):
    sseq = [X0]
    iold = state2index[X0]
    for t in range(tau):
        inew = rnd.choice(indices, p=P[:,iold])
        sseq.append(index2state[inew])
        iold = inew
    return sseq

P1 = np.array(
    [[0.30, 0.20, 0.50],
    [0.50, 0.30, 0.20],
    [0.20, 0.50, 0.30]])

P2 = np.array(
        [[0.25, 0.10, 0.25],
        [0.50, 0.80, 0.50],
        [0.25, 0.10, 0.25]])

numberOfSequences = 10000

# sequenceArray = [None] * numberOfSequences
for i in range(numberOfSequences):
    sequence = generateStateSequence('B', P2, 9)
    stateOccurences[sequence[-1]] += 1
    # sequenceArray[i] = sequence

# print(sequenceArray)

maxLikelyProbability = 0
likeliestLatElement = None
for i in indices:
    probability = stateOccurences[index2state[i]] / numberOfSequences
    print('Probability that ' + str(index2state[i]) + ' is the empirically likely last element = ' + str(probability))
    if probability > maxLikelyProbability:
        maxLikelyProbability = probability
        likeliestLatElement = index2state[i]

print('Empirically likeliest last element is ' + str(likeliestLatElement))