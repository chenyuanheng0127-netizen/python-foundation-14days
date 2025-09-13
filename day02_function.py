def power(base:int, exponent:int=2) -> int:
    """Calculate the power of a number."""
    return base ** exponent

print(power(3))          # Default exponent is 2
print(power(2, 3))       # 2 raised to the power of 3

# 可变参数
def totle_sum(*args: int) -> int:
    """Calculate the sum of all provided numbers."""
    return sum(args)

print(totle_sum(1, 4, 9, 23, 91))
print(totle_sum(10, 20, 30))
print(totle_sum())       # No arguments, should return 0

# 关键字参数
def introduce(**kwargs) -> str:
    """Introduce a person with given attributes."""
    return ';'.join(f"{key}:{value}" for key, value in kwargs.items())
print(introduce(name="Alice", age=30, city="New York"))
print(introduce(name="Bob", profession="Engineer"))
print(introduce())       # No arguments, should return an empty string

#匿名函数
square = lambda x: x **2
print(square(5))
add = lambda x, y: x + y
print(add(3, 7))
num = [1, 2, -3, 4, 5]
print (sorted(num, key=lambda x: x**2))

#综合
def stats(*args, method="sum") -> int | float:
    if method == "sum":
        return sum(args)
    elif method == "max":
        return max(args)
    elif method == "min":
        return min(args)
    elif method == "mean":
        return sum(args) / len(args) if args else 0
    else:
        raise ValueError(f"Unknown method: {method}")
print(stats(1, 2, 3, 4, 5))               # Default is sum
print(stats(1, 2, 3, 4, 5, method="max"))
print(stats(1, 2, 3, 4, 5, method="min"))
print(stats(1, 2, 3, 4, 5, method="mean"))
print(stats())                            # No arguments, should return 0 for mean  