from sympy import symbols, diff, integrate, cos
from math import pi

t = symbols('t')
c = 2125%10
a = 30/100

# Função velocidade
funcValocidade = a*2*pi*9*cos(2*pi*9*t - c)

# Integrando a função velocidade para obter a função deslocamento
funcDeslocamento = integrate(funcValocidade, t)
print(f"A função deslocamento é: {funcDeslocamento}")

# Derivando a função velocidade para obter a função aceleração
funcAceleracao = diff(funcValocidade, t)
print(f"A função aceleração é: {funcAceleracao}")

# Substituindo t = 7 na função aceleração
print(f"A aceleração no instante t = 7 é: {funcAceleracao.subs(t, 7).evalf()} m/s²")