def main():
    threshold = 500
    n = 7
    while True:
        k = n * (n + 1) // 2
        if numDivisors(k) > threshold:
            print(n, k)
            break
        n = n + 1

def numDivisors(num):
    max_p = 1
    num_cache = num
    
    numDivisors = {}
    divisorList = []
    
    if num % 2 == 0:
        numDivisors[2] = 0
        divisorList.append(2)
    while num % 2 == 0:
        numDivisors[2] = numDivisors[2] + 1
        max_p = 2
        num = num // 2
    
    current_p = 3
    while True:
        if num % current_p == 0:
            numDivisors[current_p] = 0
            divisorList.append(current_p)
        while num % current_p == 0:
            numDivisors[current_p] = numDivisors[current_p] + 1
            max_p = current_p
            num = num // current_p
        if current_p * current_p > num_cache:
            max_p = num
            break
        if current_p > num:
            break
        current_p += 2
    
    if num > 1:
        numDivisors[num] = 1
        divisorList.append(num)
    
    result = 1
    for divisor in divisorList:
        result = result * (numDivisors[divisor] + 1)
    return result

if __name__ == "__main__":
    main()