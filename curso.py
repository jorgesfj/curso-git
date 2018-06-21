n  = input("Digite seu nome: ")
i  = int(input("Digite sua idade: "))

print('Hello World! {}, voce tem {} anos. '.format(n,i))

if i<18:
	print('Menor de idade')
else:
	print('Maior de idade')	