def main():
    nums = []
    with open("Problems/13_Large_Sum/numbers.txt", "r") as f:
        for line in f:
            nums.append(int(line.rstrip()))
    
    print(sum(nums))

if __name__ == "__main__":
    main()