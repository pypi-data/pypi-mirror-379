# mymodule.py

# 1. Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


# 2. Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 3. Function to reverse a string
def reverse_string(s):
    return s[::-1]


# 4. Function to find the largest number in a list
def find_max(lst):
    if not lst:
        return None
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val


# 5. Function to count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
