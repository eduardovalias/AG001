from sympy import Eq, solve, symbols, sec

x = symbols('x')
c = 2125%10

# Primeira equação
eq1 = Eq(2**x + 2**(4*x), c + 1)
print(f"x1 = {solve(eq1, x)}")

# Segunda equação
eq2 = Eq((c + 2) * x**3 - (c + 1) * x**2 - 5*x, -4*c)
print(f"x2 = {solve(eq2, x)}")

# Terceira equação
eq3 = Eq((3*sec((c - 3)*x) + 2)**2, 0)
print(f"x3 = {solve(eq3, x)}")