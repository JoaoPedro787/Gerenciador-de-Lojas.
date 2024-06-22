from utils import add_item_lista, remove_item_lista
from loja import Loja

class Usuario:
    
    def __init__(self, nome, senha):
        self.id = None
        self.nome = nome
        self.senha = senha
        self.lojas = []
    
    def _adicionar_loja(self, loja):
        add_item_lista(self.lojas, loja)

    def _remover_loja(self, loja):
        remove_item_lista(self.lojas, loja)
    
    def compra_estoque_qtd_produto(self, produto, loja, qtd):
        if loja in self.lojas:
            # Chama o método de compra de produto na loja
            loja.compra_produto(produto, qtd)
        
    def venda_estoque_qtd_produto(self, produto, loja, qtd):
        if loja in self.lojas:
            # Chama o método de venda de produto na loja
            loja.venda_produto(produto, qtd)

class Admin:
    lojas=[]

    @classmethod
    def cadastrar_loja(cls,nome_loja):
        
        if nome_loja not in (loja.nome for loja in cls.lojas):
            nova_loja = Loja(nome_loja)
            add_item_lista(cls.lojas,nova_loja)
            print('Loja cadastrada')
            
        else:
            print('Loja já cadastrada')
            return False
    
    def adicionar_usuario_na_loja(self, usuario, loja):
        loja.adicionar_usuario(usuario)
        