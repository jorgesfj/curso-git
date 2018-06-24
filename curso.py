n  = input("Digite seu nome: ")
i  = int(input("Digite sua idade: "))
p = input("Qual o seu pais? ")
print('Hello World! {}, voce tem {} anos.\nComo vai o tempo em {} '.format(n,i,p))

if i<18:
	print('Menor de idade')
else:
	print('Maior de idade')	

