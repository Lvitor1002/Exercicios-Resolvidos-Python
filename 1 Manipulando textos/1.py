frase = 'Curso em video python'


print("------------------------------------------------------------------------------")
print(len(frase))  # Tamanho da frase
print()

# Trocando a palavra python por java
print(frase.replace("python", "Java"))
print()

# Trocando a palavra python por java e SALVANDO na variável:
new_frase = frase.replace("python", "Jupyter")
print(new_frase)
print()

print(frase[3:13])  # Do índice 3 até 13
print()

print(frase[1:15:2])  # Do índice 1 até 15, pulando de 2 em 2
print()

print(frase[::2])  # Dois pontos significa a string inteira e pulando de 2 em 2
print()

x = frase.split()  # Dividindo em paalvras
print(f"{x[0]} {x[3]}")  # Juntando as palavras pelos índice
print()


# Para imprimir texto grande basta usar (""""):
# print("""In che modo il computer può aiutarci a comprendere come funziona la nostra lingua? Che cosa significa analizzare un testo con l'aiuto di un calcolatore? In che misura possiamo estendere le potenzialità del computer rendendolo capace di interagire con gli utenti umani nella loro lingua? Queste e altre domande sono l'oggetto di indagine della linguistica computazionale, una disciplina che ha al suo centro proprio il rapporto tra lingua e computer. Il libro fornisce gli elementi di base della linguistica computazionale partendo da un interesse primario per il testo, la sua struttura e il suo contenuto. Il volume propone una sintesi equilibrata e accessibile tra sapere e fare, nozioni di base e loro applicazione, ed è destinato in primo luogo agli studenti delle facoltà umanistiche e scientifiche interessati all'interazione tra scienze umane e informatica, ma anche agli studiosi che vogliano imparare a usare il computer come strumento di ricerca sul linguaggio. """)
print("------------------------------------------------------------------------------")
