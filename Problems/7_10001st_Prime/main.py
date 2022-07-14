from math import log
import time

def main():
    idx = 10001
    n = 2
    primeList = []
    searchRange = int(idx * log(idx, 2))
    isPrimeMap = [0] * searchRange
    while len(primeList) < idx:
        if isPrimeMap[n] == 0:
            primeList.append(n)
        for p in primeList:
            if n * p >= searchRange:
                break
            isPrimeMap[n * p] = 1
            if n % p == 0 and n != p:
                break
        n += 1
    print(primeList[-1])

if __name__ == "__main__":
    main()