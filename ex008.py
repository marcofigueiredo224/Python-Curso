salario = float(input('Qual o salário do funcionário? '))
novo = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${}, com o aumento de 15% irá ganhar {:.2f}R$'.format(salario, novo))
