from utils import add_item_lista, remove_item_lista

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
    
    def add_produto_loja(self, loja,produto):
        if loja in self.lojas:
            # Chama o método de adicionar produto na loja
            loja.adicionar_produto_loja(produto)
    
    def remover_produto_loja(self, loja,produto):
        if loja in self.lojas:
            # Chama o método de remover produto na loja
            loja.remover_produto_loja(produto)
        
    
    def compra_estoque_qtd_produto(self, produto, loja, qtd):
        if loja in self.lojas:
            # Chama o método de compra de produto na loja
            loja.compra_produto(produto, qtd)
        
    def venda_estoque_qtd_produto(self, produto, loja, qtd):
        if loja in self.lojas:
            # Chama o método de venda de produto na loja
            loja.venda_produto(produto, qtd)