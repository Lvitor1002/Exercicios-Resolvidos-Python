
# Outro exemplo:
for i in range(10,0,-1):  #'-1' = Contando de trás para frente
    print(f"{i}ª = oi\n")
print("-=-"*30)

#------------------------------------------------------------------------------------

# Outro exemplo:
for i in range(1,11,2):  #'2' = Contando normal, porém de 2 em 2
    print(f"{i+1}ª = oi\n")
print("-=-"*30)

#------------------------------------------------------------------------------------

# Outro exemplo:
n = int(input("Digite um número: "))
for i in range(0,n):
    print(f"{i+1}ª = {n}\n")
print("-=-"*30)

#------------------------------------------------------------------------------------

# Outro exemplo:
inicio = int(input("Digite um número para o começo: "))
fim = int(input("Digite um número para o fim: "))
passo = int(input("Digite um número para os passos: "))

for i in range(inicio, fim, passo):
    print(f"{i+1}ª = {n}\n")
print("-=-"*30)


#------------------------------------------------------------------------------------

# Outro exemplo:

s = 0
for c in range(0,4):
    n = int(input("Digite um número: "))
    s += n
print(f"O somatório total foi: {s}\n")