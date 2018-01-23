import picasso
import numpy.random as r


def linear_search(a, v):
    for i in range(0,len(a)):
        if (a[i] == v):
            return v


a = [5, 4, 3, 2, 1]
print linear_search(a, 1)

p = picasso.Picasso('linear_search')
p.draw_best_fitting_line = True
for i in range(0, 15001, 1000):
    p.start(i)
    a = r.random_integers(0, i, i)
    linear_search(a, 1)
    p.end()
    p.export()