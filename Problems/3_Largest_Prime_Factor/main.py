def main():
    num = 600851475143
    max_p = 1
    num_cache = num
    
    while num % 2 == 0:
        max_p = 2
        num = num // 2
    
    current_p = 3
    while True:
        while num % current_p == 0:
            max_p = current_p
            num = num // current_p
        if current_p * current_p >= num_cache:
            max_p = num
            break
        if current_p > num:
            break
        current_p += 2
    
    print(max_p)

if __name__ == "__main__":
    main()