def carregar_arquivo_colaborador(arquivo):
    pass


def carregar_arquivo_fornecedor(arquivo):
    pass


def checar_arquivo(arquivo):
    try:
        arq = open(arquivo, 'rt')
        arq.close()
    except FileNotFoundError:
        print('\033[0;31mERRO: Arquivo não existe!\033[m')
        return False
    else:
        return True


def salvar_arquivo_colaborador(lista):
    try:
        arq = open('colaborador.txt', 'wt+')
        for c in lista:
            arq.write(c)
    except FileExistsError:
        print('\033[0;31mERRO: Falha ao tentar salvar!\033[m')


def salvar_arquivo_fornecedor():
    pass
