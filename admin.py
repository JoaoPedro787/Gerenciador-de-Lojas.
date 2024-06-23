from loja import Loja
from utils import add_item_lista,remove_item_lista

class Admin:
    lojas = []
    usuarios = []

    @classmethod
    def cadastrar_loja(cls, nome_loja):
        if nome_loja not in [loja.nome for loja in cls.lojas]:
            nova_loja = Loja(nome_loja)
            add_item_lista(cls.lojas, nova_loja)
            return nova_loja
        else:
            print('Loja já cadastrada')
            return None

    @classmethod
    def remover_loja(cls, nome_loja):
        for loja in cls.lojas:
            if loja.nome == nome_loja:
                remove_item_lista(cls.lojas, loja)
                return True
        print('Loja não encontrada')
        return False

    @classmethod
    def remover_usuario(cls, nome_usuario):
        for usuario in cls.usuarios:
            if usuario.nome == nome_usuario:
                remove_item_lista(cls.usuarios, usuario)
                return True
        print('Usuário não encontrado')
        return False

        