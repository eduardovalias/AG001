from sympy import sqrt, symbols, diff, integrate

t = symbols('t')
c = 2125%10

# Equação de deslocamento
s = (-2*t**4)/3 + 5*sqrt(t) - c

# Velocidade
v = diff(s, t)
print(f"v(t) = {v}")
print(f"v(8) = {v.subs(t, 8).evalf()} m/s")

# Aceleração
a = diff(v, t)
print(f"a(t) = {a}")
print(f"a(9) = {a.subs(t, 9).evalf()} m/s²")