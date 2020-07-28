import numpy as np
import numpy.linalg as la

def calculate_pi_t(pi_0, t, P):
    P_tMinus1 = P
    for i in range(t-1):
        P_tMinus1 = np.dot(P_tMinus1, P)
    return np.dot(P_tMinus1, pi_0)

P1 = np.array(
    [[0.30, 0.20, 0.50],
    [0.50, 0.30, 0.20],
    [0.20, 0.50, 0.30]])

P2 = np.array(
        [[0.25, 0.10, 0.25],
        [0.50, 0.80, 0.50],
        [0.25, 0.10, 0.25]])

t = np.array([1, 2, 4, 8, 16])


# Start from state A
pi_0 = np.array(
        [[1],
        [0],
        [0]])
print('pi[0] = ')
print(pi_0)
print('')
for i in range(len(t)):
    print('pi[' + str(t[i]) + '] = ')
    print(calculate_pi_t(pi_0, t[i], P1))
    print('')
print('\n\n')


# Start from state B
# pi_0 = np.array(
#         [[0],
#         [1],
#         [0]])
# print('pi[0] = ')
# print(pi_0)
# print('')
# for i in range(len(t)):
#     print('pi[' + str(t[i]) + '] = ')
#     print(calculate_pi_t(pi_0, t[i], P2))
#     print('')
# print('\n\n')


# Start from state C
# pi_0 = np.array(
#         [[0],
#         [0],
#         [1]])
# print('pi[0] = ')
# print(pi_0)
# print('')
# for i in range(len(t)):
#     print('pi[' + str(t[i]) + '] = ')
#     print(calculate_pi_t(pi_0, t[i], P1))
#     print('')

evals1, evecs1 = la.eig(P1)
print('Eigenvalue of P1')
print(evals1)
print('Eigenvector of P1')
print(evecs1)
spectralDecomposition1 = np.dot(evecs1, np.dot(P1, evecs1.transpose()))
print('Spectral decomposition of P1')
print(spectralDecomposition1)

evals2, evecs2 = la.eig(P2)
print('\nEigenvalue of P2')
print(evals2)
print('Eigenvector of P2')
print(evecs2)
spectralDecomposition2 = np.dot(evecs2, np.dot(P2, evecs2.transpose()))
print('Spectral decomposition of P2')
print(spectralDecomposition2)