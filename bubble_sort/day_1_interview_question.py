# SOLUTION A

def solution_a(m):
    s = 0

    for i in range(1, m):
        if i % 3 == 0 or i % 5 == 0:
            s += i

    return s

# SOLUTION B

def solution_b(max):
    sum_of_factors_of_3 = solution_b_helper(3, max)
    sum_of_factors_of_5 = solution_b_helper(5, max)
    sum_of_factors_of_15 = solution_b_helper(15, max)
    s = sum_of_factors_of_3 + sum_of_factors_of_5 - sum_of_factors_of_15
    return s

def solution_b_helper(number, max):
    s = 0

    for i in range(0, max, number):
        s += i

    return s

# SOLUTION C

def solution_c(max):
    sum_of_factors_of_3 = solution_c_helper(3, max)
    sum_of_factors_of_5 = solution_c_helper(5, max)
    sum_of_factors_of_15 = solution_c_helper(15, max)
    s = sum_of_factors_of_3 + sum_of_factors_of_5 - sum_of_factors_of_15
    return s

def solution_c_helper(number, max):
    n = int((max - 1) / number)
    sum = number * (n * (n + 1)) / 2
    return int(sum)
