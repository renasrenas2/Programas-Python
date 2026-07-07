# 4. Elabore um programa em Python que leia as duas notas de
# prova (P1 e P2) e duas notas de trabalho (T1 e T2) e
# posteriormente exiba a mensagem ‘Aprovado’ ou ‘Não
# aprovado’ dependendo dos valores obtidos, conforme as
# regras de cálculo definidas a seguir:
#  • Média de provas: MP = (P1 + P2)/2
#  • Média de trabalhos: MT = (T1 + T2)/2
#  • Média final: MF = 0,8MP + 0,2MT
#  • Situação:
#   ◦ Se MF ≥ 6,0 → aprovado
#   ◦ Se MF < 6,0 → não aprovado

notaP1 = float(input("Digite a nota P1 da prova: "))
notaP2 = float(input("Digite a nota P2 da prova: "))

notaT1 = float(input("Digite a nota T1 do trabalho: "))
notaT2 = float(input("Digite a nota T2 do trabalho: "))

media_provas = (notaP1 + notaP2)/2
media_trabalhos = (notaT1 + notaT2)/2

media_final = 0.8 * media_provas + 0.2 * media_trabalhos

if media_final >= 6.0:
    print("Aprovado.")
elif media_final < 6:
    print("Reprovado.")
