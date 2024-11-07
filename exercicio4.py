from sympy import Eq, solve, symbols

c = 2125%10

# Correntes
I1, I2, I3 = symbols('I1 I2 I3')

# Tensões
V1 = 3 + (4*c)
V2 = -1 - (5*c)

# Resistências
R1, R2, R3 = 25, 10, 20

# Equacionamento das malhas
eq1 = Eq(0, -V1 + I1*R1 + I2*R2)
eq2 = Eq(0, -I2*R2 - I3*R3 + V2)
eq3 = Eq(I2, I1 + I3)

results = solve((eq1, eq2, eq3), (I1, I2, I3))

print(f"I1 = {results[I1]} A")
print(f"I2 = {results[I2]} A")
print(f"I3 = {results[I3]} A")