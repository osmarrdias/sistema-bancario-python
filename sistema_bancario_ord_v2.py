from datetime import datetime

saldo = 0.00
limite = 500.00
extrato = ""
numero_saques = 0
numero_transacoes = 0
LIMITE_SAQUES = 3
LIMITE_TRANSACOES = 10
cadastro_clientes = {}
cadastro_contas = {}
contador = 0

def menu():
    menu = """
Por favor selecione a opção desejada:

 [c1] Cadastrar Cliente
 [l1] Listar Clientes
 [c2] Cadastrar Conta
 [l2] Listar Contas
 [d] Depositar
 [s] Sacar
 [e] Extrato
 [q] Sair

"""
    return menu

def sequencia_conta():
    global contador
    contador += 1
    return contador

def data_hora():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def cadastrar_cliente(nome, data_nascimento, cpf, endereco):
    valida_cpf = cpf in cadastro_clientes
    if valida_cpf == False:
        cadastro_clientes.update({cpf:{"nome":nome,"data_nascimento":data_nascimento,"endereco":endereco}})
        print("Cliente cadastrado com sucesso!")
        return cadastro_clientes
    else:
        print("Já existe um cliente cadastrado com este CPF!")
 
def listar_clientes():
    conta_clientes = len(cadastro_clientes)
    if conta_clientes == 0:
        print(f"Ainda não existem clientes cadastrados!")
    else:
        lista_clientes = ""
        print((f" Lista de Clientes ").center(50,"#"))
        for cpf, dados in cadastro_clientes.items():   
            lista_clientes += (f"CPF: {cpf}\n")
            lista_clientes += (f"Nome: {dados['nome']}\n")
            lista_clientes += (f"Data de Nascimento: {dados['data_nascimento']}\n")
            lista_clientes += (f"Endereço: {dados['endereco']}\n")
            lista_clientes += (f"-" * 50)
            lista_clientes += (f"\n")
        print(lista_clientes)

def cadastrar_conta(cliente, agencia, nro_conta):
    valida_conta = nro_conta in cadastro_contas
    if valida_conta == False:
        cadastro_contas.update({nro_conta:{"cliente":cliente,"agencia":agencia}})
        print("Conta cadastrada com sucesso!")
        return cadastro_contas
    else:
        print("Já existe uma conta cadastrada com este número!")

def listar_contas():
    conta_contas = len(cadastro_contas)
    if conta_contas == 0:
        print(f"Ainda não existem contas cadastradas!")
    else:
        lista_contas = ""
        print((f" Lista de Contas ").center(50,"#"))
        for conta, dados in cadastro_contas.items():
            lista_contas += (f"Conta: {conta}\n")
            lista_contas += (f"Agência: {dados['agencia']}\n")
            lista_contas += (f"CPF: {dados['cliente']}\n")
            lista_contas += (f"-" * 50)
            lista_contas += (f"\n")
        print(lista_contas)

def depositar(numero_transacoes, LIMITE_TRANSACOES, saldo, extrato, /):
    if numero_transacoes >= LIMITE_TRANSACOES:
        print(f"Já foram realizadas todas as transações permitidas para hoje ({LIMITE_TRANSACOES}). Por favor retorne amanhã.")
    else:
        try:
            valor_deposito = float(input("Por favor informe o valor a ser depositado: "))
            if valor_deposito <= 0:
                print("O valor do depósito deve ser maior do que R$ 0,00. Por favor revise o valor e tente novamente!")
            else:
                saldo += valor_deposito
                numero_transacoes += 1
                extrato += (f"{data_hora()}") + (f"{valor_deposito:.2f} +\n").rjust(20," ")
                print(f"\nDepósito realizado com sucesso! R$ {valor_deposito:.2f}!")
        except ValueError:
            print(f"Valor inválido! Digite apenas números (use ponto para decimais).")
    return saldo, extrato, numero_transacoes


