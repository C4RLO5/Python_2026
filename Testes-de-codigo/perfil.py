'''
===========================================================================================================================
===                     Projeto em cadastro Usuario, com a aplicação de uma ONG                                         ===
===                                                                                                                     ===
===  1.Criar perfil.                                                                                                    ===
===  2. Menu interativo                                                                                                 ===
===  3. Fornecimento de agendas e horarios                                                                              ===
===                                                                                                                     ===
===                                                                                                                     ===
===                                                                                                                     ===
===                                                                                                                     ===
===                                                                                                                     ===
===                                                                                                                     ===
===========================================================================================================================
'''




class Perfil:
    #Metodo construtor, todas as caracteristicas do cadastro perfil.
    def __init__(self, nome, senha, endereco, cpf, rg, profissao, funcao, qual_situacao, nome_paciente):
        self.nome = nome
        self.senha = senha
        self.endereco = endereco
        self.cpf = cpf
        self.rg = rg
        self.profissao = profissao
        self.funcao = funcao
        self.qual_situacao = qual_situacao
        self.nome_paciente = nome_paciente

    def __str__(self):
        return f'{self.__class__.__name__}: {'\n'.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}'
    
    def cadastrar_usuario():

        nome = input('Digite um nome para o novo usuario --> ')
        senha = input('Digite uma senha, podendo conter numeros com caracters(5/$/Aa) --> ')
        endereco = input('Onde mora? ---> ')
        cpf = int(input('CPF --> '))
        rg = int(input('RG -->'))
        profissao = input('Qual sua profissão? ---> ')
        funcao = input('Qual função realiza em seu trabalho? --> ')
        qual_situacao = input('Qual a situação que o usúario se encontra? ---> ')
        nome_paciente = input('Nome completo ---> ')

        novo_usuario = Perfil(nome, senha, endereco, cpf, rg, profissao, funcao, qual_situacao, nome_paciente)
        return novo_usuario

    if __name__ == '__main__':
        usuario_1 = cadastrar_usuario()
        print('============ Perfil Usuario criado com sucesso!!!! ============ ')
        print(f'{usuario_1}')
        

