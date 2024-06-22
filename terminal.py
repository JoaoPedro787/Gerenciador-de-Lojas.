from user import Usuario
from utils import load_json,dump_json,verificar_dados

def tela_inicio():
    print('[1] Login')
    print('[2] Cadastro')
    print('[3] Sair')
    
def tela_login():
    nome=input('Digite o nome: ')
    senha=input('Digite a senha: ')
    
    login=verificar_dados(nome,login=True)

def tela_cadastro():
    nome = input('Digite o nome: ')
    senha = input('Digite a senha: ')
    
    cadastro = verificar_dados(nome, login=False)
    
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
    
    dump_json(cadastro)
    print('Usuário cadastrado com sucesso')