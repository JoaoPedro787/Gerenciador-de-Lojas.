from user import Usuario
from utils import load_json,dump_json

def tela_inicio():
    print('[1] Login')
    print('[2] Cadastro')
    print('[3] Sair')
    
def tela_login():
    nome=input('Digite o nome: ')
    senha=input('Digite a senha: ')
    
    if nome and senha=='admin':
        return True

def tela_cadastro():
    nome=input('Digite o nome: ')
    senha=input('Digite a senha: ')
    
    dados=load_json()
    
    for linha in dados:
        if linha['nome']==nome:
            print('Usúario já cadastrado')
            return False
            
    novo_usuario = Usuario(nome, senha)
    novo_usuario.id = len(dados) + 1  # Atribui um ID simples baseado no número de usuários
    
    
    
    dados.append({
        'id': novo_usuario.id,
        'nome': novo_usuario.nome,
        'senha': novo_usuario.senha,
        'lojas': novo_usuario.lojas
    })
    
    dump_json(dados)
    print('Usuário cadastrado com sucesso')