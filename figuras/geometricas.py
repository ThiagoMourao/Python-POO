class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

    def __call__(self, *args, **kwargs): #caso de chamadas simples da classe
        print(args)
        print(kwargs)

    def __setattr__(self, key, value): #seta novas variaveis a classe
        self.__dict__[key] = value
        print(key, value)

    def __str__(self): # printar so a classe em si
        return 'A classe retangulo foi criada pra calculos'

    def __len__(self): #retorna a chamada do len da classe (tamanho)
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

    def __lt__(self, other): # self < other, neste caso são os dois objetos como parametro
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):# self > other
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other):# self == other(neste caso compara se os valores do objeto são iguais, e não o objeto em si)
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False    
