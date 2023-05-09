# HackerRank problem: https://www.hackerrank.com/challenges/cats-and-a-mouse/

def get_distance(a, b):
    return abs(a - b)

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    
    cat_a_dis = get_distance(x, z)
    cat_b_dis = get_distance(y, z)
    
    if cat_a_dis < cat_b_dis:
        return "Cat A"
    elif cat_a_dis > cat_b_dis:
        return "Cat B"
    else:
        return "Mouse C"
            
