# HackerRank problem: https://www.hackerrank.com/challenges/camelcase/

def camelCase(s):
    
    counter = 1
    
    for char in s:
        if char.isupper():
            counter += 1
            
    return counter
