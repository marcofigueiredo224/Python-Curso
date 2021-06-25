n1 = float(input('Primeira nota: '))
n2  = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))

m = (n1 + n2 + n3 + n4) / 4

print('A média do aluno foi {:.2f}'.format(m))

if (m >= 5):
    print(' O aluno foi aprovado!')
else:
    print('O aluno foi reprovado!')

