
def pascal_triangle(n):
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        temp = []
        for j in range(i + 1):
            value = factorial(i) // (factorial(j) * factorial(i - j))
            temp.append(value)
        triangle.append(temp)

    return triangle


def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i
    
    return result
