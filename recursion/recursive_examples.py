# reverse an array recursively
arr = [1,2,3,4,5]
def reverse(arr,index):
    if index <= (len(arr)/2):
        arr[index], arr[len(arr)-1-index] = arr[len(arr)-1-index],arr[index]
        index += 1
        return reverse(arr,index)
    else:
        return arr

print reverse(arr,0)

# def factorial(number):
#     if number == 0:
#         return 1
#     else:
#         result = number * factorial(number - 1)
#         return resul\\
# print factorial(5)

# def count_down(number):
#     if number == -1:
#         return
#     print(number)
#     count_down(number-1)
# count_down(10)
# pass dynamic elements as parameters
# def add(array,current_index,sum):
#     sum += array[current_index]
#     if current_index == len(array)-1: #base case
#         return sum
#     else:
#         return add(array,current_index+1,sum)

        
# a = [10,15,12,13]

# print add(a,0,0)


