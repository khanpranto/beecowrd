"""Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​​the square that has side B.
e) the area of the rectangle that has sides A and B.

"""
a, b, c = list(map(float, input().split()))

triangle = 0.5*a*c
print(f"TRIANGULO: {triangle:.3f}")

radius_circle = 3.14159*(c*c)
print(f"CIRCULO: {radius_circle:.3f}")

trapiziom = ((a+b)/2)*c
print(f"TRAPEZIO: {trapiziom:.3f}")

square = b*b
print(f"QUADRADO: {square:.3f}")

rectangle = a*b
print(f"RETANGULO: {rectangle:.3f}")

