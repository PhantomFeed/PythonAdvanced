def find_insert_position(array, x):
    left = 0
    right = len(array)

    while left < right:
        middle = (left + right) // 2
        if array[middle] < x:
            left = middle + 1
        else:
            right = middle
    return left


A = [1, 2, 3, 4, 5]
x = 4
print(find_insert_position(A, x))
