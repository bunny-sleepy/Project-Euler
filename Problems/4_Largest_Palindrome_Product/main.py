def main():
    maxPalindrome = 0
    for a in range(100, 1000):
        for b in range(110, 1000, 11):
            x = a * b
            if isPalindrome(x):
                if x > maxPalindrome:
                    maxPalindrome = x
    print(maxPalindrome)
            
def isPalindrome(x: int):
    a = str(x)
    if len(a) == 0:
        return True
    if len(a) % 2 == 0:
        a1 = a[:len(a) // 2]
        a2 = a[len(a) // 2:]
        a2 = a2[::-1]
        return a1 == a2
    else:
        a1 = a[:len(a) // 2]
        a2 = a[len(a)//2 + 1:]
        a2 = a2[::-1]
        return a1 == a2

if __name__ == "__main__":
    main()