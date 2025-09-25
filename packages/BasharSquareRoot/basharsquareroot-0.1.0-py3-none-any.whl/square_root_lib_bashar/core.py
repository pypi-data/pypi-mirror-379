import math

def sqrt_number(number: float) -> float:
    if number < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(number)
