"""
Convenção de não uso
_ Protected

__ Private 
"""

class Cliente:
    def __init__(self):
        self.__dados = {} #com 2 anderlines, recria a variavel em memoria com outro nome        

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id] 
