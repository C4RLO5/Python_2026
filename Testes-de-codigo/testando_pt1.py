'''Nível 1 – Básico
Cadastro de pessoa
    Crie um dicionário com nome, idade e profissão.
    Faça uma função que mostre todas as informações.
Atualizar idade
    Faça uma função que receba o dicionário e uma nova idade.
    Atualize apenas esse valor.
Maior de idade
   Faça uma função que receba um dicionário e retorne True ou False dependendo da idade.'''

cadastrando_usuario = {
    'nome': 'Carlos' ,
    'idade': 22,
    'profissão': 'Barista'
}

def informações_do_usuario():
    print(f'''
    =======================================
        INFORMAÇÕES PESSOAIS DO USUÁRIO
    =======================================
          
          Nome --> {cadastrando_usuario['nome']}
          Idade --> {cadastrando_usuario['idade']}
          Profissão --> {cadastrando_usuario['profissão']}

    =======================================
''')

informações_do_usuario()