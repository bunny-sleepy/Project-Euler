def main():
    n = 20
    # compute \binom{2n}{n}
    result = 1
    for i in range(n):
        result = result * (n + 1 + i)
    for i in range(n):
        result = result // (1 + i)
    print(result)

if __name__ == "__main__":
    main()