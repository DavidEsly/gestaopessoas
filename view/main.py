from interface import *

carrega_dados()
while True:

    op = menu('Sistema de gestão de Pessoa', ['Cadastrar', 'Listar', 'Editar', 'Excluir', 'Sair'])

    if op == 1:
        adicionar_pessoa()
    elif op == 2:
        listar_pessoa('Escolha o tipo de cadastro você quer listar.')
    elif op == 3:
        editar_pessoa()
    elif op == 4:
        excluir_pessoa()
    elif op == 5:
        salvar()
        print('Vocês está saindo do sistema! Até logo!')
        break
