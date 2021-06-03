dia, mes, ano = input("Digite sua data de nascimento (DD/MM/YYYY):\n").strip().split("/")
idade = 2021 - int(ano)
if dia == "1":
    print(f"Você nasceu em 1º de {mes} de {ano} e tem {idade} anos")
else:
    print(f"Você nasceu no dia {dia} de {mês} de {ano} e tem {idade} anos")

#def converteMes(mesNumero)
#    mesesLongo = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
#    mesLongo = mesesLongo[mesNumero]
#    return mesLongo
