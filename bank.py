from datetime import datetime

menu = """ 

    [d] Deposito
    [s] Saque
    [e] Extrato
    [q] Sair

==> """

saldo = 0
limite = 500
extrato = ""
saques = 0 
LIMITE_SAQUES = 3

while True:
    option = input(menu)
    if option == 'd':
        value = input("Qual Valor do Deposito?\n")
        if value.isdigit() == True:
            saldo += float(value)
            extrato += f" --- {datetime.today().strftime('%Y-%m-%d %H:%M')} - Deposito: R$ {value} -- \n --- Saldo: R$ {saldo} ---\n"
        else:
            print("Digite apenas números!")
            
    elif option == 's':
        value = input("Qual Valor do Saque? \n")
        if value.isdigit() == True:
            value = float(value)
            if value <= limite:
                if saques <= LIMITE_SAQUES:
                    if value <= saldo:
                        saldo -= value
                        saques += 1
                        extrato += f" --- {datetime.today().strftime('%Y-%m-%d %H:%M')} - Saque: R$ {value} -- \n --- Saldo: R$ {saldo} ---\n"
                    else:
                        print("Saldo Insuficiente!")
                else:
                    print("Limite de saques diario atingido! Tente amanhã.")
            else:
                print("O valor solicitado está acima do limite permitido!")
        else:
            print("Digite apenas números!")
    elif option == 'e':
        print(extrato)
    elif option == 'q':
        break