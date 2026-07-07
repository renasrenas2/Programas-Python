"""
8. Faça um programa em Python que leia dois valores inteiros, x
e y. Por meio de multiplicações sucessivas, calcule e exiba a
função de exponenciação xy
(Obs: quando o valor de y for 0,
não importa o valor de x, o resultado sempre será 1. Utilizar
função).
"""

# y = número de vezes que o x vai se multiplicar por ele mesmo
# do:
# n = y
# r = x
# r = r * x
# r = r * x
def calcular_x(x,y):
    n = y
    r = x
    for i in range(n-1):
        r = r * x
    print(f"O resultado de {x}^{y} é: {r}\n")

x = int(input("\nDigite o valor da base (x): ")) 
y = int(input("Digite o valor do expoente (y): "))

calcular_x(x,y)



