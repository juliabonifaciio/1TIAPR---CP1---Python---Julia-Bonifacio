# 4. Verifica se um aluno foi aprovado ou reprovado

print('''
      
      NOTA DE APROVAÇÃO

      Receba a nota de um aluno (0 a 10) e diga se ele foi aprovado (nota ≥ 6) ou reprovado.
''')

nota = int(input("Digite sua nota: "))

if nota >= 6:
    print(f"\nParabéns, você foi aprovado com nota {nota}!")
else:
    print(f"\nInfelizmente você foi reprovado com nota {nota}. Tente novamente no próximo semestre! :)")