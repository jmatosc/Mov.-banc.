
import datetime
operacoes =["Sacar","Depositar","Extrato","Encerrar atendimento"]
saldo = float(0)
historico = []
data_hoje=datetime.datetime.now()
data_hoje=data_hoje.strftime("%d-%m-%Y")
total = 0
extrato = "" 
     
def imprimir_extrato():
    global extrato
    for extrato in historico:
        print(extrato)
for indice, valor in enumerate(operacoes):
    menu = (f"{indice} {valor}")
    print(menu)
while True:  
    respcli = int(input("Selecione a transação que deseja realizar:"))    
    if respcli == 0:
        valorsaque = float(input(f"Transação {operacoes[0]} selecionada.\nInforme o valor que deseja sacar:"))
        if valorsaque > 500.00:
            print("Valor de saque excedido")
        elif valorsaque > saldo:
            print (f"Saldo insuficiente, seu saldo atual é de: R$ {saldo:.2f}")
        elif total > 3:
            print('Limite de saque diário atigido')
        else:
            saldo -= valorsaque
            data_saque = datetime.datetime.now() 
            data_saque = data_saque.strftime("%d-%m-%Y")
            extrato += f"Saque\n Data: {data_saque} \n Valor do Saque: R$ {valorsaque:.2f}\n"
            print("Transação realizada com sucesso")
            total +=1          
    if respcli == 1:
        valordeposito = float(input(f"Transação {operacoes[1]} selecionada.\nInforme o valor que deseja depositar:"))
        if valordeposito > 0:
            saldo += valordeposito
            data_deposito = datetime.datetime.now() 
            data_deposito = data_deposito.strftime("%d-%m-%Y")
            extrato += f"Deposito\n Data: {data_deposito} \n Valor do Deposito: R$ {valordeposito:.2f}\n"
    if respcli == 2:
        print(f"Transação {operacoes[2]} selecionada.\n")
        print("############## EXTRATO #############")
        print(extrato)
        print(f"Saldo total é de: R${saldo:.2f}")

    elif respcli==3:
        print("Atendimento encerrado.")
        break


            
