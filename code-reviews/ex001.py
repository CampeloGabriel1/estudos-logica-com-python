#Declaração de variáveis
#Atribuição de valores
#Nomes de variáveis(nome, tipo, xp)
#Reatribuição de valores(xp = xp + 1500)
#Tipos de dados(Str, Str, Int)

"""
Exemplo de declaração, atribuição e reatribuição de variáveis em Python.
Variáveis: nome (str), tipo (str), xp (int)
"""

nome = "Gandalf"
tipo = "Mago"
xp = 1500

xp = xp + 1500
xp += 1500  # Reatribuição usando operador +=

print(f"Seu personagem é {nome}, do tipo {tipo}, e xp: {xp}")

# Exibindo os tipos das variáveis
print(f"Tipo de nome: {type(nome).__name__}")
print(f"Tipo de tipo: {type(tipo).__name__}")
print(f"Tipo de xp: {type(xp).__name__}")