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
        inew = rnd.choice(indices, p=P[:,iold])
        sseq.append(index2state[inew])
        iold = inew
    return sseq

def calculateLogLikelihhodOfSequence(sequence):
    logLikelihhod = 0
    for i in range(len(sequence)-1):
        logLikelihhod += np.log(P[state2index[sequence[i+1]]][state2index[sequence[i]]])
    return logLikelihhod

numberOfSequences = 1000
lengthOfEachSequence = 200
logLikelihoodSummation = 0
for i in range(numberOfSequences):
    sequence = generateStateSequence('A', P, (lengthOfEachSequence-1))
    print(sequence)
    logLikelihhod = calculateLogLikelihhodOfSequence(sequence)
    print('log-likelihood for this sequence = ' + str(logLikelihhod))
    logLikelihoodSummation += logLikelihhod

print('\n Average log-likelihood = ' + str(logLikelihoodSummation/numberOfSequences))
