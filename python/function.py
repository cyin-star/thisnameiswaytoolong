def is_num(num):
    try:
        num = float(num)
        return True
    except:
        return False


def check_for_valid_equation(eq1, eq2):
    form = 'ax+by=c'
    eq1 = eq1.replace(" ", '')
    eq2 = eq2.replace(' ','')
    symbols = "+-="
    if (is_num(eq1[0])==False and is_num(eq2[0])==False) and (is_num(eq1[3])==False and is_num(eq2[3])==False) and (is_num(eq1[6])==False and is_num(eq2[6])==False):
        raise ValueError("Please use valid coeficiants")
        return [False,"Please use valid coeficiants"]
    if ((is_num(eq1[2]) not in symbols) and (is_num(eq2[2]) not in symbols)) and ((is_num(eq1[4]) not in symbols) and (is_num(eq2[4]) not in symbols)) and ((is_num(eq1[5]) not in symbols) and (is_num(eq2[5]) not in symbols)):
        raise ValueError("Please use valid varaibles(x,y)/symbols(+,-,=)")
        return [False, 'Please use valid varaibles/symbols(+,-,=)']
    return True





import re

def extract_coefficients(equation):
    # Remove spaces from the equation
    equation = equation.replace(" ", "")

    # Use regex to find coefficients
    pattern = r'([-+]?\d*\.?\d*)x\^2\s*([-+]?\d*\.?\d*)x\s*([-+]?\d*\.?\d*)'
    match = re.match(pattern, equation)

    if match:
        a = float(match.group(1)) if match.group(1) else 1.0  # Default to 1 if missing
        b = float(match.group(2)) if match.group(2) else 1.0  # Default to 1 if missing
        c = float(match.group(3)) if match.group(3) else 0.0  # Default to 0 if missing
        return a, b, c
    else:
        raise ValueError("The equation is not in the correct form.")


import sympy as sp


def get_coefficients(poly):
    # Get the coefficients of the polynomial
    return sp.Poly(poly).all_coeffs()


def quadratic_intersection(poly1, poly2):
    # Get coefficients for both polynomials
    coeffs1 = get_coefficients(poly1)
    coeffs2 = get_coefficients(poly2)

    # Coefficients for the equation Ax^2 + Bx + C = 0
    A = coeffs1[0] - coeffs2[0]  # x^2 coefficients
    B = coeffs1[1] - coeffs2[1]  # x coefficients
    C = coeffs1[2] - coeffs2[2]  # constant terms

    # Check for special cases
    if A == 0 and B == 0:
        if C == 0:
            return "The curves are identical."
        else:
            return "The curves are parallel and do not intersect."

    # Calculate the discriminant
    discriminant = B**2 - 4 * A * C

    if discriminant < 0:
        return "No intersection points."
    elif discriminant == 0:
        x = -B / (2 * A)
        y = coeffs1[0] * x**2 + coeffs1[1] * x + coeffs1[2]
        return [(x, y)]  # One intersection point
    else:
        x1 = (-B + sp.sqrt(discriminant)) / (2 * A)
        x2 = (-B - sp.sqrt(discriminant)) / (2 * A)
        y1 = coeffs1[0] * x1**2 + coeffs1[1] * x1 + coeffs1[2]
        y2 = coeffs1[0] * x2**2 + coeffs1[1] * x2 + coeffs1[2]
        return [(x1, y1), (x2, y2)]  # Two intersection points


def calc_quad1(eq1, eq2):
    # Define the variable
    x = sp.symbols('x')
    eq1 = eq1.replace(" ", '')
    eq2 = eq2.replace(' ', '')
    a1, b1, c1 = extract_coefficients(eq1)
    a2, b2, c2 = extract_coefficients(eq2)
    # Get user input for the first polynomial coefficients

    # Define the first polynomial
    poly1 = a1 * x**2 + b1 * x + c1
    # Define the second polynomial
    poly2 = a2 * x**2 + b2 * x + c2

    # Calculate intersection points
    intersection_points = quadratic_intersection(poly1, poly2)
    return intersection_points








