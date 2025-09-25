# 7. Verifica se o usuário e a senha estão corretos para login

print('''
      
      LOGIN SIMPLES

      Peça um nome de usuário e uma senha. Se o usuário for "admin" e a senha "1234", exiba “Acesso permitido”; caso contrário, “Acesso negado”.
''')

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == "admin" and senha == "1234":
    print("\nAcesso permitido!")
else:
    print("\nAcesso negado...")