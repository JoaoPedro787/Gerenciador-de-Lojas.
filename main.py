from terminal import tela_inicio,tela_login,tela_cadastro

def main():
    tela_inicio()
    
    escolha=input('Digite uma opção: ')
    
    if escolha=='1':
        if tela_login():
            tela_cadastro()
            
    elif escolha=='2':
        tela_cadastro()

if __name__=='__main__':
    main()