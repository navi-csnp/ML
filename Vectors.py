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
A_mult_vector = np.multiply(A, vector) #This is an element-wise multiplication and not matrix based multiplication
print("Matrix Transformation = ", A_mult_vector)

det = np.linalg.det(A)
print(det)

A_dot_vector = np.dot(A, vector) #This is the matrix multiplication and this tranforms the linear data
print("Matrix Dot Product = ", A_dot_vector)

#solve for AX = vector
solve = np.linalg.solve(A, vector)
print("X = ", solve)

inv = np.linalg.inv(A)
print("Inverse of A = ", inv)

v1 = [1, 2]
v2 = [1, 4]
rank = np.linalg.matrix_rank([v1, v2]) #In a matrix, the rank determines the max number of linearly independent row vectors or column vectors
print("Linear Independence or Dependent? = ", rank)



#1. Take unit square
#2. Transform all its corners
#3. Compute area before & after

B = np.array([[2, 1], [0, 1]])
unit_square = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
transformed = np.array([B @ s for s in unit_square])

print("Original square = ", unit_square)
print("Transformed square = ", transformed)

def polygon_area(points):
    x = points[:, 0] #extract 1st column
    y = points[:, 1] #extract 2nd column
    return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1))) #shoelace formula

area_before = polygon_area(unit_square)
area_after = polygon_area(transformed)
det = np.linalg.det(B)

isArea = np.isclose(area_after, area_before * det) 
print("Is Area After == Area Before * Det? = ", isArea)

#Projection of Vector
v = np.array([3, 4])
u = np.array([1, 0])
proj = (np.dot(v, u) / np.dot(u, u)) * u
print("Projection of v onto u = ", proj)


#EigenValues & EigenVectors
C = np.array([[2, 0], [0, 3]])
eigVals, eigVecs = np.linalg.eig(C)
print("Eigen values, Eigen Vectors= ", eigVals, eigVecs)

v = eigVecs[:, 0]
lam = eigVals[0]

#verify eigenvector
print("Verifying Eigen Vector = ", np.allclose(C @ v, lam * v))

#Detect collapse (Det = 0)
D = np.array([[2, 4], [1, 2]])
det = np.linalg.det(D)
print("Det = ", det)
print("Dependent vectors = ", C @ D)