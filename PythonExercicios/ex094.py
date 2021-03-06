# Crie um programa que leia nome, sexo e idade de varias pessoas,
# guardando cada pessoa em um dicionario e todos os dicionarios em uma lista
# No final mostre:
# a) Quantas pessoas foram cadastradas
# b) A média de idade do grupo
# c) Uma lista com todas as mulheres
# d) Uma lista com todas as pessoas com idade acima da media

info = {}
pessoas = []
somaIdade =0
while True:
    info.clear()
    info['nome'] = str(input('Digite o nome: '))
    while True:
        info['sexo'] = str(input('Digite o sexo [M/F]: ')).upper().split()[0]
        if info['sexo'] in 'MF':
            break
    info['idade'] = int(input('Digite a idade: '))
    somaIdade += info['idade']
    pessoas.append(info.copy())

    resp = str(input('Deseja continuar? [S/N]: ')).upper().split()[0]
    if resp == 'N':
        break
    while True:
        if resp not in 'NS':
            print('Digite somente S ou N!')
        else:
            break

print(f'Pessoas cadastradas: {len(pessoas)}')
print('As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(p['nome'], end=', ')
media = somaIdade / len(pessoas)
print(f'\nMedia do grupo: {media:5.2f}')
print('Pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] > media:
        print(p)
