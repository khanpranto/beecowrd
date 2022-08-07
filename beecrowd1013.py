
"""Make a program that reads 3 integer values and present
the greatest
one followed by the message "eh o maior". Use the
following formula:

"""




import math
value = input().split()
a,b,c = value

maior = (int(a) + int(b) + abs(int(a) - int(b))) / 2
resultado = (int(maior) + int(c) + abs(int(maior) - int(c)))/2
print("%d eh o maior" %resultado)
