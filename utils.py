import json
from pathlib import Path
from os import path

json_path=Path(r'users.json')

def add_item_lista(lista,item):
    if item not in lista:
        lista.append(item)
    else:
        return False

def remove_item_lista(lista,item):
    if item in lista:
        lista.remove(item)
    else:
        return False
    
def transacao_quantidade(produtos, produto, qtd, op):
    for p in produtos:
        if p == produto:
            if op == '+':
                p.quantidade += qtd
            elif op == '-':
                p.quantidade -= qtd
            return True
    return False

def verificar_arquivo_json():
    if not path.exists(json_path):
        with open_json('w') as file:
            file.write('')
            
    return True

def open_json(tipo):
    return open(json_path,tipo,encoding='utf-8')
            

def load_json():

    if verificar_arquivo_json():
        try:
            with open_json('r') as file:
                return json.load(file)
                            
        except json.JSONDecodeError:
            return []

def dump_json(dados):
    with open_json('w') as file:
        json.dump(dados,file,indent=4,ensure_ascii=False)
        
def verificar_dados(variavel, login):
    dados = load_json()
    
    if not dados:
        if login:
            print('Não há cadastros no JSON')
            return False
        else:
            dados = []
            return dados
    else:
        for linha in dados:
            if linha['nome'] == variavel:
                if login:
                    print('Logando...')
                    return True
                else:
                    print('Usuário já cadastrado')
                    return False
        return dados
        