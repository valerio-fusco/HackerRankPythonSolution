# HackerRank problem: https://www.hackerrank.com/challenges/diagonal-difference/

def diagonalDifference(arr):
    l_to_r = 0
    r_to_l = 0
    i = 0
    j = len(arr) - 1

    for y in arr:
        l_to_r += y[i]
        r_to_l += y[j]
        i += 1
        j -= 1

    return abs(l_to_r - r_to_l)
