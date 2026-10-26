from rich import print
from rich.panel import Panel


class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def etiqueta(self):
        etiqueta_produto = Panel(f'{self.nome}\n-----------------------------\nR$ {self.preço:.2f}', title='Produto', width=35)
        return etiqueta_produto


teste_1 = Produto('MotoG2', 1200)
print(teste_1.etiqueta())