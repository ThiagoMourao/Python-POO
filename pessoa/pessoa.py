from datetime import datetime
from random import randint


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando        

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        print(f'{self.nome} esta comendo {alimento}')
        self.comendo = True

    def stop_comer(self, alimento):
        if not self.comendo:
            print(f'{self.nome} não está comendo mais')
            return
        elif self.falando:
            print(f'{self.nome} esta falando, acabe de falar primeiro.')
            return

        self.comendo = False
        print(f'{self.nome} acabou de comer a {alimento}')    

    def falar(self, assunto):
        if self.falando:
            print(f'{self.nome} ja esta falando sobre {assunto}.')
            return
        elif self.comendo:
            print(f'{self.nome} esta comendo, acabe de comer primeiro.')
            return

        print(f'{self.nome} esta falando sobre {assunto}')
        self.falando = True

    def stop_falar(self):
        if not self.comendo:
            print(f'{self.nome} não está falando mais')
            return

        self.falando = False
        print(f'{self.nome} já acabou de falar')

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

    @classmethod
    def cria_pessoa(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_random():
        return randint(1, 99999)
        