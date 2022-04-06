from model.fornecedor import Fornecedor
from model.colaborador import Colaborador


def valida_string(msg):
    """
    Função para validação de caracteres alfabéticos.

            Parameters:
             msg: recebe uma mensagem passada na requisição.

            Exception:
             É lançada uma exceção de ValueError caso o valor recebido não atinja os requisitos;

            Except:
            É exibido ao usuário uma mensagem amigável mostrando o que deve ser feito;

            Returns:
                palavra(str): retorna a palavra ou caractere recebido após validação;
    Criado por David Esly em 06/04/2022
    """
    while True:
        try:
            palavra = str(input(msg)).strip()
            palavra2 = "".join(palavra.split())
            if not palavra2.isalpha():
                raise ValueError
        except ValueError:
            print('\033[0;31mERRO: Entrada inválida, por favor digitar apenas caracteres alfabéticos\033[m')
        else:
            return palavra.title()


def valida_inteiro(msg):
    while True:
        try:
            num = int(input(msg).strip())
            if num <= 0:
                raise ValueError
        except ValueError:
            print('\033[0;31mERRO: Digite apenas valores inteiros válidos!\033[m')
        else:
            return num


def valida_cpf(msg):
    while True:
        try:
            cpf = str(input(msg)).strip()
            if not cpf.isnumeric() or len(cpf) < 11 or len(cpf) > 11:
                raise ValueError
        except ValueError:
            print('\033[0;31mERRO: CPF Inválido!\033[m')
        else:
            return cpf


def menu(msg, opcoes):
    while True:
        try:
            print(msg)
            for p, op in enumerate(opcoes):
                print(f'{p + 1} - {op}')
            escolha = valida_inteiro("Sua escolha: ")
            if escolha > len(opcoes) or escolha < 1:
                raise ValueError
        except ValueError:
            print('\033[0;31mERRO: Opção inválida!\033[m')
        else:
            return escolha


colaborador = list()
fornecedor = list()
pessoas = list()


def adicionar_pessoa():
    op = menu('Que cadastro você gostaria de realizar:', ['Colaborador', 'Fornecedor', 'Sair'])
    nome = valida_string('Nome: ')
    funcao = valida_string('Função: ')
    if op == 1:
        colaborador.append(
            Colaborador(nome, funcao, valida_string('Digite o setor: '), valida_inteiro('Digite a matricula: ')))
        print(f'Colaborador {nome} cadastrado com sucesso!')
    elif op == 2:
        fornecedor.append(Fornecedor(nome, funcao, valida_string('Empresa:'), valida_cpf('CPF: ')))
        print(f'Fornecedor {nome} cadastrador com sucesso!')
    else:
        return


def editar_pessoa():
    op = listar_pessoa('Que tipo de pessoa você deseja alterar?')
    if op == 1:
        pos = busca_colaborador("Digite a matricula do colaborador que deseja alterar: ")
        alt_op = menu(f'O que você deseja alterar do colaborador {colaborador[pos].nome}: ',
                      ['Nome', 'Função', 'Setor', 'Sair'])
        if alt_op == 1:
            colaborador[pos].nome = valida_string('Nome: ')
            print('Alterado com sucesso!')
        elif alt_op == 2:
            colaborador[pos].funcao = valida_string('Função: ')
            print('Alterado com sucesso!')
        elif alt_op == 3:
            colaborador[pos].setor = valida_string('Setor: ')
            print('Alterado com sucesso!')
        else:
            return
    elif op == 2:
        pos = busca_fornecedor("Digite o cpf do fornecedor que deseja alterar: ")
        alt_op = menu(f'O que você deseja alterar do fornecedor {fornecedor[pos].nome}: ',
                      ['Nome', 'Função', 'Sair'])
        if alt_op == 1:
            fornecedor[pos].nome = valida_string('Nome: ')
            print('Alterado com sucesso!')
        elif alt_op == 2:
            fornecedor[pos].funcao = valida_string('Função: ')
            print('Alterado com sucesso!')
        else:
            return
    else:
        return


def excluir_pessoa():
    op = listar_pessoa('Que tipo de pessoa você deseja excluir: ')
    if op == 1:
        pos = busca_colaborador("Digite a matricula do colaborador que você deseja excluir: ")
        while True:
            sim_nao = valida_string(f"Você tem certeza que deseja excluir o colaborador {colaborador[pos].nome}?"
                                    f" [S/N] ")[0].strip().lower()
            while sim_nao not in "sn":
                sim_nao = valida_string(f"Você tem certeza que deseja excluir o colaborador {colaborador[pos].nome}?"
                                        f" [S/N] ")[0].strip().lower()
            if sim_nao == 's':
                colaborador.pop(pos)
                print('Colaborador excluído com sucesso!')
                break
            elif sim_nao == 'n':
                break
    elif op == 2:
        pos = busca_fornecedor("Digite o CPF do fornecedor que você deseja excluir: ")
        while True:
            sim_nao = valida_string(f"Você tem certeza que deseja excluir o fornecedor {fornecedor[pos].nome}?"
                                    f" [S/N] ")[0].strip().lower()
            while sim_nao not in "sn":
                sim_nao = valida_string(f"Você tem certeza que deseja excluir o colaborador {fornecedor[pos].nome}?"
                                        f" [S/N] ")[0].strip().lower()
            if sim_nao == 's':
                fornecedor.pop(pos)
                print('Fornecedor excluído com sucesso!')
                break
            elif sim_nao == 'n':
                break


def listar_pessoa(msg):
    op = menu(msg, ['Colaborador', 'Fornecedor', 'Sair'])
    if op == 1:
        print(f'Total de colaboradores cadastrados: {Colaborador.total()}')
        for p, c in enumerate(colaborador):
            print(f'{p + 1} - {c}')
        return op
    elif op == 2:
        print(f'Total de fornecedores cadastrados: {Fornecedor.total()}')
        for p, f in enumerate(fornecedor):
            print(f'{p + 1} - {f}')
        return op
    else:
        return 0


def busca_colaborador(msg):
    mat = valida_inteiro(msg)
    pos = 0
    for p, c in enumerate(colaborador):
        if c.matricula == mat:
            pos = p
    return pos


def busca_fornecedor(msg):
    cpf = valida_cpf(msg)
    pos = 0
    for p, f in enumerate(fornecedor):
        if cpf == f.cpf:
            pos = p
    return pos
