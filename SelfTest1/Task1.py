import numpy as np

P2 = np.array(
        [[0.3, 0.2, 0.5],
        [0.5, 0.3, 0.2],
        [0.2, 0.5, 0.3]])

states = ['A', 'B', 'C']
indices = range(len(states))
state2index = dict(zip(states, indices))
index2state = dict(zip(indices, states))

print('For E1')
p = P2[state2index['B']][state2index['C']] * P2[state2index['A']][state2index['B']]
likelihood = np.log(p)
print('p(E1)=%.2f' % p)
print('L(E1)=%.2f' % likelihood)

print('\nFor E2')
p = P2[state2index['A']][state2index['C']] * P2[state2index['B']][state2index['A']]
likelihood = np.log(p)
print('p(E2)=%.2f' % p)
print('L(E2)=%.2f' % likelihood)