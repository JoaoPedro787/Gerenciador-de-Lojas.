from user import Usuario
from admin import Admin
from utils import dump_json, verificar_cadastro, verificar_login, limpar, menu_base


# Menus principais
def menu_inicio():
    limpar()
    
    print('[1] Login')
    print('[2] Sair')



# Menus de login e cadastro
def menu_login():
    limpar()
    
    nome = input('Digite o nome: ')
    senha = input('Digite a senha: ')
    
    login = verificar_login(nome, senha)
    
    if login:
        menu_produtos()
    else:
        input('Pressione enter para continuar...')

def menu_cadastro():
    limpar()
    
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
    input('Pressione enter para continuar...')



# Menus para produtos
def menu_produtos():
    
    menu_base(titulo='Menu de produtos', opcoes=[
        ('Cadastro de produto', menu_cadastro_produtos),
        ('Compra de produto', menu_gerenciar_produtos),
        ('Voltar', None)
    ])

def menu_cadastro_produtos():
    
    menu_base(titulo='Menu de cadastro de produto', opcoes=[
        ('Cadastrar produto', None),  # Desenvolvimento
        ('Remover produto', None),  # Desenvolvimento
        ('Voltar', None)
    ])

def menu_gerenciar_produtos():
    
    menu_base(titulo='Menu de gerenciar produto', opcoes=[
        ('Comprar produto', None),  # Desenvolvimento
        ('Vender produto', None),  # Desenvolvimento
        ('Voltar', None)
    ])



# Menus para administração
def menu_admin():
    
    menu_base(titulo='Menu de Admin', opcoes=[
        ('Cadastro de loja(s)', menu_gerenciar_lojas),
        ('Cadastro de usuário(s)', menu_gerenciar_usuarios),
        ('Voltar', None)
    ])

def menu_gerenciar_lojas():
    
    menu_base(titulo='Gerenciar lojas', opcoes=[
        ('Adicionar loja', menu_cadastrar_loja),
        ('Remover loja', menu_remover_loja),
        ('Voltar', None)
    ])

def menu_gerenciar_usuarios():
    
    menu_base(titulo='Gerenciar usuários', opcoes=[
        ('Adicionar usuário', menu_cadastro),
        ('Remover usuário', menu_remover_usuario),
        ('Voltar', None)
    ])

def menu_cadastrar_loja():
    limpar()
    
    nome_loja = input('Digite o nome da loja: ')
    nova_loja = Admin.cadastrar_loja(nome_loja)
    
    if nova_loja:
        print('Loja cadastrada com sucesso!')
    else:
        print('Falha ao cadastrar a loja.')
    input('Pressione enter para continuar...')

def menu_remover_loja():
    limpar()
    
    nome_loja = input('Digite o nome da loja a ser removida: ')
    
    if Admin.remover_loja(nome_loja):
        print('Loja removida com sucesso!')
    else:
        print('Falha ao remover a loja.')
    input('Pressione enter para continuar...')

def menu_remover_usuario():
    limpar()
    
    nome_usuario = input('Digite o nome do usuário a ser removido: ')
    
    if Admin.remover_usuario(nome_usuario):
        print('Usuário removido com sucesso!')
    else:
        print('Falha ao remover o usuário.')
    input('Pressione enter para continuar...')