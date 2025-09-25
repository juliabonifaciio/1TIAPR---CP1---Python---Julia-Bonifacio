# 2. Verifica se um número é par ou ímpar

print('''
      
      PAR OU ÍMPAR

      Receba um número inteiro e verifique se ele é par ou ímpar.
      
''')

num = int(input("Digite um número: "))
if num % 2 == 0:
    print(f"\nO número {num} é par.")
else:
    print(f"\nO número {num} é ímpar.")