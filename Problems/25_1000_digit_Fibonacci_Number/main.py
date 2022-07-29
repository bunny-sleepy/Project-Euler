def main():
    f = [1, 1]
    while 1:
        if len(str(f[-1])) >= 1000:
            break
        f.append(f[-1] + f[-2])
    print(len(f))

if __name__ == "__main__":
    main()