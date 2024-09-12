conta = 0
extrato = ""
limitesaq = 0
#função para depositar
def depositar(cont,val):
    valido = False
    #se o valor do deposito for negativo não vai depositar
    if val<0:
        print("Depósito invalido")
    else:
        valido = True
    # se o deposito for valido vai adicionar na conta e adicionar ao extrato a operação
    if (valido == True):
        global extrato
        extrato += f"Depósito com valor de R$ {val}\n"
        return cont + val
    else:
        return cont
#função para sacar
def sacar(cont,val):
    valido = False
    global limitesaq
    #se o valor de saque for menor que o valor na conta
    #e o valor for maior que zero e menor ou igual a 500 e o usuario ainda não tenha feito 3 saques
    #será valido o saque
    if (cont>val and val>0 and val<= 500 and limitesaq < 3):
        valido = True
        limitesaq += 1
    #se o valor da conta for menor que o valor de saque
    if cont<val:
        print("Valor de saque maior que valor na conta")
    #se o valor do saque for menor que 0
    if (val<0):
        print("Valor de saque invalido")
    #se o limite de saque for alcançado
    if limitesaq >= 3:
        print("Limite de saque alcançado")
    #se o saque for valido adiciona no extrato a operação e subtrai da conta o valor
    if valido == True:
        global extrato
        extrato += f"Saque com valor de R$ {val}\n"
        return conta - val
    else:
        return cont

#parte principal do programa
while True:
    print('''
    ######-Menu-######
    |   (1)-Depósito |
    |   (2)-Saque    |
    |   (3)-Extrato  |
    |   (4)-Sair     |  
    ######-Menu-######
    ''')
    op = int(input())
    #se opção 4 for escolhida o programa acaba
    if op == 4:
        break
    #se opção 1 for escolhida o programa irá depositar
    if op == 1:
        dep = float(input("De quanto será o depósito?"))
        conta = depositar(conta,dep)
    #se opção 2 for escolhida o programa irá sacar
    if op == 2:
        saq = float(input("De quanto será o saque?"))
        conta = sacar(conta,saq)
    #se opção 3 for escolhida o programa irá imprimir o extrato
    if op == 3:
        print(f'''
        ########################################-Extrato-########################################
        \n
        {extrato}
        Saldo atual da conta R$ {conta}          
        ########################################-Extrato-########################################
        ''')