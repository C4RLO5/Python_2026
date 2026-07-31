#herança multipla

class animal:
    def __init__(self, n_patas):
        self.n_patas = n_patas
    def __str__(self):
        return f'{self.__class__.__name__}: {'\n'.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}'

class mamifero(animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        #self.n_patas = n_patas
        super().__init__(**kw)

class ave(animal):
    def __init__(self, cor_bico, **kw):
        #self.n_patas = n_patas
        self.cor_bico = cor_bico
        super().__init__(**kw)

    def __str__(self):
        return 'ave 42'

#class cachorro(mamifero):
    pass

class gato(mamifero):
    pass

#class leao(mamifero):
    pass

class Ornitorrinco(mamifero, ave):
    def __init__(self, cor_bico, cor_pelo, n_patas,):

            print(Ornitorrinco.mro())

            print(Ornitorrinco.__mro__)

            super().__init__(cor_bico=cor_bico, cor_pelo=cor_pelo, n_patas=n_patas)

gato = gato(n_patas = 4, cor_pelo= 'cinza')
print(gato,'\n')

Ornitorrinco = Ornitorrinco(n_patas = 4, cor_pelo= 'amarelo', cor_bico = 'laranja')
print(Ornitorrinco)