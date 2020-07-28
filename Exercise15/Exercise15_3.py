import numpy as np
import csv
import scipy.cluster.vq as vq
import matplotlib.pyplot as plt

def plotFigure(matX, matM):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.scatter3D(np.array(matX[0]), np.array(matX[1]), np.array(matX[2]), color='black', alpha=0.1)
    ax.scatter3D(np.array(matM[0]), np.array(matM[1]), np.array(matM[2]), color='red')
    plt.title('k-means plotting')
    plt.savefig('animation/k-means plotting.png')
    plt.show()
    plt.close(fig)

def getStateByPosition(matM, xt):
    minDistance = float("inf")
    b = -1
    for i in range(len(matM)):
        statePosition = np.array(matM[i, :])
        distance = (np.linalg.norm(xt - statePosition)) ** 2
        if distance < minDistance:
            minDistance = distance
            b = i
    return b

def getNumberOfTransitions(start, end, sequence):
    numberOfTransitions = 0
    for i in range(1, len(sequence)):
        if sequence[i] == end and sequence[i-1] == start:
            numberOfTransitions += 1
    return  numberOfTransitions

def getTotalTransition(sequence, numberOfStates):
    totalTransition = [0] * numberOfStates
    for i in range(len(sequence)):
        totalTransition[sequence[i]] += 1
    return totalTransition

with open('q3dm1-path2.csv', 'r') as f:
    reader = csv.reader(f)
    data_as_list = list(reader)
matX = np.array(data_as_list).astype(np.float)

# Clustering
numberOfStates = 10
matM, inds = vq.kmeans2(matX, k=numberOfStates, iter=100, minit='++')

# Plotting input and k-means points
plotFigure(matX.transpose(), matM.transpose())

# Generate sequence of states
sequence = []
for i in range(len(matX)):
    sequence.append(getStateByPosition(matM, matX[i, :]))
print(sequence)

epsilon = 0.1
totalTransition = getTotalTransition(sequence, numberOfStates)
P = [None] * numberOfStates
print('Calculated with epsilon')
for j in range(numberOfStates):
    p_of_i_to_j = [0] * numberOfStates
    for i in range(numberOfStates):
        p_of_i_to_j[i] = ((getNumberOfTransitions(i, j, sequence)+epsilon) / (totalTransition[i]+epsilon))
    P[j] = p_of_i_to_j
    print(p_of_i_to_j)
# print(P)

print('\nCalculated without epsilon')
P2 = [None] * numberOfStates
for j in range(numberOfStates):
    p_of_i_to_j = [0] * numberOfStates
    for i in range(numberOfStates):
        p_of_i_to_j[i] = (getNumberOfTransitions(i, j, sequence) / totalTransition[i])
    p_of_i_to_j = np.round(p_of_i_to_j, 4)
    P2[j] = p_of_i_to_j
    print(p_of_i_to_j)
# print(P2)



