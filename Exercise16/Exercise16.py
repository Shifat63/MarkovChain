import numpy as np

tau = np.array([5, 10, 100])

P2 = np.array(
        [[0.25, 0.10, 0.25],
        [0.50, 0.80, 0.50],
        [0.25, 0.10, 0.25]])

states = ['A', 'B', 'C']
indices = range(len(states))
state2index = dict(zip(states, indices))
index2state = dict(zip(indices, states))

# 16.1
print('Exercise 16.1')
for i in range(len(tau)):
    probabilityOfBeingAtB = P2[state2index['B']][state2index['B']]
    likelihood = tau[i] * np.log(probabilityOfBeingAtB) + np.log(1 - probabilityOfBeingAtB)
    print('Likelihood for tau=' +str(tau[i])+ ' is ' +str(likelihood))

# 16.2
print('\n\nExercise 16.2')
for i in range(len(tau)):
    probabilityOfBeingAtB = P2[state2index['B']][state2index['B']]
    probabilityOfGoingCfromB = P2[state2index['C']][state2index['B']]
    likelihood = tau[i] * np.log(probabilityOfBeingAtB) + np.log(probabilityOfGoingCfromB)
    print('Likelihood for tau=' +str(tau[i])+ ' is ' +str(likelihood))


# 16.3
print('\n\nExercise 16.3')
for i in range(len(tau)):
    probabilityOfBeingAtB = P2[state2index['B']][state2index['B']]
    probabilityOfNotGoingAfromB = 1 - P2[state2index['A']][state2index['B']]
    likelihood = tau[i] * np.log(probabilityOfBeingAtB) + np.log(probabilityOfNotGoingAfromB)
    print('Likelihood for tau=' +str(tau[i])+ ' is ' +str(likelihood))