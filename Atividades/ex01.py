# 1. Verifica se um número é positivo, negativo ou zero

print('''
      
      NÚMERO POSITIVO OU NEGATIVO

      Peça ao usuário um número inteiro e verifique se ele é positivo, negativo ou zero.
      
''')

num = int(input("Digite um número: "))
if num > 0:
    print(f"\nO número {num} é positivo.")
elif num < 0:
    print(f"\nO número {num} é negativo.")
else:
    print("\nO número é zero.")