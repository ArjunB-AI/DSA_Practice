# Ascending order
def bub_sort(num):

    n = len(num)

    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if num[j] > num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]
    return num

# Descending order
def bub_sort(num):
    
    n = len(num)
    
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if num[j] < num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]
        
    return num

arr = [1,3,6,4,2,5]
print(bub_sort(arr))