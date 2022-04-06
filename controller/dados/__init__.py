def carregar_arquivo_colaborador(arquivo):
    try:
        arq = open(arquivo, 'rt')
    except FileNotFoundError:
        print('\033[0;31mERRO: Arquivo informado não existe!')
    else:
        lista = list()
        for c in arq:
            funcionario = c.split(';')
            funcionario[len(funcionario) - 1] = funcionario[len(funcionario) - 1].replace('\n', '')
            lista.append(funcionario)
        arq.close()
        return lista


def carregar_arquivo_fornecedor(arquivo):
    try:
        arq = open(arquivo, 'rt')
    except FileNotFoundError:
        print('\033[0;31mERRO: Arquivo informado não existe!')
    else:
        lista = list()
        for c in arq:
            terceirizado = c.split(';')
            terceirizado[len(terceirizado) - 1] = terceirizado[len(terceirizado) - 1].replace('\n', '')
            lista.append(terceirizado)
        arq.close()
        return lista


def checar_arquivo(arquivo):
    try:
        arq = open(arquivo, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def salvar_arquivo_colaborador(lista):
    try:
        arq = open('colaborador.txt', 'wt+')
        for c in lista:
            arq.write(f'{c.nome};{c.funcao};{c.setor};{c.matricula} \n')
    except FileExistsError:
        print('\033[0;31mERRO: Falha ao tentar salvar!\033[m')
    else:
        arq.close()


def salvar_arquivo_fornecedor(lista):
    try:
        arq = open('fornecedor.txt', 'wt+')
        for f in lista:
            arq.write(f'{f.nome};{f.funcao};{f.empresa};{f.cpf} \n')
    except FileExistsError:
        print('\033[0;31mERRO: Falha ao tentar salvar!\033[m')
    else:
        arq.close()
