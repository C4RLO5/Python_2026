'''█

O objetivo desse projeto com a temática de Pokemon seria simular uma pokedex com Python, 
utilizando estruturas condicionais com dicionarios e funções.

Abaixado podemos notar o que está em desenvolvimento e o que está sendo removido ou foi dessa atualização de codigo.

Pokedex v1.2

[1] Ver Pokedex                    █ Funcionando normal
[2] Buscar Pokemon                 █ Descartado da versão inicial
[3] Comparar Pokemon               █ Funcionando normal
[4] Adicionar Pokemon              █ Funcionando normal
[5] Editar Pokemon                 █ Descartado da versão inicial
[6] Remover Pokemon                █ Funcionando normal
[7] Estatisticas                   █ Descartado da versão inicial
[8] Sair


Pokedex v1.3

Nessa atualização será implementado um menu de comparação entre dois pokemons
escolhidos pelo úsuario, nele irá mostrar todos as habilidades, peso e suas
características. Também será melhor elaborado uma correção, e deixar o código
de maneira geral mais limpo, evitando ao maximo repertição de palavras, e mais
elaboração de funções, onde irá separar o que cada elemento será responsavel.

O possivél menu para a função de comparação entre pokemons:

def comparar_pokemon():

    print(
====================== 
=== [1] Bulbasaur  ===
=== [2] Charmander ===
=== [3] Squirtle   ===
=== [4] Pikachu    ===
=== [5] Caterpie   ===
=== [6] Butterfree ===
=== [7] Pidge      ===
======================

)

Pokedex v1.4

Nessa nova atualização o usuario poderá acessar duas ferramentas que serão inclusas,
o adicionar um novo Pokemon e excluir o próprio. Será solicitado (nome, pesoa, tipo, habilidades) ou seja,
tudo que foi atribuido nos pokemons existentes do dicionario.

- Possivel menu com essas aplicações e correção, priorizando um código limpo.

=========[ POKEDEX ]===============█
[1] Ver Pokedex                    █                 
[2] Comparar Pokemon               █
[3] Adicionar Pokemon              █
[4] Remover Pokemon                █                  
[5] Sair                           █
====================================

Pokedex v1.5 

Nessa ultima atualização será focada apenas na limpeza e resumo geral do código, não será nada de inovador,
apenas serão observados se há pequenos trechos repertidos. Será aplicado tratamento de erros, por enquanto
não haverá alteração de menu, irá ser fixo o design apresentado na v1.4. E com isso gostaria de agradecer pelo meu esforço por ter 
desenvolvido esse código, lembrando que apenas uma pessoa foi responsável por esse projeto que será compartilhado na conta profissional
do GitHub. 


'''


