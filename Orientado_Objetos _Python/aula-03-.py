class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Ligando motor...')
    def __str__(self):
        #return self.cor
        return f'{self.__class__.__name__}: {'\n'.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}'

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
      super().__init__(cor, placa, numero_rodas)
      self.carregado = carregado

    def esta_carregado(self):
        print(f'{'sim' if self.carregado else 'não'} estou carregado.')

moto = Motocicleta('Vermelha', 'ABC-1234', 2)
moto.ligar_motor()

carro = Carro('preto', 'bmw', 4)
carro.ligar_motor()

caminhao = Caminhao('roxo', 'gfd-8712', 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)
