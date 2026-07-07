# 3. Faça um programa que peça o tamanho de um arquivo para
# download (em MB) e a velocidade de um link de Internet (em
# Mbps), calcule e informe o tempo aproximado de download do
# arquivo usando este link (em minutos).

# tamanho do arquivo ---> MB = MegaBytes
# velocidade         ---> Mbps = Mega bits por segundo
# tempo do download  ---> minutos = 60 segundos

# tempo do download = tamanho do arquivo / velocidade

# 1 B -------- 8 b
# 1 MB ------- 10^6 b

#lê o tamanho do arquivo em MB 
tamArquivo = float(input("\nDigite o tamanho do arquivo em MB: "))

#lê a velocidade do link em Mbps
velocidade = float(input("Digite a velocidade do link de internet em Mbps: "))

#converte a velocidade do link em MBps
velocidade_MBps = velocidade / 8

#calcula o tempo em segundos
tempo_segundos = tamArquivo / velocidade_MBps

#converte para minutos
tempo_minutos = tempo_segundos / 60

#imprime resultado 
print(f"\nTamanho do arquivo (MB): {tamArquivo:.2f}")
print(f"Velocidade do link de internet (Mbps): {velocidade:.2f}")
print(f"Tempo aproximado de download: {tempo_segundos:.2f} segundos")
print(f"Tempo aproximado de download: {tempo_minutos:.2f} minutos\n")

