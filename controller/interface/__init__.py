def valida_string(msg):
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
