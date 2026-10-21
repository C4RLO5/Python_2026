#Declaração da classe
class Gafanhoto:
    '''
        Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade.
    
        Para criar uma nova pessoa, use
        Variavel = Gafanhoto(nome, idade)
    '''
    #Atributos
    def __init__(self, nome = 'default', idade = 0 ):
        self.nome = nome
        self.idade = idade

    #Metodos
    def aniversario(self):
        self.idade = self.idade + 1

    '''def mensagem(self):
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade.'
    '''
    def __str__(self):
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade.'

    def __getstate__(self):
        return f'Estado: Nome = {self.nome} ; Idade = {self.idade}'
# Declaração de Objetos

#objeto 1
g1 = Gafanhoto('Carlos', 23)
g1.aniversario()
#print(g1.mensagem())
#print(g1)
print(g1.__getstate__()) #Personalizavel
print(g1.__dict__)

#objeto 2
g2 = Gafanhoto('Eduardo', 21)
#print(g2.mensagem())
#print(g1)
print(g2.__dict__)
print(g2.__getstate__())


#objeto 3
g3 = Gafanhoto()
#print(g3.mensagem())
#print(g1)
print(g3.__dict__) #imprimir o objeto de forma de um dicionario.
print(g3.__getstate__())
print(g3.__class__) #Classe do objeto criado
