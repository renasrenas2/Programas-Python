tarefas = []

tarefas.append("Estudar Python")
tarefas.append("Fazer exercícios")
tarefas.append("Ler documentação")

print("Tarefas iniciais:")
print(tarefas)

tarefas.insert(0, "Tomar café")
tarefas.remove("Fazer exercícios")

print("\nTarefas após alterações:")
for i in range(len(tarefas)):
    print(f"{i + 1}. {tarefas[i]}")

tarefas.sort()

print("\nTarefas em ordem alfabética:")
print(tarefas)

tarefas.reverse()
print("\nTarefas em ordem reversa:")
print(tarefas)

ultima = tarefas.pop()
print(f"\nÚltima tarefa removida: {ultima}")
print(f"\nNúmero de tarefas restantes: {len(tarefas)}")