import math
import sys
EPS = 1e-10

if __name__ == '__main__':
    x = float(input("Value of x = "))
    n = int(input("Value of n = "))
    if n < 0:
      print("Illegal value of n", file=sys.stderr)
      print("n should be 0 or more", file=sys.stderr)
      exit(1)


a = 1 / math.factorial(n)
S, k = a, 0


while math.fabs(a) > EPS:
    a *= (x ** 2) / ((4 * (k ** 2)) + (4 * k * n) + (8 * k) + (4 * n) + 4)
    S += a
    k += 1

print(f"Ei({x}) = {((x / 2) ** n) * S}")
