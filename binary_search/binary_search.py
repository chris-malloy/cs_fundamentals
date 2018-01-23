# 1. define start and end
# 2. mid == target?  if yes => return index,
#   if no => target < mid and end = mid - 1
#   or target > mid and start = mid + 1
# 3. find length of remaining data set, which is end minus start, then /2 by two to get midpoint #   of that set
# 4. take that number and add it to start
# 5. this can be simplified to start + end / 2

import picasso
import numpy.random as r

def binary_search(a, v):
    start = 0
    end = len(a) - 1

    while start < end:
        mid_index = (end + start) / 2
        print start, end, mid_index
        mid_value = a[mid_index]
        if v == mid_value:
            return mid_index
        elif v > mid_value:
            start = mid_value + 1
            return mid_index
        elif v < mid_value: 
            end = mid_index - 1
            return mid_index

a = range(0,10,1)
print a 
print "Index of Target: " + str(binary_search(a, 9))

# p = picasso.Picasso('binary_search')
# p.draw_best_fitting_line = True
# for i in range(0, 15001, 1000):
#     p.start(i)
#     a = r.random_integers(0, i, i)
#     binary_search(a, 1)
#     p.end()
#     p.export()
