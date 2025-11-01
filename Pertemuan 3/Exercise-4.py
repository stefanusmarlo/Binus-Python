triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

right_angled(a, b, c):
    sides = sorted([a, b, c])
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-6

determine_triangle_type(a, b, c):
    if not is_triangle(a, b, c):
        return "Not a Triangle"
    elif a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        if is_right_angled(a, b, c):
            return "Isosceles and Right-angled"
        return "Isosceles"
    elif is_right_angled(a, b, c):
        return "Right-angled"
    else:
        return "Scalene"

try:
    a = float(input("Enter length of side A: "))
    b = float(input("Enter length of side B: "))
    c = float(input("Enter length of side C: "))

    triangle_type = determine_triangle_type(a, b, c)
    print("Triangle Type:", triangle_type)

except ValueError:
    print("Please enter valid numeric values for the sides.")
