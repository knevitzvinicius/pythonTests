def converteMes(mesNumero):
    mesesLongo = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    mesLongo = mesesLongo[int(mesNumero) - 1]
    return mesLongo

dia, mes, ano = input("Digite sua data de nascimento (DD/MM/YYYY):\n").strip().split("/")
idade = 2021 - int(ano)
mes = converteMes(mes)
if dia == "1":
    print(f"Você nasceu em 1º de {mes} de {ano} e tem {idade} anos")
else:
    print(f"Você nasceu no dia {dia} de {mes} de {ano} e tem {idade} anos")


