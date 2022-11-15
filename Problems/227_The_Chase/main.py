import numpy as np

def main():
    # num players
    n = 100
    # state transition matrix
    # A[i, j] is prob. that i transit to j
    A = np.zeros((n // 2 + 1, n // 2 + 1), dtype=np.float64)
    A[0][0] = np.float64(1)
    A[1][1] = np.float64(0.5 + 1 / 36)
    A[1][0] = np.float64(2 / 9)
    A[1][2] = np.float64(2 / 9)
    A[1][3] = np.float64(1 / 36)
    A[n // 2 - 1][n // 2 - 1] = np.float64(0.5 + 1 / 36)
    A[n // 2 - 1][n // 2 - 2] = np.float64(2 / 9)
    A[n // 2 - 1][n // 2 - 3] = np.float64(1 / 36)
    A[n // 2 - 1][n // 2] = np.float64(2 / 9)
    A[n // 2][n // 2] = np.float64(0.5)
    A[n // 2][n // 2 - 1] = np.float64(4 / 9)
    A[n // 2][n // 2 - 2] = np.float64(1 / 18)
    for i in range(2, n // 2 - 1):
        A[i][i] = np.float64(0.5)
        A[i][i - 2] = np.float64(1 / 36)
        A[i][i + 2] = np.float64(1 / 36)
        A[i][i - 1] = np.float64(2 / 9)
        A[i][i + 1] = np.float64(2 / 9)
    print(solve_markov_expectation(A)[-1])

def solve_markov_expectation(A: np.ndarray):
    """Solve the expected steps to reach a stable state at (0, 0)

    Args:
        A: the state transition matrix
    Returns:
        the expected steps
    """
    dim = A.shape[0]
    B = np.eye(dim - 1, dtype=np.float64) - A[1:, 1:]
    x = np.linalg.solve(B, np.ones((dim - 1, ), dtype=np.float64))
    return x

if __name__ == "__main__":
    main()