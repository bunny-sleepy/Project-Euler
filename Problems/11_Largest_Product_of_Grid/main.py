def main():
    consecutiveNumber = 4
    M = []
    
    with open("./mat.txt", "r") as f:
        for line in f:
            tup = []
            for idx in range(0, len(line), 3):
                tup.append(int(line[idx:idx+2]))
            M.append(tup)
    maxProduct = 0
    # row
    for rowIdx in range(len(M)):
        for i in range(len(M[0]) - consecutiveNumber + 1):
            product = 1
            for j in range(consecutiveNumber):
                product = product * M[rowIdx][i + j]
            if product > maxProduct:
                maxProduct = product
    # column
    for colIdx in range(len(M[0])):
        for i in range(len(M) - consecutiveNumber + 1):
            product = 1
            for j in range(consecutiveNumber):
                product = product * M[i + j][colIdx]
            if product > maxProduct:
                maxProduct = product
    # anti-diagonal
    for rowIdx in range(len(M)):
        if len(M) - rowIdx < consecutiveNumber:
            continue
        for i in range(len(M) - rowIdx - consecutiveNumber + 1):
            product = 1
            for j in range(consecutiveNumber):
                product = product * M[rowIdx + i + j][i + j]
            if product > maxProduct:
                maxProduct = product
    for colIdx in range(len(M[0])):
        if len(M[0]) - colIdx < consecutiveNumber:
            continue
        for i in range(len(M[0]) - colIdx - consecutiveNumber + 1):
            product = 1
            for j in range(consecutiveNumber):
                product = product * M[i + j][colIdx + i + j]
            if product > maxProduct:
                maxProduct = product
    # diagonal
    M_ = []
    for i in range(len(M)):
        M_.append(M[len(M) - 1 - i])
    for rowIdx in range(len(M_)):
        if len(M_) - rowIdx < consecutiveNumber:
            continue
        for i in range(len(M_) - rowIdx - consecutiveNumber + 1):
            product = 1
            for j in range(consecutiveNumber):
                product = product * M_[rowIdx + i + j][i + j]
            if product > maxProduct:
                maxProduct = product
    for colIdx in range(len(M_[0])):
        if len(M_[0]) - colIdx < consecutiveNumber:
            continue
        for i in range(len(M_[0]) - colIdx - consecutiveNumber + 1):
            product = 1
            for j in range(consecutiveNumber):
                product = product * M_[i + j][colIdx + i + j]
            if product > maxProduct:
                maxProduct = product
    print(maxProduct)

if __name__ == "__main__":
    main()