def main():
    n = 2
    primeList = []
    searchRange = int(2e6)
    isPrimeMap = [0] * (searchRange + 1)
    while n <= searchRange:
        if isPrimeMap[n] == 0:
            primeList.append(n)
        for p in primeList:
            if n * p > searchRange:
                break
            isPrimeMap[n * p] = 1
            if n % p == 0 and n != p:
                break
        n += 1
    
    print(sum(primeList))

if __name__ == "__main__":
    main()