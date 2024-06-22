from user import Usuario,Admin
from utils import dump_json, verificar_cadastro, verificar_login,limpar

def tela_inicio():
    print('[1] Login')
    print('[2] Cadastro')
    print('[3] Sair')
    
def tela_login():
    nome = input('Digite o nome: ')
    senha = input('Digite a senha: ')
    
    # Verifica as credenciais de login
    login=verificar_login(nome, senha)
    
    if login is None:
        limpar()
        tela_cadastrar_loja()
    
    
def tela_cadastro():
    nome = input('Digite o nome: ')
    senha = input('Digite a senha: ')
    
    # Verifica se o nome de usuário já está cadastrado
    cadastro = verificar_cadastro(nome)
    
    if cadastro is False:
        return
    
    novo_usuario = Usuario(nome, senha)
    novo_usuario.id = len(cadastro) + 1
    
    cadastro.append({
        'id': novo_usuario.id,
        'nome': novo_usuario.nome,
        'senha': novo_usuario.senha,
        'lojas': novo_usuario.lojas
    })
    
    # Salva a lista atualizada de cadastros no arquivo JSON
    dump_json(cadastro)
    print('Usuário cadastrado com sucesso')
    
def tela_cadastrar_loja():
    nome_loja = input('Digite o nome da loja: ')
    Admin.cadastrar_loja(nome_loja)
    return


def tela_cadastrar_user():
    pass
