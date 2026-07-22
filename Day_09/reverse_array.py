# using recursion
def reverse_arr(arr,left,right):
    if left >= right:
        return
    arr[left],arr[right] = arr[right],arr[left]
    reverse_arr(arr,left+1,right-1)


# Using while loop
def reverse_arr(arr,left,right):
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1


arr = [1, 2, 3, 4, 5]

reverse_arr(arr, 0, len(arr) - 1)
print(arr)