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

versão 1.2

protótipo menu adicionar produto(em desenvovlimento):

[Cardapio]
                
                [1] Bebidas Frias
                [2] Bebidas quentes
                [3] Frappuccinos
                [4] Chás
                [5] Refreschers
                [6] Grãos


'''
class Starbucks:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    def __str__(self):
            informativo = '\n'.join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])
            return f"{self.__class__.__name__}:{informativo}"
    #return f'{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}' 


    def menu(self):
        escolha = int(input('''
                        [ HOME ]

            + DESCUBRA UBE + COCO. Textura cremosa, sensação tropical.
                - Frappuccino ube coco
                - Ube latte


            + CLIQUE E RETIQUE, na sua Starbucks favorita.

            
            [1] Adicionar produto
            [2] Ver o carrinho
            [3] Remover produto

---> '''))
        match escolha:
            case 1:
                self.menu_adicionar_produto()
                '''
                teste1 = Starbucks('','','')
                print(teste1)
                '''   
            case 2: print('teste 2')
            case 3: print('teste 3')
    def menu_adicionar_produto(self):
         escolha = int(input('''
                
                    [Cardapio]
                
                [1] Bebidas Frias
                [2] Bebidas quentes
                [3] Frappuccinos
                [4] Chás
                [5] Refreschers
                [6] Grãos

---> '''))
         print(escolha)
             
class bebida_quente(Starbucks):
     def __init__(self, nome, preço):
        super().__init__(nome,preço)

class bebida_fria(Starbucks):
     def __init__(self, nome, preço):
          super().__init__(nome, preço)

app_teste= Starbucks("","")
app_teste.menu()    

