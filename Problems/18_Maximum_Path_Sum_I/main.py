def main():
    filePath = "./Problems/18_Maximum_Path_Sum_I/triangle.txt"
    triangle = []
    with open(filePath, 'r') as f:
        for line in f:
            tup = []
            for idx in range(0, len(line), 3):
                tup.append(int(line[idx:idx+2]))
            triangle.append(tup)
    
    N = len(triangle)
    dpPath = triangle.copy()
    for idx, tup in enumerate(reversed(triangle)):
        for j, x in enumerate(tup):
            dpPath[N - 1 - idx][j] = x
            if idx != 0:
                dpPath[N - 1 - idx][j] += max(dpPath[N - idx][j], dpPath[N - idx][j + 1])
    
    print(dpPath[0][0])

if __name__ == "__main__":
    main()