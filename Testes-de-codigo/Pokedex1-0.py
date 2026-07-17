pokemon = {
    'Bulbasaur' : {
        'Altura': '0.7m',
        'Peso':'6.9kg',
        'Categoria':'Speed',
        'Habilidade':'Overgrow',
        'Sexo':'Masculino/Feminino',
        'Tipo':'Planta/Poison',
        'Fraquezas': '\n1.Fogo\n2.Flying\n3.Ice\n4.Psiquico\n',
        'Estatísticas': '\nPS [][][]\nAtaque [][][]\nDefesa [][][]\nAtaque Especial [][][]\nDefesa Especial [][][]\nVelocidade [][][][]\n' 
    },
    'Charmander': {
        'Altura': '0.6m',
        'Peso':'8.5kg',
        'Categoria':'Lizard',
        'Habilidade':'Blaze',
        'Sexo':'Masculino/feminino',
        'Tipo':'Fogo',
        'Fraquezas': '\n1.Agua\n2.Rock\n3.Ground\n',
        'Estatísticas': '\nPS [][][]\nAtaque [][][][]\nDefesa [][][]\nAtaque Especial [][][][]\nDefesa Especial [][][]\nVelocidade [][][][]\n'         
    },
    'Squirtle':{
        'Altura': '0.5m',
        'Peso':'9.0kg',
        'Categoria':'Tiny Turtle',
        'Habilidade':'Torrent',
        'Sexo':'Masculino/Feminino',
        'Tipo':'Agua',
        'Fraquezas': '\n1.Planta\n2.Eletric\n',
        'Estatísticas': '\nPS [][][]\nAtaque [][][]\nDefesa [][][][]\nAtaque Especial [][][]\nDefesa Especial [][][][]\nVelocidade [][][]\n'
    },
    'Pikachu':{
        'Altura': '.4m',
        'Peso':'6kg',
        'Categoria':'Mouse',
        'Habilidade':'Static',
        'Sexo':'Masculino/Feminino',
        'Tipo':'Eletric',
        'Fraquezas': '\n1.Ground\n',
        'Estatísticas': '\nPS [][][]\nAtaque [][][][]\nDefesa [][][]\nAtaque Especial [][][]\nDefesa Especial [][][]\nVelocidade [][][][]\n'
    },
    'Caterpie': {
        'Altura': '0.3m',
        'Peso':'2.9kg',
        'Categoria':'Worm',
        'Habilidade':'Shield Dust',
        'Sexo':'Masculino/Feminino',
        'Tipo':'Bug',
        'Fraquezas': '\n1.Fogo\n2.Flying\n3.Rock\n',
        'Estatísticas': '\nPS [][][]\nAtaque [][]\nDefesa [][][]\nAtaque Especial [][]\nDefesa Especial [][]\nVelocidade [][][]\n'
    },
    'Butterfree': {
        'Altura': '1.1m',
        'Peso':'32kg',
        'Categoria':'Butterfree',
        'Habilidade':'Compound Eyes',
        'Sexo':'Masculino/Feminino',
        'Tipo':'Bug/Flying',
        'Fraquezas': '\n1.Fogo\n2.Eletric\n3.Flying\n4.Rock\n5.Ice\n',
        'Estatísticas': '\nPS [][][][]\nAtaque [][][]\nDefesa [][][]\nAtaque Especial [][][][][][]\nDefesa Especial [][][][][]\nVelocidade [][][][][]\n'
    },
    'Pidgey': {
        'Altura': '0.3m',
        'Peso':'1.38kg',
        'Categoria':'Tiny Bird',
        'Habilidade':'Keen Eye/Tangled Feet',
        'Sexo':'Masculino/Feminino',
        'Tipo':'Normal/Flying',
        'Fraquezas': '\n1.Eletric\n2.Rock\n3.Ice\n',
        'Estatísticas': '\nPS [][][]\nAtaque [][][]\nDefesa [][][]\nAtaque Especial [][][]\nDefesa Especial [][][]\nVelocidade [][][][]\n'        
    }
}


def menu_pokemom():
    escolha_pokemon = int(input('''
=============== POKEMON LIST ===============
[1] Bulbasaur
[2] Charmander
[3] Squirtle
[4] Pikachu
[5] Caterpie
[6] Butterfree
[7] Pidgey

                                + Sobre qual pokemon deseja saber? --->  '''))

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
\n\n============= Você escolheu {escolha_pokemon} abaixo está suas informações: =========
''')

    for chave, valor in pokemon[escolha_pokemon].items():
        print(f'- {chave}: {valor}')


menu_pokemom()