temp_Celsius = float(input("\nDigite a temperatura em Graus Celsius: "))

if temp_Celsius < 0:
    print("Frio extremo.\n")
elif temp_Celsius >= 0 and temp_Celsius <= 10:
    print("Frio.\n")
elif temp_Celsius > 10 and temp_Celsius <= 25:
    print("Ameno.\n")
elif temp_Celsius > 25 and temp_Celsius <= 35:
    print("Quente.\n")
else:
    print("Muito quente.\n")
