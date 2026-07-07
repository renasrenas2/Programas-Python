'''
exemplos de funções:
- append()
- remove()
- pop()
- insert()
- sort()
- reverse()
- len()
'''

numeros = [1, 2, 3, 4, 5]

print(f"Lista numeros antes da alteração: {numeros}")
numeros.append(3)
print(f"Lista numeros depois da alteração: {numeros}")

print(f"Quantidade de elementos na lista numeros: {len(numeros)}")

numeros.sort() 

print(f"Lista organizada em ordem crescente: {numeros}")

numeros.append(6)
numeros.remove(3)

print(numeros)

numeros.reverse()

print(numeros)
