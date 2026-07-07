p1 = float(input("\nDigite a nota da prova 1: "))
p2 = float(input("Digite a nota da prova 2: "))

t1 = float(input("Digite a nota do trabalho 1: "))
t2 = float(input("Digite a nota do trabalho 2: "))

media_provas = (p1 + p2)/2

media_trabalho = (t1 + t2)/2

media_final = (0.8 * media_provas) + (0.2 * media_trabalho)

print(f"\nMédia final: {media_final:.2f}")

if media_final >= 6.0:
    print(f"\nVocê está aprovado!\n")
else:
    print(f"\nNão aprovado.\n")
