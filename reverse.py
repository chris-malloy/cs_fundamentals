def reverse(a):
    for i in range(len(a)/2):
        z = len(a) - 1 - i
        a[i], a[z] = a[z], a[i]

    return a



a = [1,2,3,4,5]
print(reverse(a))