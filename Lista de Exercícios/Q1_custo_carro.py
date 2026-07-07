# 1. O custo ao consumidor de um carro novo é a soma do custo
# de fábrica com a porcentagem do distribuidor e dos impostos
# (aplicados ao custo de fábrica).
# Supondo que a porcentagem do distribuidor seja de 12% do 
# preço de fábrica e os impostos de 30% do preço de fábrica,
# fazer um programa em Python para ler o custo de fábrica
# de um carro e imprimir o custo ao consumidor.

# porcentagem do distribuidor = 12% do preço de fábrica
# impostos = 30% do preço de fábrica

# ALGORITMO:
# 1- Ler o custo de fábrica do carro
# 2- Calcular o valor da porcentagem do distribuidor (0.12)
# 3- Calcular o valor dos impostos (0.3)
# 4- Imprimir o custo ao consumidor do carro

custoFabrica = float(input("Digite o custo de fábrica do carro R$: "))

distribuidor = 0.12 * custoFabrica
impostos = 0.3 * custoFabrica

custoConsumidor = custoFabrica + distribuidor + impostos

print(f"\nValor de fábrica: R$ {custoFabrica:.2f}")
print(f"Valor do Distribuidor: R$ {distribuidor:.2f}")
print(f"Valor do Imposto: R$ {impostos:.2f}")
print(f"Valor do Carro para o Consumidor: R$ {custoConsumidor:.2f}\n")


