def permutationAtPosition(n: int, orderList: list):
    numItem = len(orderList)
    if numItem == 1:
        return orderList
    
    numPermutation = 1
    for i in range(1, numItem):
        numPermutation *= i
    
    idx = n // numPermutation
    r = n % numPermutation
    newOrderList = []
    for i, item in enumerate(orderList):
        if i != idx:
            newOrderList.append(item)
    result = [orderList[idx]]

    a = permutationAtPosition(r, newOrderList)
    result.extend(a)
    return result

def main():
    print(permutationAtPosition(999999, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

if __name__ == "__main__":
    main()