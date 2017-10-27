# list all numbers that are multiples of 3 or 5 and below 50,000,000 and find that sum

# step 1 find multiples of 3 or 5
# step 1a if number is multiple of 3 AND 5, don't count it
# step 2 find out if they are less than 50,000,000
# step 3 add them together

list_of_multiples = []
def sum_of_mul(max):
    sum = 0
    for i in range(3,max,3):
        list_of_multiples.append(i)
        sum += i
    for j in range (5,max,5):
        if j % 3 != 0:
            list_of_multiples.append(j)
            sum += j
    return sum
    
print sum_of_mul(50000000)

    
    
    
    
