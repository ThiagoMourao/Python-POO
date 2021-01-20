from contextlib import contextmanager

class Arquivo:
    def __init__(self, arquivo, modo):
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.arquivo.close()

class decorador_arquivo:
    @contextmanager
    def open_arquivo(self, arquivo, modo):
        try:
            arquivo = open(arquivo, modo)
            print('Abrindo arquivo')
            yield arquivo
        finally:
            print('Fechando arquivo')
            arquivo.close()
