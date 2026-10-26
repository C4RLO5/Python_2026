from rich import print
from rich.panel import Panel


class Churrasco:
    def __init__(self, quantidade_pessoas):
        self.quantidade_pessoas = quantidade_pessoas

    def calculo_geral(self):
        quantidade_carne = self.quantidade_pessoas * 0.4
        custo_churrasco = quantidade_carne * 82.40
        preço_pessoas = custo_churrasco / self.quantidade_pessoas

        mensagem = (f'''
        :grinning_squinting_face: Analisando Churras dos Amigos com {self.quantidade_pessoas} convidados. 
        
        Cada participante comerá 0.4kg e cada Kg custa R$82.40

        Recomendo comprar {quantidade_carne:.3f}Kg de Carne

        O custo total será de R${custo_churrasco:.2f}

        Cada pessoa pagará R${preço_pessoas:.2f} para participar

''')
        return Panel(mensagem, title='Churras dos Amigos', width=35)

teste = Churrasco(15)
print(teste.calculo_geral())
        


