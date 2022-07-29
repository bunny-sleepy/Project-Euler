def main():
    searchRange = 1000
    maxLen = 1
    maxLenNum = 1
    for num in range(1, searchRange):
        if num % 2 == 0 or num % 5 == 0:
            continue
        currentReciprocalCycleLen = reciprocalCycleLen(num)
        if maxLen < currentReciprocalCycleLen:
            maxLen = currentReciprocalCycleLen
            maxLenNum = num
    print(maxLen, maxLenNum)

def reciprocalCycleLen(num):
    str_9 = '9'
    while 1:
        if int(str_9) % num == 0:
            break
        str_9 = f"{str_9}9"
    return len(str_9)

if __name__ == "__main__":
    main()