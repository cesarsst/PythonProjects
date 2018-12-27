# crie um programa que leia varios numeros inteiros pelo teclado.
# o programa só vai parar quando o usuario digitar 999
# no final mostre quantos numeros foram digitados e qual foi a soma deles

soma = count = n = 0
while n != 999:
    n = int(input('Digite um numero: [999 para parar]: '))
    if n != 999:
        soma += n
        count += 1
print('A soma dos {} valores digitados é : {}'.format(count, soma))

# outra forma:
soma = count = n = 0
n = int(input('Digite um numero: [999 para parar]: '))
while n != 999:
    soma += n
    count += 1
    n = int(input('Digite um numero: [999 para parar]: '))
print('A soma dos {} valores digitados é : {}'.format(count, soma))