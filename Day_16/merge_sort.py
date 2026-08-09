# Function for merging the sorted arrays
def merge_arr(left,right):

    result = []
    n,m = len(left),len(right)
    i,j = 0,0

    while i<n and j<m:
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i < n:
        result.append(left[i])
        i += 1

    while j < m:
        result.append(right[j])
        j += 1

    return result


# Function for merge_sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    n = len(arr)
    min_value = n//2
    left_arr = arr[: min_value]
    right_arr = arr[min_value :]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_arr(left,right)

arr1 = [9,8,7,6,5,4,3,2,1]
print(merge_sort(arr1))