# check if a number is prime using loops.

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Test
print(is_prime(7))  
print(is_prime(10))  
print(is_prime(1))   