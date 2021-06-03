dia, mes, ano = input("Insira sua data de nascimento:\n").strip().split("/")
idade = 2021 - int(ano)
print(f"Você nasceu em {dia} de {mes} de {ano} e tem {idade} anos")