def sacar(*, saldo, extrato, limite, numero_saques, LIMITE_SAQUES, numero_transacoes, LIMITE_TRANSACOES):
    if numero_transacoes >= LIMITE_TRANSACOES:
        print(f"Já foram realizadas todas as transações permitidas para hoje ({LIMITE_TRANSACOES}). Por favor retorne amanhã.")
    else:
        if numero_saques >= LIMITE_SAQUES:
            print(f"Já foram realizados todos os saques permitidos para hoje ({LIMITE_SAQUES}). Por favor retorne amanhã.")
        else:              
            try: 
                valor_saque = float(input("Por favor informe o valor a ser sacado: "))
                if valor_saque <= 0:
                    print("O valor do saque deve ser maior do que R$ 0,00. Por favor revise o valor e tente novamente!")
                else:
                    if valor_saque > saldo:
                        print(f"Saldo insuficiente para realizar a operação!") 
                    elif valor_saque > limite:
                        print(f"Saque superior ao limite de transação!")                 
                    else:
                        numero_saques += 1
                        numero_transacoes += 1
                        saldo -= valor_saque
                        extrato += (f"{data_hora()}") + (f"{valor_saque:.2f} -\n").rjust(20," ")
                        print(f"\nSaque realizado com sucesso! R$ {valor_saque:.2f}!")
            except ValueError:
                print(f"Valor inválido! Digite apenas números (use ponto para decimais).")
    return saldo, extrato, numero_saques, numero_transacoes


def ver_extrato(saldo, /, *, extrato):
    print()
    print((f" Extrato Atualizado ").center(50,"#")+"\n")
    if extrato == "":
        print("Não foram realizadas movimentações!\n")
    else:
        print(f"{extrato}")
    print((f"Saldo da Conta: R$ {saldo:.2f}") + "\n")
    print((f"").center(50,"#"))
    return saldo, extrato



while True:

    opcao = input(menu())

    if opcao == "c1":
        
        contador_validacao_cpf = 0
        while contador_validacao_cpf == 0:
            try:
                cpf = int(input("Por favor informe o número do seu CPF: "))
                contador_validacao_cpf += 1
            except ValueError:
                contador_validacao_cpf = 0
                print(f"CPF inválido! Digite apenas números.")   
        
        nome = input("Por favor informe seu nome: ")
        
        contador_validacao_nascimento = 0
        while contador_validacao_nascimento == 0:
            data_nascimento = input("Por favor informe sua data de nascimento (dd/mm/aaaa): ")
            try:
                data = datetime.strptime(data_nascimento, "%d/%m/%Y")
                contador_validacao_nascimento += 1
            except ValueError:
                print("Data inválida. Por favor digite no formato dd/mm/aaaa")
                contador_validacao_nascimento = 0           
        
        endereco = input("Por favor informe o seu endereço: ")
        cadastrar_cliente(nome, data_nascimento, cpf, endereco)
        #print(cadastro_clientes)

    elif opcao == "l1":
        listar_clientes()

    elif opcao == "c2":
        
        contador_validacao_cpf = 0
        while contador_validacao_cpf == 0:
            try:
                cpf = int(input("Por favor informe o número do seu CPF: "))
                # Verificando se o CPF está cadastrado como cliente
                valida_cliente = cpf in cadastro_clientes
                if valida_cliente == False:
                    print(f"Cliente não cadastrado. Por favor informe um CPF válido.")
                    contador_validacao_cpf = 0
                else:
                    contador_validacao_cpf += 1
            except ValueError:
                contador_validacao_cpf = 0
                print(f"CPF inválido! Digite apenas números.")   
        
        agencia = "0001"
        print(f"Agência: {agencia}")
        
        conta = sequencia_conta()
        print(f"Conta: {conta}")

        cadastrar_conta(cpf, agencia, conta)
        #print(cadastro_contas)

    elif opcao == "l2":
        listar_contas()

    elif opcao == "d":
        saldo, extrato, numero_transacoes = depositar(numero_transacoes, LIMITE_TRANSACOES, saldo, extrato)
        saldo, extrato = ver_extrato(saldo, extrato=extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques, numero_transacoes = sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques,LIMITE_SAQUES=LIMITE_SAQUES, numero_transacoes=numero_transacoes, LIMITE_TRANSACOES=LIMITE_TRANSACOES)
        saldo, extrato = ver_extrato(saldo, extrato=extrato)

    elif opcao == "e":
        saldo, extrato = ver_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        print(f"Obrigado por utilizado nossos serviços. Volte sempre!!!")
        break

    else:
        print(f"Operação inválida, por favor verifique as opções do menu e tente novamente.")