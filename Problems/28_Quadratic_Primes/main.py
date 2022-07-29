def main():
    searchRange = 1000
    bList = primeList(searchRange)
    allPrimes = primeList(2 * searchRange * searchRange + searchRange)
    allPrimes = set(allPrimes)
    maxLen, max_a, max_b = 0, 0, 0
    for a in range(-searchRange + 1, searchRange):
        for b in bList:
            n = 0
            while 1:
                if f(a, b, n) not in allPrimes:
                    break
                n += 1
            if n > maxLen:
                maxLen, max_a, max_b = n, a, b
    print(maxLen, max_a, max_b, max_a * max_b)
            

def f(a, b, n):
    return n ** 2 + a * n + b

def primeList(searchRange: int) -> list:
    primeList = []
    isPrimeMap = [0] * (searchRange + 1)
    n = 2
    while n <= searchRange:
        if isPrimeMap[n] == 0:
            primeList.append(n)
        for p in primeList:
            if n * p >= searchRange:
                break
            isPrimeMap[n * p] = 1
            if n % p == 0 and n != p:
                break
        n += 1
    return primeList

if __name__ == "__main__":
    main()