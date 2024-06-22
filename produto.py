class Categoria:
    def __init__(self,nome,descricao):
        self.nome=nome
        self.descricao=descricao

class Produto:
    def __init__(self,nome,categoria):
        self.nome=nome
        self.categoria=categoria
        self.quantidade=0