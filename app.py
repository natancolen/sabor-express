import os

restaurantes = ['Pizzaria das TTMN', 'Cachorro quente Sonic', 'Lamen Uzumaki']

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
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')

def finalizar_app():
    exibir_subtitulos('Fializando app')

def opcao_invalida():
    exibir_subtitulos('Opção inválida!')
    voltar_menu_principal()

def exibir_subtitulos(texto):
    os.system('clear')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulos('Cadastrar de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')

    restaurantes.append(nome_do_restaurante)

    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso')

    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulos('Listar restaurantes')

    for restaurante in restaurantes:
        print(f'.{restaurante}\n')

    voltar_menu_principal()

def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu princiapl ')
    main()

def escolher_opcao():
    try:
        opcao_escohilhida = int(input('Digite uma opção: '))
        print(f'Você escolheu a opção: {opcao_escohilhida}!')

        if opcao_escohilhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escohilhida == 2:
            listar_restaurantes()
        elif opcao_escohilhida == 3:
            print('Ativar restaurante')
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

