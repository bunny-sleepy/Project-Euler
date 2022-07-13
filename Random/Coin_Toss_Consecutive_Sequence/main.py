import numpy as np

def main():
    H_string = 'H'
    T_string = 'T'
    pattern = input() # match pattern input
    p = float(input()) # probability of head
    
    len_p = len(pattern)
    # construct Markov Matrix
    X = np.zeros([len_p, len_p])
    for idx in range(len_p):
        s = pattern[:idx]
        match_len_H = str_max_head_tail_match(pattern, f"{s}{H_string}")
        match_len_T = str_max_head_tail_match(pattern, f"{s}{T_string}")
        if match_len_H < len_p:
            X[idx, match_len_H] = p
        if match_len_T < len_p:
            X[idx, match_len_T] = 1 - p
    # (I - X) \mu = 1, we want \mu_0
    print(np.matmul(np.linalg.inv(np.eye(len_p) - X), np.ones((len_p, 1)))[0][0])

def str_max_head_tail_match(s1: str, s2: str):
    '''
    return: uint, the match length
    '''
    if len(s1) == 0 or len(s2) == 0:
        return 0
    
    length = len(s2)
    while length > 0:
        if s2[len(s2) - length:] == s1[:length]:
            break
        length -= 1
    return length
    

if __name__ == "__main__":
    main()