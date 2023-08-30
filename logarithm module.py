def calculate_log(x, base):
    if x <= 0 or base <= 1:
        raise ValueError("Input values must be positive.")

    epsilon = 1e-6
    low = 0
    high = x
    mid = 0

    while high - low > epsilon:
        mid = (low + high) / 2
        value = base ** mid
        
        if value < x:
            low = mid
        else:
            high = mid

    return mid

# Example usage
x = 14
base = 9
result = calculate_log(x, base)
print(f"Log_{base}({x}) = {result}")
