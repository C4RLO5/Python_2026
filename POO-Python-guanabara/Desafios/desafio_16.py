class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar_funcionario(self):
        return f'Olá , sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa Curso em Video.'


funcionario_1 = Funcionario('Carlos', 'Analise de dados', 'Desenvolvedor')
print(funcionario_1.apresentar_funcionario())