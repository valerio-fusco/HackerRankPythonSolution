# HackerRank problem: https://www.hackerrank.com/challenges/mini-max-sum/

def miniMaxSum(arr):
    arr = sorted(arr)

    min_sum = 0
    max_sum = 0
    c = 0

    for n in arr:
        if c < 4:
            min_sum += n
        if c > 0:
            max_sum += n

        c += 1

    print(min_sum, max_sum)
