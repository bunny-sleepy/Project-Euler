from re import M


def main():
    result = 0
    digitDict = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }
    
    tensDict = {
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
    }
    
    digitTensDict = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'
    }
    
    hundredStr = 'hundred'
    andStr = 'and'
    
    for i in range(1, 1000):
        if i // 100 > 0:
            result += len(digitDict[i // 100])
            result += len(hundredStr)
            if i % 100 != 0:
                result += len(andStr)
        if i % 100 == 0:
            pass
        elif i % 100 < 10:
            result += len(digitDict[i % 100])
        elif i % 100 < 20:
            result += len(tensDict[i % 100])
        else:
            result += len(digitTensDict[(i % 100) // 10])
            if i % 10 != 0:
                result += len(digitDict[i % 10])
    
    result += len('thousand')
    result += 3
    print(result)

if __name__ == "__main__":
    main()