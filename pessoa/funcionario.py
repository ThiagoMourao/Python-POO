from pessoa.pessoa import Pessoa


class Funcionario:
    def __init__(self, nome, idade, carteira_trabalho):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
        self.carteira_trabalho = carteira_trabalho

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)
        print()

    def __del__(self):
        print('\n')
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

class Gerente2(Pessoa, Funcionario): #A ordem dos parametros é exatamente a ordem de busca em profundidade dos metodos e variaveis
    def __init__(self, nome, idade,cpf):
        Pessoa.__init__(self, nome, idade)        
        self.cpf = cpf

    def gerenciar_estoque(self):        
        print(f'O gerente 2: nome:{self.nome}')
        print(f'O gerente 2: idade:{self.idade}')
        print(f'O gerente 2: cpf:{self.cpf}')    
    