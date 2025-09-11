#day01_basics.py
#This is a simple Python script that demonstrates basic syntax and operations.
#PRINT STATEMENT
print("Hello, World!")
#VARIABLES AND DATA TYPES
name = "Alice"  # String
age = 30        # Integer
height = 5.5    # Float
is_student = False  # Boolean
#LISTS
print(type(name), type(age), type(height), type(is_student))
#容器
nums = [1, 2, 3, 4, 5]
print(nums[0], nums[-1], sum(nums), len(nums))
#切片&推导式
squares = [n**3 for n in nums if n % 2 == 1]
print(squares)
#函数
def greet(user: str) -> str:
    return f"Hello, {user}!"

print(greet("Hendrix"))
def sum(numbers:list[int]) -> int:
    total = 0
    for num in numbers:
        total += num
    return total

print(sum([1, 2, 3, 4, 5]))

def is_even(n:int) -> bool:
    return n % 2 == 0

print(is_even(20000))

def square_sum(numbers:int) -> int:
    return sum(n**2 for n in range(1, numbers+1))

print("square sum of 1 to 100:", square_sum(100))

#numpy向量化
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("numpy array:", arr)
print("numpy array sum of squares:", np.sum(arr**2))
print("square:", arr**2)
print("mean:", arr.mean())
print("mean:", np.mean(arr))