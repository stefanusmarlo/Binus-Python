import cmath

a = float(input("Enter value A: "))
b = float(input("Enter value B: "))
c = float(input("Enter value C: "))

if a == 0:
    print("It is not a quadratic equation")
else:
    discriminant = b**2 - 4*a*c
    equation = f"{a}x² + {b}x + {c} = 0"
    print(f"Quadratic Equation: {equation}")
    print(f"Discriminant value: {discriminant}")

    if discriminant > 0:
        x1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        print("It has distinct roots")
        print(f"Root x1: {x1.real}")
        print(f"Root x2: {x2.real}")
    elif discriminant == 0:
        x = -b / (2*a)
        print("It has a double root")
        print(f"Root x1 and x2: {x}")
    else:
        x1 = (-b + cmath.sqrt(discriminant)) / (2*a)
        x2 = (-b - cmath.sqrt(discriminant)) / (2*a)
        print("It has imaginary roots")
        print(f"Root x1: {x1}")
        print(f"Root x2: {x2}")
