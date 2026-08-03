def insert_sort(nums):
    n = len(nums)
    for i in range(1,n):
        key = nums[i]
        j = i-1

        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = key

    return nums

arr = [1,3,5,4,2]
arr = [1,3,5,4,2]
arr = [1,3,5,4,2]
print(insert_sort(arr))