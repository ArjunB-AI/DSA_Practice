def is_palindrome(num):
    num = abs(num)
    original_num = num  
    result = 0          
    
    while num > 0:
        ld = num % 10
        result = (result * 10) + ld
        num = num // 10
        
    return result == original_num

print(is_palindrome(12345))