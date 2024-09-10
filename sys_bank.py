import os

os.system('cls')
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    print('''
        1 - Extrato
        2 - Deposito
        3 - Saque
        4 - Sair
        ''')
    opcao = input('Selecione a opçao desejada: ')
    if opcao == '1':
        os.system('cls')
        print('#'.center(70,"#"))
        if not extrato:
            texto =f' Nao foram realizadas transaçoes. Seu saldo atual é de: R${saldo:.2f} '
            print(texto.center(70," "))
        else:
            print(extrato)
            texto = f' Seu saldo atual é de: R${saldo:.2f} '
            print(texto.center(70," "))
        print('#'.center(70,"#"))
    elif opcao == '2':
        valor = float(input('Informe o valor a ser depositado: '))

        if valor > 0:
            saldo += valor
            os.system('cls')
            print('#'.center(70,"#"))
            texto = f' Deposito de R$ {valor:.2f} feito. '
            extrato += f' Deposito = R$ {valor:.2f} \n'
            print(texto.center(70," "))
            print('#'.center(70,"#"))

        else:
            os.system('cls')
            print('#'.center(70,"#"))
            texto = ' Não foi possivel concluir essa operação '
            print(texto.center(70," "))
            print('#'.center(70,"#"))
    elif opcao == '3':
        valor = float(input('Informe o valore que deseja sacar:'))

        if (valor > 0):
            if numero_saques < LIMITE_SAQUES:
                if not valor > saldo:
                    saldo = saldo - valor
                    os.system('cls')
                    print('#'.center(70,"#"))
                    texto = ' Valor debitado da sua conta. '
                    extrato += f' Saque = - R$ {valor:.2f} \n'
                    print(texto.center(70," "))
                    print('#'.center(70,"#")) 
                    numero_saques += 1
                else:
                    os.system('cls')
                    print('#'.center(70,"#"))
                    texto = ' Voce não pode sacar essa quantidade. Saldo insuficiente '
                    print(texto.center(70," "))
                    print('#'.center(70,"#"))   
            else:
                os.system('cls')
                print('#'.center(70,"#"))
                texto = ' Seu limite diario de saques foi exedido '
                print(texto.center(70," "))
                print('#'.center(70,"#"))   
        else:
            os.system('cls')
            print('#'.center(70,"#"))
            texto = ' Não foi possivel concluir essa operação '
            print(texto.center(70," "))
            print('#'.center(70,"#"))
            
    elif opcao == '4':
        break
    else:
        os.system('cls')
        print('#'.center(70,"#"))
        texto = ' Verifique a lista de opções e selecione uma opção valida. '
        print(texto.center(70," "))
        print('#'.center(70,"#"))