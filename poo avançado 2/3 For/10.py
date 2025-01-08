

soma_idade = 0
soma_sexo_f= 0
idades = []
homem_mais_velho = ''
homem_mais_novo = ''

for c in range(1,5):
    print(f'-----{c}ª PESSOA-----')
    nome = str(input('Digite seu nome: ')).strip().title()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()
    if idade:
        soma_idade += idade
    média = soma_idade / 4

    if sexo == 'F' and idade < 20:
        soma_sexo_f += 1

    if sexo == 'M':
        idades.append(idade)
        if idade == max(idades) and sexo == 'M':
            homem_mais_velho = nome

    if sexo == 'M':
        idades.append(idade)
        if idade == min(idades) and sexo == 'M':
            homem_mais_novo = nome 

print(f'\nA média de idade do grupo é de {média} anos de idade!')
print(f'\nO grupo contém {soma_sexo_f} mulheres menores de 20 anos!')
print(f'\nO homem mais velho tem {max(idades)} anos de idade e se chama {homem_mais_velho}!')
print(f'\nO homem mais novo tem {min(idades)} anos de idade e se chama {homem_mais_novo}!\n\n') 