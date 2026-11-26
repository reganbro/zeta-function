import math

def zeta(s: int, a: int = 25) -> float:
    if not isinstance(s, int) or s < 1:
        raise ValueError("s must be a positive integer")
    if not isinstance(a, int) or a < 1:
        raise ValueError("a must be a positive integer")
    if s == 1:
        return math.inf
    if s >= 55:  # 2**-55 < float64 machine epsilon (~2.22e-16)
        return 1.0

    # Sum smallest terms first to minimize floating-point rounding drift
    total = 0.0
    for i in range(a - 1, 1, -1):
        total += i ** (-s)
    if a > 1:
        total += 1.0

    # Euler-Maclaurin tail for sum_{i=a}^{inf} i^-s (computed once)
    inv_a = 1.0 / a
    inv_a_s = inv_a ** s
    inv_a2 = inv_a * inv_a

    tail = inv_a_s * (
        a / (s - 1)
        + 0.5
        + (s / 12.0) * inv_a
        - (s * (s + 1) * (s + 2) / 720.0) * inv_a * inv_a2
        + (s * (s + 1) * (s + 2) * (s + 3) * (s + 4) / 30240.0) * inv_a * inv_a2 * inv_a2
        - (s * (s + 1) * (s + 2) * (s + 3) * (s + 4) * (s + 5) * (s + 6) / 1209600.0) * inv_a * (inv_a2 ** 3)
    )
    return total + tail
lol=int(input("Enter value for s: "))
print(zeta(lol, 25))
