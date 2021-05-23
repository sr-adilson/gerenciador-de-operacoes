'''troca vírgula por ponto
define que so pode um ponto
transforma int em float caso necessáario
mostra a mensagem de erro caso necessário!
'''
def ppv(x):
    nx = x.replace(',', '.')
    if nx.count('.') == 0:
        fx = int(nx)
    else:
        fx = float(nx)
    return fx


def msv(k):
    mf = '{:.2f}'.format(k)
    dec = mf[-2:]
    intf = '{:,}'.format(int(k))
    antes = str(intf).replace(',', '.')
    fn = '{}{}{}'.format(antes, ',', dec)
    return fn


def ciclo(m):
    while True:
        try:
            v = ppv(str(input(m)))
            return v
        except ValueError:
            print('\nVocê digitou um ou mais caracteres inválidos. '
                  'Digite apenas número, separando as casa decimais com ponto ou vírgula!\n')
            continue

div = ('=' * 85)
''' Definição do conversor
Cria um looping para o sistema
Cadastra o nome do Usuário
Mostra as opções do menu de escolhas ao usuário
Executa o comando de câmbio
Define as opções de moedas
Define taxa
Transforma a moeda e a Taxa em Real
Faz a conversão para a moeda desejada
Mostra ao usuário o resultado
Retorna ao menu de escolhas 
Executa os Relatórios do Usuário 
'''
cadastro = True
while cadastro:
    cliente = str(input('Vamos fazer seu cadastro?\nQual o seu nome? '))
    print(div)
    condicao = True
    valor_total_operacoes = 0
    valor_total_taxas_cobradas = 0
    valor_base = 0
    valor_taxa_real = 0

    while condicao:
        print('Olá {},'.format(cliente))
        print('Para acessar o sistema escolha uma das opções abaixo:')
        print('      1 - Voltar ao cadastro')
        print('      2 - Câmbio')
        print('      3 - Relatório')
        opcao = ciclo('Digite a opção desejada: ')
        print(div)

        # Se opção inválida mensagem erro
        try:
            if 1 < opcao > 3:
                raise ValueError('Opção inválida!\n')
        except ValueError as error:
            print(error)

        # Se opção 0 volta para o cadastro
        if opcao == 1:
            condicao = False
            break
            # Se opção 2 executa o câmbio
        if opcao == 2:
            print('\nOpções de moeda')
            print('   1 - Dólar')
            print('   2 - Euro')
            print('   3 - Real\n')
            moeda_origem = ciclo('Escolha a moeda para troca: ')    #define a moeda que o usuário tem
            moeda_destino = ciclo('Para qual moeda deseja: ')       #define a moeda que o usuário deseja
            valor_original = ciclo('Digite o valor ')               #quantidade de moeda do usuário

            print(div)
            valor_taxa = valor_original * 0.10
            valor_taxado = valor_original - valor_taxa
            valor_dolar = 5.37                                      #Valores para conversão
            valor_euro = 6.54
            valor_real = 1.00

            # conversão de dólar para real com as taxas
            if moeda_origem == 1:
                valor_base = valor_taxado * valor_dolar
                valor_taxa_real = valor_taxa * valor_dolar

                # conversão de euro para real com as taxas
            if moeda_origem == 2:
                valor_base = valor_taxado * valor_euro
                valor_taxa_real = valor_taxa * valor_euro

            # Se for real so usa o valor taxado
            if moeda_origem == 3:
                valor_base = valor_taxado
                valor_taxa_real = valor_taxa

            # converte o real para dolar
            if moeda_destino == 1:
                valor_conversao = valor_base / valor_dolar
                print('{} o resultado da sua conversão ficou em US${:.2f}'.format(cliente, valor_conversao))
                print('E a taxa aplicada foi de R${:.2f}'.format(valor_taxa_real))


            # converte o real para euro
            if moeda_destino == 2:
                valor_conversao = valor_base / valor_euro
                print('{} o resultado da sua conversão ficou em €{:.2f}'.format(cliente, valor_conversao))
                print('A taxa aplicada foi de R${:.2f}'.format(valor_taxa_real))


            # mostra valor real na tela
            if moeda_destino == 3:
                valor_conversao = valor_base
                print('{} o resultado da sua conversão ficou em R${:.2f}'.format(cliente, valor_conversao))
                print('A taxa aplicada foi de R${:.2f}'.format(valor_taxa_real))
            print(div)

            # Opção 3 de relatório de operações mostra total de operações e total das taxas cobradas
        if opcao == 3:
            print('Digite a opção do relatório desejado: ')
            print('1 - Relatório total operações')
            print('2 - Relatório total taxas cobradas')
            opcao_relatorio = ciclo('Digite a opção desejada: ')
            print(div)
            if opcao_relatorio == 1:
                valor_total_operacoes = valor_total_operacoes + valor_base
                print('Valor total de operações e R${:.2f}'.format(valor_total_operacoes))
            else:
                valor_total_taxas_cobradas = valor_total_taxas_cobradas + valor_taxa_real
                print('Valor total de taxas cobradas e R${:.2f}'.format(valor_total_taxas_cobradas))
            print(div)
