# Autores: Carlos Henrique De Godoy Santos; Inaldo pereira freitas
# Programa feito em 23/02/2024 

# Este código é um menu, onde o cliente escolhe uma das opções apresentadas e a quantidade desejada. 
# O programa calcula o valor final. Se a forma de pagamento for no débito, deve descontar 5% sobre o valor total. 
# Se a quantidade escolhida for maior que 5KG, o preço do produto aumenta, conforme apresentado no menu. 
# Não pode haver mais de uma compra por cliente, então após uma escolha ser feita, não há a opção do mesmo cliente comprar mais produtos. 
# Ao encerrar o dia, é retornado o resumo do dia, que calcula o valor final do caixa (quanto dinheiro entrou), 
# o total de clientes do dia e a média de valor gasto por cliente.


# Inicialização das variáveis
rep = 0  # Flag para repetição do loop principal
caixa = 0  # Total arrecadado no caixa
clientes = 0  # Contador de clientes atendidos
media = 0  # Média de vendas por cliente

# Loop principal do programa
while rep == 0:
    # Exibição do menu de opções
    print('''=-=-=-=-=-=-=-=-= MENU =-=-=-=-=-=-=-=-=-=-=-=-
                            ATÉ 5 KG                      ACIMA DE 5 KG
        FILE DUPLO        R$ 4,90 POR KG                R$ 5,80 POR KG 
        ALCATRA           R$ 5,90 POR KG                R$ 6,80 POR KG 
        PICANHA           R$ 6,90 POR KG                R$ 7,80 POR KG 

        [1] FILÉ DUPLO
        [2] ALCATRA
        [3] PICANHA 
        ''')

    # Loop para garantir que o usuário insira uma opção válida do menu
    while True:
        opc = int(input("Digite o tipo que deseja levar: "))
        if opc not in [1, 2, 3]:
            print("A OPÇÃO ESCOLHIDA NÃO ESTÁ NO MENU")
        else:
            break

    # Entrada da quantidade comprada pelo cliente
    qnt = float(input("Digite a quantidade comprada (em KG): "))

    # Verificação do tipo de carne escolhida e cálculo do preço
    if opc == 1:
        carne = 'FILÉ DUPLO'
        preco = 4.90 if qnt <= 5 else 5.80
        preco *= qnt
    elif opc == 2:
        carne = 'ALCATRA'
        preco = 5.90 if qnt <= 5 else 6.80
        preco *= qnt
    else:
        carne = 'PICANHA'
        preco = 6.90 if qnt <= 5 else 7.80
        preco *= qnt

    # Pergunta se a compra será realizada no débito
    print('''A COMPRA SERÁ REALIZADA NO DÉBITO? 
                [1] SIM 
                [2] NÃO ''')

    # Loop para garantir que o usuário insira uma opção válida para o método de pagamento
    while True:
        pag = int(input("SUA OPÇÃO: "))
        if pag not in [1, 2]:
            print("A OPÇÃO ESCOLHIDA NÃO ESTÁ NO MENU")
        else:
            break

    # Aplicação de desconto se o pagamento for feito no débito
    if pag == 1:
        desc = preco * 5 / 100
        preco_com_desconto = preco - desc
        print(F'''*****************CUPOM FISCAL******************
            CARNE: {carne}
            QUANTIDADE: {qnt} KG
            PREÇO: {preco + desc}
            CARTÃO DEBITO: SIM
            TOTAL COM DESCONTO: {preco_com_desconto}''')
    else:
        print(F'''*****************CUPOM FISCAL******************
            CARNE: {carne}
            QUANTIDADE: {qnt}KG
            PREÇO: {preco}
            CARTÃO DEBITO: NÃO
            TOTAL: {preco}''')

    # Atualização do total arrecadado no caixa e do número de clientes atendidos
    caixa += preco if pag == 2 else preco_com_desconto
    clientes += 1
    media = caixa / clientes

    # Menu para o usuário escolher entre atender o próximo cliente ou encerrar o dia
    print('''=-=-=-=-=-=-=-=-=-= HOME =-=-=-=-=-=-=-=-=-=-=
            [1] PROXIMO CLIENTE
            [2] ENCERRAR O DIA ''')

    # Loop para garantir que o usuário insira uma opção válida para o menu HOME
    while True:
        EscHome = int(input("SUA OPÇÃO: "))
        if EscHome not in [1, 2]:
            print("A OPÇÃO ESCOLHIDA NÃO ESTÁ NO MENU")
        else:
            break

    # Verificação se o usuário escolheu encerrar o dia
    if EscHome == 2:
        rep = 1

# Exibição do resumo do dia
print(F'''=-=-=-=-=-=-=-=-=-= RESUMO DO DIA =-=-=-=-=-=-=-=-=-=
    VALOR DO CAIXA: {caixa} 
    TOTAL DE CLIENTES: {clientes} 
    MEDIA DO DIA: {media}''')
