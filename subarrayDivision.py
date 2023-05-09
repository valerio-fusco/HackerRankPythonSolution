# HackerRank problem: https://www.hackerrank.com/challenges/the-birthday-bar/

def birthday(s, d, m):
    sequence = s
    length = m
    target = d
    result = 0

    for i in range(len(sequence) + 1):
        if i > length - 1:
            segments = sequence[i-length:i]
            if sum(segments) == target:
                result += 1

    return result
