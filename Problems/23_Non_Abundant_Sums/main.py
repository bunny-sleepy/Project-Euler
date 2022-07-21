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
    bound = 28123
    
    abundantList = []
    for n in range(1, bound + 1):
        if n < d(n):
            abundantList.append(n)
    print(abundantList)
    abundantMap = [1] * (bound + 1)
    
    for i in abundantList:
        for j in abundantList:
            if i + j <= bound:
                abundantMap[i + j] = 0
    
    print(sum([idx * n for idx, n in enumerate(abundantMap)]))

if __name__ == "__main__":
    main()