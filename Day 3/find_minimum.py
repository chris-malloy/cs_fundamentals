def find_minimum(a):
    #look through array, compare each number to next number. 
    # if i is > next num, than put next num in lowest_num var
    for i in range(len(a)-1):
        lowest_num = a[i]
        if a[i] < lowest_num:
            lowest_num = a[i]
    return lowest_num

a = [12,3,5,-3,20]
print find_minimum(a)