def main():
    int_3 = 3
    int_5 = 5
    upper_bound = 1000
    sum = 0
    for i in range(upper_bound):
        if i % int_3 == 0 or i % int_5 == 0:
            sum += i
    print(sum)

if __name__ == "__main__":
    main()