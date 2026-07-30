def sel_sort(num):
    n = len(num)

    for i in range(0,n):
        min_ind = i

        for j in range(i+1,n):
            if num[j] < num[min_ind]:
                min_ind = j

        num[i],num[min_ind] = num[min_ind],num[i]

    return num


arr = [1,3,2,4,6,5,9,8]
print(sel_sort(arr))