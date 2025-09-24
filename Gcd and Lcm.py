def gcd(a: int, b: int) -> int:
    """
    Return the greatest common divisor (non-negative) of integers a and b.
    Uses the iterative Euclidean algorithm.
    """
    # make sure we work with non-negative values
    a, b = abs(a), abs(b)

    # Special case: gcd(0, 0) is usually defined as 0 in computing contexts
    if a == 0 and b == 0:
        return 0

    # Euclidean loop
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """
    Return the least common multiple of a and b.
    If either a or b is 0, lcm is 0 (no non-zero common multiple).
    """
    # If both zero, no meaningful LCM — we choose to return 0 but inform could be undefined.
    if a == 0 and b == 0:
        return 0

    # compute using gcd; abs() to keep LCM non-negative
    return abs(a * b) // gcd(a, b)


if __name__ == "__main__":
    x = int(input("Enter first integer: "))
    y = int(input("Enter second integer: "))

    print("GCD:", gcd(x, y))
    print("LCM:", lcm(x, y))
