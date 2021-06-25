nome = str(input ("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
peso = input("Digite seu peso: ")
print("Seu nome é {}, você tem {} anos, e pesa {} quilos".format(nome, idade, peso))
if (idade <=17):
    print("Você ainda é menor de idade")
else:
    print("Você é maior de idade")
