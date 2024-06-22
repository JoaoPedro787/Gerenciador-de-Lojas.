import json
from pathlib import Path
from os import path, system

json_path = Path(r'users.json')

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

def verificar_login(nome, senha):
    if nome == 'admin' and senha == 'admin':
        return True
    
    dados = load_json()
    
    if not dados:
        print('Não há cadastros no JSON')
        return False
    
    for linha in dados:
        if linha['nome'] == nome and linha['senha'] == senha:
            print('Logando...')
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
            return False

    # Retorna a lista de usuários cadastrados
    return dados
