class Cachorro:
    def __init__(self, nome, cor, acordado = True):#Construtor
        print('Iniciaindo a classe...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):#Destrutor
        print('Removendo a instância da classe... ')

    def falar(self):
        print('Auau...')

def criar_cachorro():
    c = Cachorro('Zeus', 'Branco e preto', False)
    print(c.nome)

c = Cachorro('Charpie', 'Amarelo')
c.falar()
criar_cachorro()

print('1')
del c
print('2')
print('3')
print('4')