from sympy import Symbol, limit, sqrt

x = Symbol('x')
c = 2125%10

# Função
func1 = (1 + ((c-15)/sqrt(x))) ** sqrt(x)

# Limite de x tendendo a 0
limite1 = limit(func1, x, 0)
print(f"O primeiro limite é: {limite1}")

# Limite de x tendendo a infinito
limite2 = limit(func1, x, 'oo')
print(f"O segundo limite é: {limite2}")

# Limite de x tendendo a -infinito
limite3 = limit(func1, x, '-oo')
print(f"O terceiro limite é: {limite3}")