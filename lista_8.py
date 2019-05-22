import math

def func(x):
    return math.exp(x ** 3) * (x ** 2)

# pi1 - a
import scipy.integrate as integrate
import scipy.special as special
a, b = 3, 5
analytical_result = integrate.quad(func, a, b)[0]

print(f'Resultado analítico: {analytical_result}')

# pi1 - b
a, b = 3, 5
h = 10 ** (-3) # Size of the path
sum_ = -( func(a) + func(b) ) / 2.0 # Multiplication by h

# in the end
while a < b:
    sum_ += func(a)
    a += h

numerical_result = (sum_ + func(b)) * h
print(f'Resultado numérico: {numerical_result}')

# pi1 - d
a, b = 3, 5
h = 10 ** (-2)
sum_ = -( func(a) + func(b) ) / 2.0

# in the end
while a < b:
    sum_ += func(a)
    a += h

numerical_result_2 = (sum_ + func(b)) * h
print(f'Resultado 10^-2: {numerical_result_2} - \nDiff 10^-3: {numerical_result_2-numerical_result}\n')

a, b = 3, 5
h = 10 ** (-4) # Size of the path
sum_ = -( func(a) + func(b) ) / 2.0 # Multiplication by h

# in the end
while a < b:
    sum_ += func(a)
    a += h

numerical_result_4 = (sum_ + func(b)) * h
print(f'Resultado 10^-4: {numerical_result_2} - \nDiff 10^-3: {numerical_result_4-numerical_result}')
