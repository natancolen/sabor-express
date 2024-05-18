import os

restaurantes = [{'nome': 'Pizzaria das TTMN', 'categoria': 'italino', 'ativo': True},
                {'nome': 'Hot-Dog do Sonic', 'categoria': 'americano', 'ativo': True},
                {'nome': 'Lamen Uzumaki', 'categoria': 'japonsa', 'ativo': False}]

def exibir_nome_programa():
    print("""
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░      
      """)

def exibir_opcoes():
    '''
        Função quando chamada exibe uma lista de opções.
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alterar o estado do restaurante')
    print('4. Sair \n')

def finalizar_app():
    '''
        Função quando chamada finaliza a execução do app.
    '''
    exibir_subtitulos('Fializando app')

def opcao_invalida():
    '''
        Função quando chamada exibe uma mensagem de opção inválida.
    '''
    exibir_subtitulos('Opção inválida!')
    voltar_menu_principal()

def exibir_subtitulos(texto):
    '''
        Função quando chamada exibe subtitulo da opção escolhida.
    '''
    os.system('clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''
        Função quando cadastra um restaurante.
    '''
    exibir_subtitulos('Cadastrar de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input('Digite o nome da categoria do restaurante: ')

    dados_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_restaurante)

    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso')

    voltar_menu_principal()

def listar_restaurantes():
    '''
        Função quando chamada exibe  a lista de restaurantes cadastrado.
    '''
    exibir_subtitulos('Listar restaurantes')
    print(f'Nome do restaurante'. ljust(22), f'|categoria'.ljust(22), f'|estado')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}\n')

    voltar_menu_principal()

def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def alternar_estado_restaurante():
    '''
        Função quando chamada altera o estado do restaurante.
    '''
    exibir_subtitulos('Alterando estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_menu_principal()

def escolher_opcao():
    '''
        Função quando chamada você escolhe uma opção do app.
    '''
    try:
        opcao_escohilhida = int(input('Digite uma opção: '))
        print(f'Você escolheu a opção: {opcao_escohilhida}!')

        if opcao_escohilhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escohilhida == 2:
            listar_restaurantes()
        elif opcao_escohilhida == 3:
            alternar_estado_restaurante()
        elif opcao_escohilhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

