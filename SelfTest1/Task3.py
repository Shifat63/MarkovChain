import numpy as np
import numpy.random as rnd

P = np.array(
        [[0.3, 0.2, 0.5],
        [0.5, 0.3, 0.2],
        [0.2, 0.5, 0.3]])

states = ['A', 'B', 'C']
indices = range(len(states))
state2index = dict(zip(states, indices))
index2state = dict(zip(indices, states))

def generateStateSequence(X0, P, tau):
    sseq = [X0]
    iold = state2index[X0]
    for t in range(tau):
        inew = rnd.choice(indices, p=P[:, iold])
        sseq.append(index2state[inew])
        iold = inew
    return sseq

def getNumberOfTransitions(start, end, sequence):
    numberOfTransitions = 0
    for i in range(1, len(sequence)):
        if state2index[sequence[i]] == end and state2index[sequence[i-1]] == start:
            numberOfTransitions += 1
    return  numberOfTransitions

def getTotalTransition(sequence, numberOfStates):
    totalTransition = [0] * numberOfStates
    for i in range(len(sequence)):
        totalTransition[state2index[sequence[i]]] += 1
    return totalTransition

# Generate Sequence
lengthOfEachSequence = 200
logLikelihoodSummation = 0
sequence = generateStateSequence('A', P, (lengthOfEachSequence-1))
print(sequence)

# Calculate the probability matrix of Markov chain producing this sequence
numberOfStates = len(states)
totalTransition = getTotalTransition(sequence, numberOfStates)
P_Calculated = [None] * numberOfStates
for j in range(numberOfStates):
    p_of_i_to_j = [0] * numberOfStates
    for i in range(numberOfStates):
        p_of_i_to_j[i] = round((getNumberOfTransitions(i, j, sequence) / totalTransition[i]), 2)
    P_Calculated[j] = p_of_i_to_j
    print(p_of_i_to_j)