print("Equation a*x**2 + b*x + c == 0,")
print("Enter a")
a = input()
a = float(a)
print("Enter b")
b = input()
b= float(b)
print("Enter c")
c = input()
c= float(c)
d = (b**2) - (4*a*c)
print(d)
if d > 0:
    print('x_1 = (-b - delta**0.5) / (2 * a)')
    print('x_2 = (-b + delta**0.5) / (2 * a)')

    print("Primes of the quadratic equation:")
    print("x_1 = (x_1)")
    print("x_2 = (x_2)")


elif d == 0:
    print("Primes of the quadratic equation:")
    x_1 = x_2 = 0

elif d != 0:
    print("no solution")
