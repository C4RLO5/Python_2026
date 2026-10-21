class Starbucks:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço

    def informações(self):
        return f'''
        ====== Informações ======

        Café {self.nome}
        Preço R$ {self.preço}

''' 
    
