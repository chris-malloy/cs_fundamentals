# take two sorted arrays and combine them and sort them

# try and do this
# [1]
# then [1,2,3]
# then [1,2,3,4]
import numpy
import numpy.random as r

def merge_and_sort(a, b):
    c = []
    while (len(a) != 0) and (len(b) != 0):
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        final = c + b
    else:
        final = c + a

    return final

# a = [1,3,5]
# b = [2,4,6]

# print merge_and_sort(a,b)

def merge_sort(a):
    if len(a) == 1:
        return a
    else:
        mid = len(a) / 2
    a_list = merge_sort(a[:mid])
    b_list = merge_sort(a[mid:])
    return merge_and_sort(a_list,b_list)

random_array = r.random_integers(0, 100, 10).tolist()
print 'random_array'
print random_array

sorted_array = merge_sort(random_array)
print 'sorted array'
print sorted_array
