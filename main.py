'''
Nome: MATHEUS RAMON PRADO
Curso: ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
16/06/2025
'''

def menu_principal ():
    print(f'  \nMenu Principal ')
    print(f'1 - ALUNOS')
    print(f'2 - DISCIPLINAS ')
    print(f'3 - MATRÍCULAS')
    print(f'4 - TURMAS')
    print(f'5 - PROFESSORES')
    print(f'0 - SAIR')
    print('')


def menu_operacional():
    print(f'  \nMenu Operacional: ALUNOS ')
    print(f'1 - ADICIONAR')
    print(f'2 - LISTAGEM')
    print(f'3 - ATUALIZAR')
    print(f'4 - EXCLUIR')
    print(f'5 - MENU PRINCIPAL')
    print('')


def adicionar_aluno():
    cadastro = {}
    try:
        cadastro['codigo'] = int(input('Digite o código do aluno: '))
    except ValueError:
        print('Código inválido. Digite um número.')
        return  # encerra a função sem adicionar

    cadastro['nome'] = input('Digite o nome do aluno: ')
    cadastro['cpf'] = input('Digite o CPF do aluno: ')

    if cadastro['nome'].strip():
        alunos.append(cadastro)
        print(f"\nAluno: Cód. de cadastro {cadastro['codigo']} - Nome: {cadastro['nome']} - CPF: {cadastro['cpf']} adicionado!")
    else:
        print('O nome está vazio!')


def listagem_alunos():
    if not alunos:
        print('Nenhum aluno cadastrado.')

    else:
        # Mostra todos os dados do alunos
        for i, aluno in enumerate(alunos, start=1):  # Para a variavel 'nome' na lista 'estudantes' aparecera cada elemento
            print(f"\nAluno: Cód. de cadastro {aluno['codigo']} - Nome: {aluno['nome']} - CPF: {aluno['cpf']} adicionado!")
        input('Pressione Enter para voltar ao menu.')


def atualizando_alunos():
    if not alunos:
        print('\nNenhum aluno cadastrado para atualizar.')
        return

    # Lista os alunos para atualização
    for i, estudante in enumerate(alunos, start=1):
        print(f"\n{i}- Código: {estudante['codigo']} - Nome: {estudante['nome']} - CPF: {estudante['cpf']}")
    try:
        indice = int(input('Digite o número do estudante que deseja atualizar: '))

        if 1 <= indice <= len(alunos):
            # Acessa o estudante pelo índice
            estudante_para_atualizar = alunos[indice - 1]
            print(f"Atualizando estudante: {estudante_para_atualizar['nome']}")

            # Atualizar o código
            novo_codigo_str = input(f"Digite o novo código ({estudante_para_atualizar['codigo']}): ")
            if novo_codigo_str.strip():  # Verifica se o input não está vazio
                try:
                    estudante_para_atualizar['codigo'] = int(novo_codigo_str)
                except ValueError:
                    print("Código inválido.")

            # Atualizar o nome
            novo_nome = input(f"Digite o novo nome ({estudante_para_atualizar['nome']}): ").strip()
            if novo_nome:  # Verifica se o nome não está vazio
                estudante_para_atualizar['nome'] = novo_nome

            # Atualizar o CPF
            novo_cpf = input(f"Digite o novo CPF ({estudante_para_atualizar['cpf']}): ").strip()
            if novo_cpf:  # Verifica se o CPF não está vazio
                estudante_para_atualizar['cpf'] = novo_cpf

            print(f"\nAluno atualizado com sucesso!")
        else:
            print('Número inválido.')
    except ValueError:
        print('Digite um número válido.')



def excluindo_alunos():
    if not alunos:
        print('\nNenhum estudante cadastrado para excluir.')
        return
    # Lista os estudantes para exclusão
    for i, estudante in enumerate(alunos, start=1):
        print(f"{i}- Código: {estudante['codigo']} - Nome: {estudante['nome']} - CPF: {estudante['cpf']}")
    try:
        indice = int(input('Digite o número do estudante que deseja excluir: '))
        if 1 <= indice <= len(alunos):
            removido = alunos.pop(indice - 1)
            print(f"Estudante '{removido['nome']}' excluído com sucesso.")
        else:
            print('Número inválido.')
    except ValueError:
        print('Digite um número válido.')








#Criar as listas antes de tudo para que não seja apagada
alunos = []


while True: #Esse primeiro 'while' é para a operação não ser finalizada
    #Menu Principal
    menu_principal()

    #Primeira escolha do Usuário
    try:
        opcao1 = int(input(f'Digite o número referente a categoria: '))
    except ValueError:
        print('Escolha um número válido!')
        continue


    if opcao1 == 1:
        print(f'\nVocê escolheu a opção: {opcao1}')



        while True: #O segundo é para que não fique apenas no menu principal e continue no Segundo ate que o usuario queira sair
            # Segundo Menu
            if opcao1 == 1:
                menu_operacional()


            # Segunda escolha do usuário
            try:
                opcao2 = int(input('Digite uma opção válida: '))
            except ValueError:
                print('Escolha um número válido de 1 - 5!')
                continue


#ADICIONAR ALUNOS
            if opcao2 == 1:
               print('\nCADASTRAR ALUNOS')
               adicionar_aluno()


#LISTAR ALUNOS
            elif opcao2 == 2:
                print('\nLISTAGEM DE ALUNOS')
                listagem_alunos()


#ATUALIZAR ALUNOS

            elif opcao2 == 3:
                print('\nATUALIZAR DADOS DE ALUNOS')
                atualizando_alunos()


#EXCLUIR ALUNOS
            elif opcao2 == 4:
                print('\nEXCLUIR ALUNOS')
                excluindo_alunos()



#VOLTAR PARA O MENU PRINCIPAL
            elif opcao2 == 5:
                break #Esse break serve para parar o loop do segundo menu e assim voltar para o menu principal

            else:
                print(f'\nOpção inválida, tente novamente!')
                print('')

    elif opcao1 >= 2 and opcao1 <= 5:
        print(f'Você escolheu a opção:{opcao1}')
        print(f'EM DESENVOLVIMENTO..')
        print('')

    elif opcao1 == 0:
        print(f'\nSaindo..')
        break #Como esse break esta junto com o menu principal que é a base de tudo, ele encerra todo o processo

    else:
        print(f'Opcão inválida, tente novamente!')




