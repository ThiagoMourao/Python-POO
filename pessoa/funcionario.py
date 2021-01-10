from pessoa.pessoa import Pessoa

class Funcionario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)
        print()

    def __del__(self):
        print(f'{self.nome} foi apagado')

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} foi apagado')

class Gerente(Pessoa):
    def gerenciar(self):
        print('O gerente esta administrando no momento...')

class Diretor(Gerente):
    def __init__(self, nome, idade,cpf):
        Pessoa.__init__(self, nome, idade)
        self.cpf = cpf
    
    def gerenciar(self):
        Pessoa.get_ano_nascimento(self)
        super().gerenciar()
        print('O diretor esta administrando, aguarde...')
    