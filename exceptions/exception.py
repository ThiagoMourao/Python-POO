class UmErroEspecificoError(Exception): pass

def testar():
    raise UmErroEspecificoError('Errado!')

