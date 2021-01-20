from pessoa.pessoa import Pessoa
from produto.produto import Produto, CarrinhoDeCompras
from pessoa.cliente import Cliente
from pessoa.escritor import Escritor, Caneta, MaquinaDeEscrever
from pessoa.funcionario import Funcionario, Endereco, Gerente, Diretor, Gerente2
from classes_genericas.abstrato import ContaPoupanca, ContaCorrente
from figuras.geometricas import Retangulo
from arquivos.gerenciador_arquivo import Arquivo, decorador_arquivo


class teste:
    def teste1(self):
        #p1 = Pessoa('Thiago', 23)
        #p2 = Pessoa('Maria', 33)

        p3 = Pessoa.cria_pessoa('Verenice', 1963)

        print(p3.idade)
        print(p3.get_ano_nascimento())

        print(Pessoa.gera_random())

    def teste2(self):
        produto1 = Produto('Camisa', 'R$50')
        produto1.desconto(10)

        print(produto1.nome)
        print(produto1.preco)

        produto2 = Produto('CANECA', 20)
        produto2.desconto(5)

        print(produto2.nome)
        print(produto2.preco)

    def teste_encapsulamento(self):
        bd = Cliente()
        bd.inserir_cliente(1, 'Thiago')
        bd.inserir_cliente(2, 'Ana')
        bd.inserir_cliente(3, 'Marcos')
        
        #bd.apaga_cliente(2)
        #bd.lista_clientes()

        bd.__dados = 'Teste 123'

        print(bd.__dados) #acessa a variavel que em memoria __dados
        print(bd._Cliente__dados) # acessa a variavel em memoria alterada pela classe, a partir do momento em que se instancia o objeto com variavel com 2 anderlines
        
        print(bd.dados) #Com Get consegue acessar o valor

    def teste_associacao(self): # só passa um objeto como paramentro
        escritor = Escritor('Jao')
        #print(escritor.nome)

        caneta = Caneta('Bic')
        #print(caneta.marca)

        maquina = MaquinaDeEscrever()
        #print(maquina)

        escritor.ferramenta = maquina
        escritor.ferramenta.escrever()

    def teste_agregado(self): # ainda independentes, mas foram feitas para funcionar juntos
        carrinho = CarrinhoDeCompras()

        produto1 = Produto('Banana', 5)
        produto2 = Produto('Copo', 15)
        produto3 = Produto('iPhone', 10000)
        
        carrinho.inserir_produto(produto1)
        carrinho.inserir_produto(produto2)
        carrinho.inserir_produto(produto3)

        carrinho.lista_produtos()
        print(f'O total e:{carrinho.soma_total()}')

    def teste_composicao(self): # dependencia total de instanciamento
        func1 = Funcionario('Maria', 32, 'carteira1')
        func1.insere_endereco('Belo Horizonte', 'MG')
        print(f'{func1.nome}, e seus enderecos:')
        func1.lista_enderecos()

        func2 = Funcionario('Tez', 55, 'carteira2')
        func2.insere_endereco('Salvador', 'BA')
        func2.insere_endereco('Rio de Janeiro', 'RJ')
        print(f'{func2.nome}, e seus enderecos:')
        func2.lista_enderecos()   

    def teste_heranca_simples(self):
        gerente1 = Gerente('Marcos', 20)
        gerente1.gerenciar()

    def teste_sobreposicao(self):
        diretor1 = Diretor('John', 47, 11122233355)
        diretor1.gerenciar()
        print(diretor1.cpf)

    def teste_heranca_mutipla(self):
        gerente2 = Gerente2('Carlos', 45, 22299988877)
        gerente2.gerenciar_estoque()

    def teste_classe_abstrata(self):
        #obj = ContaPoupanca(1111, 2222, 0)
        #obj.depositar(10)
        #obj.sacar(5)

        obj = ContaCorrente(1111, 2222, 0, 500)
        obj.depositar(100)
        obj.sacar(250)
        obj.sacar(500)

    def teste_sobrecarga(self):
        r1 = Retangulo(10, 20)
        r2 = Retangulo(10, 20)
        r3 = r1 + r2
        print(r1 == r2)

    def teste_metodos_magicos(self):
        a = Retangulo(5,5)
        a(1,2,3,4,5, nome='Thiago')    

        a.nome = 10
        print (a.nome)

        print(a)

    def gerenciador_contexto(self):
        #with Arquivo('arquivos/texto.txt', 'w') as arquivo:
        #    arquivo.write('testando escrita')
        
       decorador = decorador_arquivo()
       with decorador.open_arquivo('arquivos/texto.txt', 'w') as arquivo:
           arquivo.write('Linha 1 de teste')

