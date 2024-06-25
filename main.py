from menu import menu_inicio, menu_login,menu_admin

def main():
    while True:
        menu_inicio()
        
        escolha = input('Digite uma opção: ')
        
        if escolha == '1':
            menu_login()
                
        elif escolha == '2':
            exit()
        
        elif escolha.lower() == 'admin':
            menu_admin()
        
        else:
            print('Opção incorreta')
            input('Pressione enter para continuar...')
            

if __name__ == '__main__':
    main()