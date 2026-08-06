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
                [4] Chás ----------------- Descartado da versão inicial
                [5] Refreschers ----------------- Descartado da versão inicial
                [6] Grãos ----------------- Descartado da versão inicial

Nessa versão o usúario poderá escolher adicionar um novo produto, logo aṕos aparecerá um cardapio com poucas opções, no momento
estará disponivel frappucino, bebidas frias e quentes. Entretando com o decorrer de futuras atualizações haverá mais produtos.

Atualizações futuras(Em planejamento):

def menu(self):
        escolha = int(input('''
'''  [ HOME ]

            + DESCUBRA UBE + COCO. Textura cremosa, sensação tropical.
                - Frappuccino ube coco
                - Ube latte


            + CLIQUE E RETIQUE, na sua Starbucks favorita.

            
            [1] Adicionar produto
            [2] Ver o carrinho
            [3] Remover produto

---> #))

O menu acima sofrerá mudanças em linhas de código, por ser tratar de menu, irá ser aplicada a função while para rodar lo até que o uśuario escolha sair/encerrar a compra,
possivelmente tambem será capaz de observar items/bebidas que foram selecionados no carrinho, porém por enquanto está descartadado.

'''

class Starbucks:
    def __init__(self, nome, preço, tamanho = 'venti'):
        self.nome = nome
        self.preço = preço
        self.tamanho = tamanho

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



            [4] (desenvolvimento)

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
            case _: print('Opção inválida...')
             
    def menu_adicionar_produto(self):
         escolha = int(input('''
                
                    [Cardapio]
                
                [1] Bebidas Frias
                [2] Bebidas quentes
                [3] Frappuccinos
            

---> '''))
         match escolha:
                         case 1:
                             self.bebidas_frias()
                         case 2:
                             self.bebida_quente()
                         case 3:
                             print('teste')
                         case _: print('Opção invalida...')
              
    def bebidas_frias(self):
        escolha = int(input('''
                
                [1] Caramelo Macchiato (Venti) R$ 23.90
                [2] Iced Shaken Expresso (venti) R$ 24.90
                [3] Vanilha Latte Gelado (Venti) R$ 24.90
            
---> '''))
        match escolha:
            case 1:
                gelo_adicional = input('Nivel de gelo na bebida (Pouco / médio / Alto / Sem) --> ')
                app_itemBebida = bebida_fria('Caramelo Macchiato', 23.90, 'Venti', gelo_bebida = gelo_adicional,)
                print(f'Obrigado por comprar conosco, volte sempre!!\n')
                print(app_itemBebida)
            case 2:
                gelo_adicional = input('Nivel de gelo na bebida (Pouco / médio / Alto / Sem) --> ')
                app_itemBebida = bebida_fria('Iced Shaken Expresso', 24.90, 'Venti', gelo_bebida = gelo_adicional,)
                print(f'Obrigado por comprar conosco, volte sempre!!\n')
                print(app_itemBebida)
            case 3:
                gelo_adicional = input('Nivel de gelo na bebida (Pouco / médio / Alto / Sem) --> ')
                app_itemBebida = bebida_fria('Vanilha Latte Gelado', 24.90, 'Venti', gelo_bebida = gelo_adicional,)
                print(f'Obrigado por comprar conosco, volte sempre!!\n')
                print(app_itemBebida)


    def bebida_quente(self):
         escolha = int(input('''

        [] Café Mocha
        [] Doce de leite Latte
        [] Cafe Latte

---> '''))
         match escolha:
              case 1: print('teste')
              case 2: print('teste')
              case 3: print('teste')
              case _: print('escolha inválida.')
                    
              
             
class bebida_quente(Starbucks):
     def __init__(self, nome, preço,tamanho = 'venti', temperatura = 'Extra Hot'):
        super().__init__(nome,preço,tamanho)
        self.temperatura = temperatura

class bebida_fria(Starbucks):
     def __init__(self, nome, preço, tamanho = 'venti', gelo_bebida = 'padrão'):
          super().__init__(nome, preço, tamanho)
          self.gelo_bebida = gelo_bebida


               

app_teste= Starbucks("",0.0,'')
app_teste.menu()    

