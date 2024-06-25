import json
from pathlib import Path
from os import path, system

json_path = Path(r'users.json')

# Função para criação de menus, comum no arquivo menu.py
def menu_base(titulo, opcoes):
    while True:
        limpar()
        print(titulo)
        for c, linhas in enumerate(opcoes, start=1):
            print(f'[{c}] {linhas[0]}')
                
        escolha = input('Escolha uma opção: ')
        
        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
            if opcoes[int(escolha)-1][1] is None:
                break
            else:
                opcoes[int(escolha)-1][1]()
        else:
            print('Valor inválido')
            input('Pressione enter para continuar...')



# Funções de Utilidade Geral
def limpar():
    return system('cls')

def add_item_lista(lista, item):
    if item not in lista:
        lista.append(item)
    else:
        return False

def remove_item_lista(lista, item):
    if item in lista:
        lista.remove(item)
    else:
        return False

def transacao_quantidade(produtos, produto, qtd, op):
    # Realiza uma transação (compra ou venda) de um produto
    for p in produtos:
        if p == produto:
            if op == '+':
                p.quantidade += qtd
            elif op == '-':
                p.quantidade -= qtd
            return True
    return False



# Funções para Manipulação de Arquivo JSON
def verificar_arquivo_json():
    # Verifica se o arquivo JSON existe e o cria se não existir
    if not path.exists(json_path):
        with open(json_path, 'w', encoding='utf-8') as file:
            file.write('[]')
    return True

def open_json(tipo):
    # Abre o arquivo JSON no modo especificado
    return open(json_path, tipo, encoding='utf-8')

def load_json():
    # Carrega os dados do arquivo JSON
    if verificar_arquivo_json():
        try:
            with open_json('r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []

def dump_json(dados):
    # Salva os dados no arquivo JSON
    with open_json('w') as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)



# Funções Específicas de Verificação e Manipulação de Dados
def verificar_login(nome, senha):

    dados = load_json()
    
    if not dados:
        print('Não há cadastros no JSON')
        return False
    
    for linha in dados:
        if linha['nome'] == nome and linha['senha'] == senha:
            return True
    
    print('Credenciais incorretas')
    return False

def verificar_cadastro(nome):
    dados = load_json()
    
    # Se não há dados, retorna uma lista vazia para iniciar o cadastro
    if not dados:
        return []

    for linha in dados:
        if linha['nome'] == nome:
            print('Usuário já cadastrado')
            input('Pressione enter para continuar...')
            return False

    # Retorna a lista de usuários cadastrados
    return dados