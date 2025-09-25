# 9. Verifica se a temperatura está congelante, agradável ou quente

print('''
      
      CONVERSÃO DE TEMPERATURA

      Peça ao usuário uma temperatura em graus Celsius e mostre se está:
        - Abaixo de 0 → “Congelante”
        - Entre 0 e 30 → “Agradável”
        - Acima de 30 → “Quente”
''')

temp = int(input("Digite a temperatura atual: "))

if temp < 0:
    print(f"\nA temperatura {temp}° está CONGELANTE!")
elif temp >= 0 and temp <= 30:
    print(f"\nA temperatura {temp}° está AGRADÁVEL!")
else:
    print(f"\nA temperatura {temp}° está QUENTE!")