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


with open("hmm2_01.in", "r") as inputs:
    i = 0
    for line in inputs:
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
    
    vit = [{}] 
    path = {}
    # Initialize base cases (t == 0)
    for s in range(len(pi[0])):
        vit[0][s] = pi[0][s] * B[s][obs[0]]
        path[s] = [s]
    for t in range(1, len(obs)):
        vit.append({})
        newpath = {}   
        for y in range(num_state):
            (prob, state) = max((vit[t-1][y0] * A[y0][y] * B[y][obs[t]], y0) for y0 in range(num_state))
            vit[t][y] = prob
            newpath[y] = path[state] + [y] # y is the index of current state, path[state] is the best path to reach current state
        path = newpath
    n = 0
    if len(obs)!=1:
        n = t
    (prob, state) = max((vit[n][y], y) for y in range(num_state))
    print(vit)
    print(path)
    # In the end path will be {0:[path 0],1:[path 1],2:[path 2],3:[path 3]} 
    # each indicating to reach state i what is the path before i and the last value of path[i] will be i (itself)

    #print(' '.join(map(str, path[state])))
