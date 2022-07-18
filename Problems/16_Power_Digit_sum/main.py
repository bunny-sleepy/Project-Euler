def main():
    base = 2
    power = 1000

    num = str(base ** power)
    result = 0
    for c in num:
        result += int(c)
    print(result)

if __name__ == "__main__":
    main()