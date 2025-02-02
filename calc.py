def calculodamedia(nota1, nota2, nota3, nota4):
    soma = nota1*2 + nota2*2 + nota3*3 + nota4*4
    media = soma / 100
    if media >= 6:
        print('Aprovado.')
    else:
        print('Reprovado.')

a = int(input('Insira sua nota a etapa 1: '))
b = int(input('Insira sua nota a etapa 2: '))
c = int(input('Insira sua nota a etapa 3: '))
d = int(input('Insira sua nota a etapa 4: '))

calculodamedia(a, b, c, d)