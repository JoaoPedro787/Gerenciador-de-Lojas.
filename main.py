from terminal import tela_inicio, tela_login, tela_cadastro
from utils import limpar

def main():
    while True:
        limpar()
        tela_inicio()
        
        escolha = input('Digite uma opção: ')
        
        if escolha == '1':
            limpar()
            tela_login()
            input('Pressione enter para continuar...')
                
        elif escolha == '2':
            limpar()
            tela_cadastro()
            input('Pressione enter para continuar...')
        
        elif escolha == '3':
            exit()
        
        else:
            print('Opção inválida')
            input('Pressione enter para continuar...')

if __name__ == '__main__':
    main()