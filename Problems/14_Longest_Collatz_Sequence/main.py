def main():
    maxNum = 1000000
    maxLen = 1
    num = 1
    for i in range(1, maxNum):
        len = 1
        n = i
        while True:
            if n == 1:
                break
            len += 1
            n = n // 2 if n % 2 == 0 else 3 * n + 1
        if len > maxLen:
            maxLen = len
            num = i
    print(maxLen, num)

def f(n: int):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

if __name__ == "__main__":
    main()