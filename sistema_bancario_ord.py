from datetime import datetime

menu = """
Por favor selecione a opção desejada:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

def data_hora():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

saldo = 0.00
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def ver_extrato():
    print((f" Extrato Atualizado ").center(50,"#")+"\n")
    if extrato == "":
        print("Não foram realizadas movimentações!\n")
    else:
        print(f"{extrato}")
    print((f"Saldo da Conta: R$ {saldo:.2f}") + "\n")
    print((f"").center(50,"#"))

while True:

    opcao = input(menu)

    if opcao == "d":
        try:
            valor_deposito = float(input("Por favor informe o valor a ser depositado: "))
            if valor_deposito <= 0:
                print("O valor do depósito deve ser maior do que R$ 0,00. Por favor revise o valor e tente novamente!")
            else:
                saldo += valor_deposito
                extrato += (f"{data_hora()}") + (f"{valor_deposito:.2f} +\n").rjust(20," ")
                print(f"Depósito realizado com sucesso! R$ {valor_deposito:.2f}!")
        except ValueError:
            print(f"Valor inválido! Digite apenas números (use ponto para decimais).")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print(f"Já foram realizados todos os saques permitidos para hoje. Por favor retorne amanhã.\n")
            ver_extrato()
            break
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
                        saldo -= valor_saque
                        extrato += (f"{data_hora()}") + (f"{valor_saque:.2f} -\n").rjust(20," ")
                        print(f"Saque realizado com sucesso! R$ {valor_saque:.2f}!")                 
            except ValueError:
                print(f"Valor inválido! Digite apenas números (use ponto para decimais).")

    elif opcao == "e":
        ver_extrato()

    elif opcao == "q":
        print(f"Obrigado por utilizado nossos serviços. Volte sempre!!!")
        break

    else:
        print(f"Operação inválida, por favor verifique as opções do menu e tente novamente.")