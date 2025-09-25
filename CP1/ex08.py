# 8. Verifica se um número é par, múltiplo de 5 ou outro número

print('''
      
      PAR OU MÚLTIPLO DE 5

      Solicite um número inteiro e verifique:
        - Se ele é par, escreva “Par”.
        - Senão, se for múltiplo de 5, escreva “Múltiplo de 5”.
        - Caso contrário, escreva “Outro número”.
''')

num = int(input("Digite um número: "))

if num % 2 == 0 and num % 5 == 0:
    print(f"\nO número {num} é par e múltiplo de 5.")
elif num % 2 == 0:
    print(f"\nO número {num} é par.")
elif num % 5 == 0:
    print(f"\nO número {num} é múltiplo de 5.")
else:
    print("Outro número.")