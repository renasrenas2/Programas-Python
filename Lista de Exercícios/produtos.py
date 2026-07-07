produtos = [
 (1001, "Caneta", 1.50),
 (1002, "Caderno", 12.00),
 (1003, "Mochila", 75.90),
]

codigo_busca = 1002

for produto in produtos:
    codigo, nome, preco = produto
    if codigo == codigo_busca:
        print(f"Produto encontrado: {nome} - R$ {preco:.2f}")
        break
    else:
        print("Produto não encontrado.")