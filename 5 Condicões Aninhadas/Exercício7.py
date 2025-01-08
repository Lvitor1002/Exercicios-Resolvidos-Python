'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso atual: "))

imc = (peso / (altura ** 2))

if imc < 18.5:
    print(f"\nVocê está abaixo do peso.\n")
elif imc >= 18.5 and imc < 25:
    print("\nPeso ideal. Parabéns!!\n")
elif imc >= 25 and imc < 30:
    print("\nCuidado. Você está em sobrepeso!!\n")
elif imc >= 30 and imc < 40:
    print("\nAtenção, obesidade! Você está muito acima do peso.\n")
else:
    print("\nAlerta, obesidade mórbida. Risco de vida! Você está além do limite de peso corporal máximo aceitável. Procure um médico.\n\n")