# a = [5,3,1,4,-1]
# 3 < 5
# put 3 in temp spot
# move 5 then move 3
# move sorted list
import picasso 
# take a[i] and figure out where to insert it on the left

import numpy.random as r 

def insertion_sort(a):
    #unsorted list - i is the beginning of the unsorted list
    for i in range(len(a)):
        temp = a[i]
        j = i
        #sorted list - j is end of sorted list
        while (j > 0) and (a[j-1] > temp): #second condition is for when the value to the left of j is greater than j
            a[j] = a[j-1]
            j -= 1
        
        a[j] = temp
    return a

a = [5,4,3,2,1]
print insertion_sort(a)

# temp is the number that we are looking to insert to the left of it

p = picasso.Picasso('insertion_sort')
p.draw_best_fitting_line = True



