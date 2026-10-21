class Starbucks:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def informações(self):
        return f'''
        ====== Informações ======

        Café {self.nome}
        Preco R$ {self.preco}

''' 
