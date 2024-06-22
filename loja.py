from utils import add_item_lista,remove_item_lista,transacao_quantidade

class Loja:
    
    def __init__(self,nome):
        self.id=None
        self.nome=nome
        self.produtos=list()
        self.users=list()
    
    def adicionar_usuario(self, usuario):
        add_item_lista(self.users,usuario)
        usuario._adicionar_loja(self)

    def remover_usuario(self, usuario):
        remove_item_lista(self.users,usuario)
        usuario._remover_loja(self)
        
    def adicionar_produto_loja(self,produto):
        add_item_lista(self.produtos,produto)
    
    def remover_produto_loja(self,produto):
        remove_item_lista(self.users,produto)
    
    def compra_produto(self,produto,qtd):
        transacao_quantidade(self.produtos,produto,qtd,op='+')
        
    def venda_produto(self,produto,qtd):
        transacao_quantidade(self.produtos,produto,qtd,op='-')