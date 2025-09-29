import random

def create_deck():
  naipes = ['Copas', 'Ouros', 'Paus', 'Espadas']
  ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
  baralho = []

  for naipe in naipes:
    for rank in ranks:
      baralho.append(f"{rank} de {naipe}")

  random.shuffle(baralho)

  return baralho

def deal_card(deck):
  return False

meu_baralho = create_deck()
print(meu_baralho)
print(f"Total de cartas: {len(meu_baralho)}")
