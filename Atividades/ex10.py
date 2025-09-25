# 10. Calculadora

print('''

      CALCULADORA SIMPLES

      Receba dois números inteiros e uma operação (+, -, *, /) digitada pelo usuário. 
      Use if-else para calcular e mostrar o resultado.
''')

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação matemática (+, -, * ou /): ")

if operacao == "+":
    print(f"\nO resultado da soma entre {num1} e {num2} é {num1 + num2}!")
elif operacao == "-":
    print(f"\nO resultado da subtração entre {num1} e {num2} é {num1 - num2}!")
elif operacao == "*":
    print(f"\nO resultado da multiplicação entre {num1} e {num2} é {num1 * num2}!")
elif operacao == "/":
    if num2 != 0:
        print(f"\nO resultado da divisão entre {num1} e {num2} é {num1 / num2}!")
    else:
        print("\nErro: não é possível dividir por zero!")
else:
    print("\nOperação inválida! Digite apenas +, -, * ou /.")