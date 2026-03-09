import numpy as np

v = np.array([2, 3])
w = np.array([4, 1])
print ("v = ", v, "w = ", w)

add = v + w
sub = v - w
print("Added Vectors = ", add, "Subracted Vectors = ", sub)

mult = np.multiply(4 , ([1, 2]))
print("Scalor multiplied by vector = ", mult)

dot = np.dot(v, w)
print("Dot = ", dot)

magnitude = np.linalg.norm(v)
print("Magnitude = ", magnitude)

A = [[2, 0], [1, 3]]
vector = [1, 2]
A_mult_vector = np.multiply(A, vector)
print("Matrix Transformation = ", A_mult_vector)

det = np.linalg.det(A)
print(det)

