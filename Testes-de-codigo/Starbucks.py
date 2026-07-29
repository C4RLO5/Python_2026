'''
================== Starbucks ========================

O que esperar desse projeto?

1. Criação de uma Classe.
2. Código Limpo.
3. metodos/funções de ações no desenvolvimento do código.
4. Herança
5. Encapsulamento
6. Polimofismo
7. Classes Abstratas

Menu

Haverá um menu no decorrer do desenvolvimento do projeto, onde o total foco seria
simular um carrinho de compra em um sistema digital da franquia Starbucks.
O que é possível ter:

1. Adicionar produto
2. Remover produto
3. Concluir Compra
4. Catalogo(Cafés e bebidas)

Versão 1.0

Iniciando uma classe com nome, preço e torra. O objetivo nessa etapa
é apenas demonstrar um metodo que entrega as informações de acordo como é 
criado o objeto.

Versão 1.1

Protótipo do menu cartalogo

1. Bebidas | --->    1. Geladas 2. Quentes | (Em caso de escolher gelada) ---> 1. Frapuccino 2. Icead de bebidas quentes
2. Café em grão | ---> 1. Brasil Blend 2. Veranda 3. Colombia
3. Retail | ---> 1. Copo  2. Garrafa 


'''
class Produto:
    def __init__(self, nome, preço, torra):
        self.nome = nome
        self.preço = preço
        self.torra = torra
    
    def __str__(self):
        return f'''nome -> {self.nome}\npreço -> R$ {self.preço}\ntorra --> {self.torra} '''

produto_1 = Produto('Brasil Blend', 54.90, 'Média')
print(produto_1)