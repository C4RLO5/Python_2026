class bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):# Construtor
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print('piiiiii')

    def parar(self):
        print('Parando a bicicleta ...')
        print('bicicleta parada ... ')

    def correr(self):
        print('Vruummmm ...')

    #def __str__(self):
        # return f'''
        #  === Bicicleta ===

        #  - Cor: {self.cor}    
        #  - Modelo: {self.modelo}
        #  - Ano: {self.ano}
        #  - valor: R$ {self.valor} '''

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}'

    '''def status(self):
        print(f'''

    '''
    - Cor: {self.cor}    
    - Modelo: {self.modelo}
    - Ano: {self.ano}
    - valor: R$ {self.valor}

    '''
''') '''

    

calor1 = bicicleta('vermelha', 'BMX', 2014, 2000)
print(calor1)
#print(calor1)
#print(calor1.cor, calor1.modelo, calor1.ano, calor1.valor)
#calor1.status()
calor1.buzinar()
calor1.correr()
calor1.parar()

calor2 = bicicleta('preto', 'Monark', 2003, 1500)
print(calor2)