pokemon = {
    'Bulbasaur' : {
        'Altura': '0.7m',
        'Peso':'6.9kg',
        'Categoria':'Speed',
        'Habilidade':'Overgrow',
        'Sexo':'Masculino/Feminino',
        'Tipo':'Planta/Poison',
        'Fraquezas': '\n1.Fogo\n2.Flying\n3.Ice\n4.Psiquico\n',
        'Estatísticas': {
            'PS': '███\n\n',
            'Ataque': '███\n\n',
            'Defesa': '███\n\n',
            'Ataque Especial': '███\n\n',
            'Defesa Especial': '███\n\n',
            'Velocidade': '████\n' 
    }},
    'Charmander': {
        'Altura': '0.6m',
        'Peso':'8.5kg',
        'Categoria':'Lizard',
        'Habilidade':'Blaze',
        'Sexo':'Masculino/feminino',
        'Tipo':'Fogo',
        'Fraquezas': '\n1.Agua\n2.Rock\n3.Ground\n',
        'Estatísticas':{ 
            'PS':'███\n\n',
            'Ataque': '████\n\n',
            'Defesa': '███\n\n',
            'Ataque Especial': '████\n\n',
            'Defesa Especial': '███\n\n',
            'Velocidade': '████\n'         
        }
    },
    'Squirtle':{
        'Altura': '0.5m',
        'Peso':'9.0kg',
        'Categoria':'Tiny Turtle',
        'Habilidade':'Torrent',
        'Sexo':'Masculino/Feminino',
        'Tipo':'Agua',
        'Fraquezas': '\n1.Planta\n2.Eletric\n',
        'Estatísticas': {
            'PS': '███\n\n',
            'Ataque':'███\n\n',
            'Defesa': '████\n\n',
            'Ataque Especial': '███\n\n',
            'Defesa Especial': '████\n\n',
            'Velocidade': '███\n',
        }
    },
    'Pikachu':{
        'Altura': '.4m',
        'Peso':'6kg',
        'Categoria':'Mouse',
        'Habilidade':'Static',
        'Sexo':'Masculino/Feminino',
        'Tipo':'Eletric',
        'Fraquezas': '\n1.Ground\n',
        'Estatísticas': {
            'PS': '███\n\n',
            'Ataque':'████\n\n',
            'Defesa': '███\n\n',
            'Ataque Especial': '███\n\n',
            'Defesa Especial': '███\n\n',
            'Velocidade': '████\n',
        }
    },
    'Caterpie': {
        'Altura': '0.3m',
        'Peso':'2.9kg',
        'Categoria':'Worm',
        'Habilidade':'Shield Dust',
        'Sexo':'Masculino/Feminino',
        'Tipo':'Bug',
        'Fraquezas': '\n1.Fogo\n2.Flying\n3.Rock\n',
        'Estatísticas':{
            'PS': '███\n\n',
            'Ataque': '██\n\n',
            'Defesa': '███\n\n',
            'Ataque Especial': '██\n\n',
            'Defesa Especial': '██\n\n',
            'Velocidade': '███\n'
    }},
    'Butterfree': {
        'Altura': '1.1m',
        'Peso':'32kg',
        'Categoria':'Butterfree',
        'Habilidade':'Compound Eyes',
        'Sexo':'Masculino/Feminino',
        'Tipo':'Bug/Flying',
        'Fraquezas': '\n1.Fogo\n2.Eletric\n3.Flying\n4.Rock\n5.Ice\n',
        'Estatísticas': {
            'PS': '████\n\n',
            'Ataque': '███\n\n',
            'Defesa': '███\n\n',
            'Ataque Especial': '██████\n\n',
            'Defesa Especial': '█████\n\n',
            'Velocidade': '█████\n'
    }},
    'Pidgey': {
        'Altura': '0.3m',
        'Peso':'1.38kg',
        'Categoria':'Tiny Bird',
        'Habilidade':'Keen Eye/Tangled Feet',
        'Sexo':'Masculino/Feminino',
        'Tipo':'Normal/Flying',
        'Fraquezas': '\n1.Eletric\n2.Rock\n3.Ice\n',
        'Estatísticas': {
            'PS': '███\n\n',
            'Ataque': '███\n\n',
            'Defesa': '███\n\n',
            'Ataque Especial': '███\n\n',
            'Defesa Especial': '███\n\n',
            'Velocidade': '████\n'        
    }}
}

numeração_pokemon = ['Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu', 'Caterpie', 'Butterfree', 'Pidgey']

def menu_pokedex():
    while True:
        escolha = int(input('''
=========[ POKEDEX ]===============█
[1] Ver Pokedex                    █                 
[2] Comparar Pokemon               █
[3] Adicionar Pokemon              █
[4] Remover Pokemon                █                  
[5] Sair                           █
====================================
O que deseja? ---> '''))
        if escolha == 1:
            ver_pokedex()
        elif escolha == 2:
            comparar_pokemon()
        elif escolha == 3:
            adicionar_pokemon()
        elif escolha == 4:
            remover_pokemon()
        elif escolha == 5:
            print('Obrigado por testar esse projeto!!! ')
            break


def ver_pokedex():
    '''escolha_pokemon = int(input'''
    print('''
=============== POKEMON LIST ===============
[1] Bulbasaur
[2] Charmander
[3] Squirtle
[4] Pikachu
[5] Caterpie
[6] Butterfree
[7] Pidgey

                                + Sobre qual pokemon deseja saber? --->  ''')
    for indice, nome in enumerate(numeração_pokemon, start = 1):
        print(f'[{indice}] {nome}')
    escolha_pokemon = int(input('\nEscolha um pokemon: '))

    escolha_pokemon = numeração_pokemon[escolha_pokemon - 1]

    print(f'\nO pokemon escolhido foi {escolha_pokemon}\n')

    for chave, valor, in pokemon[escolha_pokemon].items():
        print(f' - {chave}: {valor}')

    #return numeração_pokemon[escolha_pokemon - 1]

