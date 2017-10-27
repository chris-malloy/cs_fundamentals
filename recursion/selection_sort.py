# every number is unsorted
# find minumum unsorted element and put it and the end of the sorted portion
# swap the a[0](beigging of unsorted list) with minumimum number
# then minimum element will change

# def find_minimum(a):
#     for i in range(len(a)-1):
#         lowest_num = a[i]
#         if a[i] < lowest_num:
#             lowest_num = a[i]
#     return lowest_num

# a = [12,3,5,-3,20]
# print find_minimum(a)

def selection_sort(a):
    for i in range(len(a)):
        minimum = i
        for j in range(i,len(a)):
            if a[j] < a[minimum]:
                minimum = j
        a[i],a[minimum] = a[minimum],a[i]

    return a

a = [5,4,3,2,1] 
print selection_sort(a)
    