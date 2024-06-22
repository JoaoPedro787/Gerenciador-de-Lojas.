from utils import add_item_lista, remove_item_lista, transacao_quantidade

class Loja:
    
    def __init__(self, nome):
        self.id = None
        self.nome = nome
        self.produtos = []
        self.users = []
    
    def adicionar_usuario(self, usuario):
        # Adiciona o usuário à lista de usuários da loja
        add_item_lista(self.users, usuario)
        # Adiciona esta loja à lista de lojas do usuário
        usuario._adicionar_loja(self)

    def remover_usuario(self, usuario):
        # Remove o usuário da lista de usuários da loja
        remove_item_lista(self.users, usuario)
        # Remove esta loja da lista de lojas do usuário
        usuario._remover_loja(self)
        
    def adicionar_produto_loja(self, produto):
        add_item_lista(self.produtos, produto)
    
    def remover_produto_loja(self, produto):
        remove_item_lista(self.produtos, produto)
    
    def compra_produto(self, produto, qtd):
        # Aumenta a quantidade de um produto na loja
        transacao_quantidade(self.produtos, produto, qtd, op='+')
        
    def venda_produto(self, produto, qtd):
        # Diminui a quantidade de um produto na loja
        transacao_quantidade(self.produtos, produto, qtd, op='-')