from user import Usuario
from admin import Admin
from utils import dump_json, verificar_cadastro, verificar_login, limpar

# Telas principais
def tela_inicio():
    print('[1] Login')
    print('[2] Sair')



# Telas de login e cadastro
def tela_login():
    nome = input('Digite o nome: ')
    senha = input('Digite a senha: ')
    
    login = verificar_login(nome, senha)
    
    if login:
        tela_produtos()
    
def tela_cadastro():
    nome = input('Digite o nome: ')
    senha = input('Digite a senha: ')
    
    cadastro = verificar_cadastro(nome)
    
    if cadastro is False:
        return
    
    novo_usuario = Usuario(nome, senha)
    novo_usuario.id = len(cadastro) + 1
    
    Admin.usuarios.append(novo_usuario)
    
    cadastro.append({
        'id': novo_usuario.id,
        'nome': novo_usuario.nome,
        'senha': novo_usuario.senha,
        'lojas': novo_usuario.lojas
    })
    
    dump_json(cadastro)
    print('Usuário cadastrado com sucesso')



# Telas para produtos
def tela_produtos():
    pass



# Telas para administração
def tela_admin():
    while True:
        limpar()
        print('[1] Cadastro de loja(s)')
        print('[2] Cadastro de usuário(s)')
        print('[3] Voltar')
        
        escolha = input('Digite uma opção: ')
        
        if escolha == '1':
            tela_gerenciar_lojas()
        elif escolha == '2':
            tela_gerenciar_usuarios()
        elif escolha == '3':
            break
        else:
            print("Opção inválida, tente novamente.")

def tela_gerenciar_lojas():
    while True:
        limpar()
        print('[1] Adicionar loja')
        print('[2] Remover loja')
        print('[3] Voltar')
        
        escolha = input('Digite uma opção: ')
        
        if escolha == '1':
            tela_cadastrar_loja()
        elif escolha == '2':
            tela_remover_loja()
        elif escolha == '3':
            break
        else:
            print("Opção inválida, tente novamente.")

def tela_gerenciar_usuarios():
    while True:
        limpar()
        print('[1] Adicionar usuário')
        print('[2] Remover usuário')
        print('[3] Voltar')
        
        escolha = input('Digite uma opção: ')
        
        if escolha == '1':
            tela_cadastro()
        elif escolha == '2':
            tela_remover_usuario()
        elif escolha == '3':
            break
        else:
            print("Opção inválida, tente novamente.")

def tela_cadastrar_loja():
    nome_loja = input('Digite o nome da loja: ')
    nova_loja = Admin.cadastrar_loja(nome_loja)
    if nova_loja:
        print('Loja cadastrada com sucesso!')
    else:
        print('Falha ao cadastrar a loja.')
    input('Pressione enter para continuar...')

def tela_remover_loja():
    nome_loja = input('Digite o nome da loja a ser removida: ')
    if Admin.remover_loja(nome_loja):
        print('Loja removida com sucesso!')
    else:
        print('Falha ao remover a loja.')
    input('Pressione enter para continuar...')

def tela_remover_usuario():
    nome_usuario = input('Digite o nome do usuário a ser removido: ')
    if Admin.remover_usuario(nome_usuario):
        print('Usuário removido com sucesso!')
    else:
        print('Falha ao remover o usuário.')
    input('Pressione enter para continuar...')