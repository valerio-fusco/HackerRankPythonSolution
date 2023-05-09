# HackerRank problem: https://www.hackerrank.com/challenges/grading/

multiples_5 = [n for n in range(1, 101) if n % 5 == 0]

def diff_from_two_number(a, b):
    return abs(a - b)

def is_multiple_of_5(n):
    return n % 5 == 0
    
def closest_multiple_number(n):
    closest_multiple = 0

    for i in multiples_5:
        n_diff = diff_from_two_number(n, i)
        if n_diff < 3:
            closest_multiple = i

    if closest_multiple > n:
        return closest_multiple

    return n
    
def gradingStudents(grades):
    res = []

    for grade in grades:

        if grade < 38:
            res.append(grade)
            continue

        res.append(closest_multiple_number(grade))

    return res