'''

Pokedex v1.2, antiga funcionadade no codigo como era utilizado.

    - Repertição desnecessária de estrutura condicional

    if escolha_pokemon == 1:
        escolha_pokemon = 'Bulbasaur'
    elif escolha_pokemon == 2:
        escolha_pokemon = 'Charmander'
    elif escolha_pokemon == 3:
        escolha_pokemon = 'Squirtle'
    elif escolha_pokemon == 4:
        escolha_pokemon = 'Pikachu'
    elif escolha_pokemon == 5:
        escolha_pokemon = 'Caterpie'
    elif escolha_pokemon == 6:
        escolha_pokemon = 'Butterfree'
    elif escolha_pokemon == 7:
        escolha_pokemon = 'Pidgey'
    else:
        print('Pokemon não identificado...')
        return
    
    print(f'''
#\n\n============= Você escolheu {escolha_pokemon} abaixo está suas informações: =========
''')




    for chave, valor in pokemon[escolha_pokemon].items():
        if chave == 'Estatísticas':
            print(f'\n{chave}:')
            for atributo, barra in valor.items():
                print(f'{atributo}:{barra}')
        else:
            print(f'- {chave}: {valor}')'''
    


def comparar_pokemon():

    print('''
====================== 
=== [1] Bulbasaur  ===
=== [2] Charmander ===
=== [3] Squirtle   ===
=== [4] Pikachu    ===
=== [5] Caterpie   ===
=== [6] Butterfree ===
=== [7] Pidgey     ===
======================

''')
    primeiro_pokemon = int(input('Primeira pokemon escolhido >>>> '))
    segundo_pokemon = int(input('Segundo pokemon escolhido >>>>  '))

    primeiro_pokemon = numeração_pokemon[primeiro_pokemon - 1]
    segundo_pokemon = numeração_pokemon[segundo_pokemon - 1]

    for chave, valor in pokemon[primeiro_pokemon].items():
        print(f'''
        ========= Informações do Primeiro Pokemon =========
        
        {chave}: {valor}''')
    for chave, valor in pokemon[segundo_pokemon].items():
        print(f'''
        ========= Informações do segundo Pokemon =========
        
        {chave}: {valor}''')

def adicionar_pokemon():
    pokemon_adicionado = input('Digite um nome para seu pokemon >>> ')
    altura = int(input('Altura >>> '))
    peso = int(input('Peso >>> '))
    categoria = input('Categoria ao qual seu pokemon se classifica >>> ')
    habilidade = input('Qual a habilidade desse pokemon? >>> ')
    sexo = input('Masculino ou Feminino? >>> ')
    tipo = input('Tipo desse pokemon? >>> ')
    fraqueza = input('A principal fraqueza desse pokemon? >>> ')

    ''''Altura': '0.7m',
        'Peso':'6.9kg',
        'Categoria':'Speed',
        'Habilidade':'Overgrow',
        'Sexo':'Masculino/Feminino',
        'Tipo':'Planta/Poison',
        'Fraquezas': '\n1.Fogo\n2.Flying\n3.Ice\n4.Psiquico\n',
        'Estatísticas'''
    pokemon[pokemon_adicionado] = {
        'Altura': altura,
        'Peso': peso,
        'Categoria': categoria,
        'Habilidade': habilidade,
        'Sexo': sexo,
        'Tipo':tipo,
        'Fraquezas': fraqueza
    }

    numeração_pokemon.append(pokemon_adicionado)

    print(f'\nPokemon {pokemon_adicionado} adicionado com sucesso!!! ')
    for chave, valor in pokemon[pokemon_adicionado].items():
        print(f'- {chave}: {valor}')

def remover_pokemon():

    for indice, nome in enumerate(numeração_pokemon, start=1):
        print(f'[({indice}] {nome}')
    escolha_pokemon = int(input('\nGostaria de apagar qual pokemon? '))

    pokemon_removido = numeração_pokemon[escolha_pokemon - 1]
    numeração_pokemon.remove(pokemon_removido)

    del pokemon[pokemon_removido]

    print(f'\nPokemon {pokemon_removido} deletado com sucesso!!! ')

menu_pokedex()