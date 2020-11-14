import sys
def zeros_matrix(rows, cols):
    """
    Creates a matrix filled with zeros.
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have
 
        :return: list of lists that form the matrix
    """
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
 
    return M

def copy_matrix(M):
    """
    Creates and returns a copy of a matrix.
        :param M: The matrix to be copied
 
        :return: A copy of the given matrix
    """
    # Section 1: Get matrix dimensions
    rows = len(M)
    cols = len(M[0])
 
    # Section 2: Create a new matrix of zeros
    MC = zeros_matrix(rows, cols)
 
    # Section 3: Copy values of M into the copy
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]
 
    return MC



i = 0
for line in sys.stdin:
    if i<3:
        line = line.split()
        row = int(line[0])
        col = int(line[1])
        line = line[2:]
        m = zeros_matrix(row, col)
        r = 0
        c = 0
        for item in line:
            if c == col:
                c = 0
                r = r+1
            m[r][c] = float(item)
            c = c+1
        if i == 0:
            num_state = row
            A = m
        elif i == 1:
            B = m
        else:
            pi = m
    else:
        line = line.split()
        num_seq = int(line[0])
        line = line[1:]
        obs = []
        for oi in line:
            obs.append(int(oi))
    
    i = i+1

fwd = [{}] 
# Initialize base cases (t == 0)
for i in range(len(pi[0])):
    fwd[0][i] = pi[0][i] * B[i][obs[0]]
for t in range(1, len(obs)):
    fwd.append({})     
    for y in range(num_state):
        fwd[t][y] = sum((fwd[t-1][y0] * A[y0][y] * B[y][obs[t]]) for y0 in range(num_state))
prob = sum((fwd[len(obs) - 1][s]) for s in range(num_state))
#ans = str(prob)
print(prob)