def extract_quadratic_coefficients(equation):
    # Remove spaces from the equation
    equation = equation.replace(" ", "")

    # Regex pattern for quadratic equations
    pattern = r'([-+]?\d*\.?\d*)x\^2\s*([-+]?\d*\.?\d*)x\s*([-+]?\d*)'
    match = re.match(pattern, equation)

    if match:
        a = float(match.group(1)) if match.group(1) else 1.0  # Default to 1 if missing
        b = float(match.group(2)) if match.group(2) else 1.0  # Default to 0 if missing
        c = float(match.group(3)) if match.group(3) else 0.0  # Default to 0 if missing
        return a, b, c
    else:
        raise ValueError("The quadratic equation is not in the correct form.")

def extract_linear_coefficients(equation):
    # Remove spaces from the equation
    equation = equation.replace(" ", "")

    # Regex pattern for linear equations
    pattern = r'([-+]?\d*\.?\d*)x\s*([-+]?\d*)'
    match = re.match(pattern, equation)

    if match:
        b = float(match.group(1)) if match.group(1) else 1.0  # Default to 1 if missing
        c = float(match.group(2)) if match.group(2) else 0.0  # Default to 0 if missing
        return b, c
    else:
        raise ValueError("The linear equation is not in the correct form.")

def get_coefficients(poly):
    # Get the coefficients of the polynomial
    return sp.Poly(poly).all_coeffs()

def quadratic_linear_intersection(quadratic, linear):
    # Get coefficients for both polynomials
    coeffs_quad = get_coefficients(quadratic)
    coeffs_lin = get_coefficients(linear)

    # Coefficients for the equation Ax^2 + Bx + C = 0
    A = coeffs_quad[0]  # x^2 coefficient from quadratic
    B = coeffs_quad[1] - coeffs_lin[0]  # x coefficient (subtract linear's coefficient)
    C = coeffs_quad[2] - coeffs_lin[1]  # constant terms (subtract linear's constant)

    # Calculate the discriminant
    discriminant = B**2 - 4 * A * C

    if discriminant < 0:
        return "No intersection points."
    elif discriminant == 0:
        x = -B / (2 * A)
        y = coeffs_quad[0] * x**2 + coeffs_quad[1] * x + coeffs_quad[2]
        return [(x, y)]  # One intersection point
    else:
        x1 = (-B + sp.sqrt(discriminant)) / (2 * A)
        x2 = (-B - sp.sqrt(discriminant)) / (2 * A)
        y1 = coeffs_quad[0] * x1**2 + coeffs_quad[1] * x1 + coeffs_quad[2]
        y2 = coeffs_quad[0] * x2**2 + coeffs_quad[1] * x2 + coeffs_quad[2]
        return [(x1, y1), (x2, y2)]  # Two intersection points

def solve_linear_quad(eq1,eq2):
    # Define the variable
    x = sp.symbols('x')
    eq1 = eq1.replace(" ", '')
    eq2 = eq2.replace(' ', '')

    b1, c1 = extract_linear_coefficients(eq1)
    a2, b2, c2 = extract_quadratic_coefficients(eq2)

    # Define the linear polynomial
    linear_poly = b1 * x + c1
    # Define the quadratic polynomial
    quad_poly = a2 * x**2 + b2 * x + c2

    # Calculate intersection points
    intersection_points = quadratic_linear_intersection(quad_poly, linear_poly)
    return intersection_points
def find_vertex(eq):
    a,b,c = extract_quadratic_coefficients(eq)
    # Calculate the x-coordinate of the vertex
    x_vertex = -b / (2 * a)
    # Calculate the y-coordinate of the vertex
    y_vertex = a * x_vertex**2 + b * x_vertex + c
    return (x_vertex, y_vertex)

import cmath
def find_roots(eq):
    a,b,c = extract_quadratic_coefficients(eq)
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Calculate the two roots using the quadratic formula
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

    return (root1, root2)
def get_info(eq):
    a,b,c = extract_quadratic_coefficients(eq)
    return f'Y-intercept: {c}, roots: {find_roots(eq)}, vertex: {find_vertex(eq)}'

def avg(a):
    return sum(a)/len(a)

def calc_basic_stats(nums):
    nums = nums.replace(' ','')
    nums = nums.split(',')
    av = avg([int(i) for i in nums])
    return f"average: {av}"





