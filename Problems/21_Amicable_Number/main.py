def d(num: int):
    num_cache = num
    
    numDivisors = {}
    divisorList = []
    
    if num % 2 == 0:
        numDivisors[2] = 0
        divisorList.append(2)
    while num % 2 == 0:
        numDivisors[2] = numDivisors[2] + 1
        num = num // 2
    
    current_p = 3
    while True:
        if num % current_p == 0:
            numDivisors[current_p] = 0
            divisorList.append(current_p)
        while num % current_p == 0:
            numDivisors[current_p] = numDivisors[current_p] + 1
            num = num // current_p
        if current_p * current_p > num_cache:
            break
        if current_p > num:
            break
        current_p += 2
    
    if num > 1:
        numDivisors[num] = 1
        divisorList.append(num)
    
    result = 1
    for p in divisorList:
        k = sum([p**i for i in range(numDivisors[p] + 1)])
        result *= k
    return result - num_cache

def main():
    bound = 10000
    dList = [d(n) for n in range(1, bound + 1)]
    ans = 0
    for k in range(1, bound + 1):
        if dList[k - 1] <= bound and dList[k - 1] != k and dList[dList[k - 1] - 1] == k:
            print(k, dList[k - 1])
            ans += k
    print(ans)

if __name__ == "__main__":
    main()