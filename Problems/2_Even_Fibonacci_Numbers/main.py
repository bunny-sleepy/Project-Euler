from cmath import sqrt
import math

def main():
    sqrt5 = math.sqrt(5)
    a_1 = 2 + sqrt5
    a_2 = 2 - sqrt5
    A = (5 + 2 * sqrt5) / 5
    B = (5 - 2 * sqrt5) / 5
    upper_bound = 4e6
    upper_idx = int(math.log(upper_bound, a_1))
    sum = int(A * ((a_1 ** (upper_idx + 1)) - 1) / (a_1 - 1)) + 1
    print(sum)

if __name__ == "__main__":
    main()