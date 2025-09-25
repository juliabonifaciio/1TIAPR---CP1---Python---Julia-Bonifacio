# 6. Calcula desconto em produto

print('''
      
      DESCONTO EM PRODUTO

      Receba o valor de um produto e mostre o preço final com desconto de 10% se o valor for maior que 100; caso contrário, mostre o preço sem desconto.
''')

valor = float(input("Digite o valor da sua compra: "))
desconto = valor * 0.10
valor_total = valor - desconto

if valor >= 100:
    print(f"\nO valor da sua compra é de {valor_total} com 10% de desconto.")
else:
    print(f"\nO valor da sua compra é de {valor}.")