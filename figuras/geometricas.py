from dataclasses import dataclass
import math

"""
Responsavel por criar e manipular objetos geometricos

Lorem ipsum dolor sit amet, consectetur adiposcing elit, Vivamus
"""""

#meta classes
class Meta(type): 
    def __new__(mcs, name, bases, namespace):
        print(f'{name} ! \n' )
        
        # garante que os tratamentos não sejá feito na class 'pai'
        if name == 'Retangulo': 
            return type.__new__(mcs, name, bases, namespace)

        if 'attr_class' in namespace:
            print(f'{name} tentou sobrescrever o atributo, a regra de negocio não permite nesse caso! \n')
            del namespace['attr_class']

        # garante a criação de funçoes obrigatorias em classes que herdam
        if 'get_area' not in namespace: 
            print(f'Erro ao instanciar a class {name}, favor criar a função get_area \n nas classes que herdam de Retangulo!')
            return None
        elif not callable(namespace['get_area']):
            print(f'get_area precisa ser um método, e não um atributo, em {name}')
            return None


        print(f'{namespace} ! \n' )
        return type.__new__(mcs, name, bases, namespace)

class Retangulo(metaclass= Meta):
    attr_class = 'cálculo do Retangulo'
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # executado logo apos o __init__, pode ser util para fazer algum controle
    def __post_init__(self):
        pass
        

    #caso de chamadas simples da classe
    def __call__(self, *args, **kwargs): 
        print(args)
        print(kwargs)

    #seta novas variaveis a classe
    def __setattr__(self, key, value): 
        self.__dict__[key] = value
        print(key, value)

    # printar so a classe em si
    def __str__(self): 
        return 'A classe retangulo foi criada pra calculos'

    #retorna a chamada do len da classe (tamanho)
    def __len__(self): 
        return 51
    
    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    def get_area(self):
        return self.x * self.y

    #sobrecarga - redefinir operações de comparação, por exemplo
    def __add__(self, other): 
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Retangulo(new_x, new_y)

    # self < other, neste caso são os dois objetos como parametro
    def __lt__(self, other): 
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False
    
    # self > other
    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    # self == other(neste caso compara se os valores do objeto são iguais, e não o objeto em si)
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False    

#Responsavel por criar e manipular objetos geometricos
class Quadrado(Retangulo):
    """
    Documentação da classse Quadrado

    Esta é um exemplo de documentação para fins de estudos e testes praticos
    """""
    def __init__(self, x, y):
        Retangulo.__init__(self, x, y)

    attr_class = 'cálculo do quadrado'

    def get_area(self):
        """
        multiplica os lados

        :param x: Primeiro numero
        :type x: int or float
        :param y: Segundo numero
        :type y: int or float

        :return: A multiplicação entre x e y
        :rtype: int or float
        """
        return self.x * self.y

#data classes
@dataclass()
class Circulo:
    raio: float
    
    def __post_init__(self):
        if not (isinstance(self.raio, float)) and not (isinstance(self.raio, int)):
            raise TypeError(
                f'Tipo invalido {type(self.raio).__name__} != float or int em {self}'
            ) 

    def area(self):
        return math.pi * (self.raio ** 2) 
