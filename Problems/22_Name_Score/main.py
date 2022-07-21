import enum


def main():
    upperStr = 'A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z'
    upperList = upperStr.split(', ')
    
    characterScore = {}
    for idx, character in enumerate(upperList):
        characterScore[character] = idx + 1
    
    with open('./Problems/22_Name_Score/names.txt', 'r') as f:
        nameStr = f.readline()
    
    nameStr = '(' + nameStr + ')'
    nameList = eval(nameStr)
    nameList = sorted(nameList)
    
    result = 0
    for idx , name in enumerate(nameList):
        sumName = 0
        if name == 'COLIN':
            print(idx)
        for c in name:
            sumName += characterScore[c]
        result += ((idx + 1) * sumName)
    print(result)

if __name__ == "__main__":
    main()