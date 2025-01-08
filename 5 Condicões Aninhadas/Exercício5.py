
'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''
from datetime import date

nascimento = int(input("Digite o ano de seu nascimento com quatro dígitos: "))
ano_atual = date.today().year
idade = ano_atual - nascimento

if idade <= 9:
    print("_=__"*20)
    print(f"\n\tIdade: {idade}\n\n\tCategoria Mirim\n")
    print("_=__"*20)
elif idade > 9 and idade <= 14:
    print("_=__"*20)
    print(f"\n\tIdade: {idade}\n\n\tCategoria Infantil\n")
    print("_=__"*20)
elif idade > 14 and idade <= 19:
    print("_=__"*20)
    print(f"\n\tIdade: {idade}\n\n\tCategoria Júnior\n")
    print("_=__"*20)
elif idade > 19 and idade <= 25:
    print("_=__"*20)
    print(f"\n\tIdade: {idade}\n\n\tCategoria Sênior\n")
    print("_=__"*20)
else:
    print("_=__"*20)
    print(f"\n\tIdade: {idade}\n\n\tCategoria Master\n")
    print("_=__"*20)


