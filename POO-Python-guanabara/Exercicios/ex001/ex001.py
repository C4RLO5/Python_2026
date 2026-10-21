#Declaração da classe
class Gafanhoto:

    #Atributos
    def __init__(self):
        self.nome = ''
        self.idade = 0

    #Metodos
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade.'

# Declaração de Objetos

#objeto 1
g1 = Gafanhoto()
g1.nome = 'Carlos'
g1.idade = 23
g1.aniversario()
print(g1.mensagem())

#objeto 2
g2 = Gafanhoto()
g2.nome = 'Eduardo'
g2.idade = 21
print(g2.mensagem())