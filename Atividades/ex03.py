# 3. Verifica se uma pessoa é maior ou menor de idade

print('''
      
      MAIORIDADE

      Solicite a idade de uma pessoa e mostre se ela é maior de idade (18 anos ou mais) ou menor de idade.
      
''')

idade = int(input("Digite a idade: "))
if idade >= 16:
    print("\nVocê é maior de idade.")
else:
    print("\nVocê é menor de idade.")