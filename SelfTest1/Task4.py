import numpy as np
import numpy.linalg as la

matP = np.array(
        [[0.3, 0.2, 0.5],
        [0.5, 0.3, 0.2],
        [0.2, 0.5, 0.3]])

m = matP.shape[0]
vecB = np.hstack((np.zeros(m), 1))
matI = np.eye(m)
matA = np.vstack((matI-matP, np.ones(m)))

# My manual process to calculate PI
PI = np.dot(matA.transpose(), matA)
PI = la.inv(PI)
PI = np.dot(PI, matA.transpose())
PI = np.dot(PI, vecB)

# Professor's formula to calculate PI
vecPI = la.lstsq(matA, vecB)[0]

print(vecPI)
print(PI)