# 5. Verifica qual número é maior

print('''
      
      COMPARAÇÃO DE DOIS NÚMEROS

      Peça dois números inteiros e informe qual deles é maior ou se são iguais.
''')

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número 2: "))

if num1 > num2:
    print(f"\nO primeiro número {num1} é maior que o segundo número {num2}!")
elif num1 == num2:
    print(f"\nO primeiro número {num1} é igual ao segundo número {num2}!")
else:
    print(f"\nO segundo número {num2} é maior que o primeiro número {num1}!")