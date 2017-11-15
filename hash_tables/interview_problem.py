# given an array of numbers
# [1,2,2,10,3,5]
# Question 1 --> What is the least occuring number?
# Question 2 --> return true if there are any duplicates

def hash_problem(array):
    my_hash = {}
    for i in range(len(a)):
        if my_hash[str(a[i])] == None:
            my_hash[str(a[i])] = 1
        else:
            my_hash[str(a[i])] += 1
    min_array = []
    min = myHash(first_value)
    for k,v in my_hash:
        if v > min:
            return
        elif v == min:
            min_array.append(k)
        else:
            min_array = [k]
    return min_array

a = [1,2,2,10,3,5]
hash_problem(a)

