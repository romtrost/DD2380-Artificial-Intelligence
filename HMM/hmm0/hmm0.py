import sys

# Creates a matrix of size rows x columns
def createMatrix(data, rows, columns):
    return [data[i:i+columns] for i in range(0, len(data), columns)]

# Matrix multiplication
def multiplyMatrices(A, B):
    return [[sum(a*b for a,b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

# Turns matrix of strings into floats
def stringToFloat(A):
    for i in range(0, len(A)):
        A[i] = float(A[i])
    return A

# Gets input from console and seperates them by line, then turns their values into floats
A_in = stringToFloat(sys.stdin.readline().split())
B_in = stringToFloat(sys.stdin.readline().split())
Pi_in = stringToFloat(sys.stdin.readline().split())
#print("A_in:", A_in)
#print("B_in:", B_in)
#print("Pi_in:", Pi_in)

# Creates matrices A, B and Pi
A_matrix = createMatrix(A_in[2:], int(A_in[0]), int(A_in[1]))
B_matrix = createMatrix(B_in[2:], int(B_in[0]), int(B_in[1]))
Pi_matrix = createMatrix(Pi_in[2:], int(Pi_in[0]), int(Pi_in[1]))
#print("A_matrix:", A_matrix)
#print("B_matrix:", B_matrix)
#print("Pi_matrix:", Pi_matrix)

# Multiplication of matrices
Pi_A = multiplyMatrices(Pi_matrix, A_matrix)
Pi_A_B = multiplyMatrices(Pi_A, B_matrix)
#print("Pi_A_B:", Pi_A_B)

dims = [str(len(Pi_A_B)), str(len(Pi_A_B[0]))]   # Getting row and column (dimensions) of Pi_A_B
Pi_A_B = [str(round(data, 6)) for row in Pi_A_B for data in row] # Rounding Pi_A_B to 1 decimal point + returning its values to strings
#print("dims:", dims)
#print("Pi_A_B:", Pi_A_B)

# Putting in correct format
dims = ' '.join(dims)
Pi_A_B = ' '.join(Pi_A_B)
#print("dims:", dims)
#print("Pi_A_B:", Pi_A_B)

# Output
output = dims + ' ' + Pi_A_B
print(outputz)






