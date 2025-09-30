import random

def create_deck():
  suits = ['Copas', 'Ouros', 'Paus', 'Espadas']
  ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

  deck = []

  for suit in suits:
    for rank in ranks:
      if rank == 'A':
          value = 11  # The Ace beggins as 11. A future function will adjust it as needed.
      elif rank in ['J', 'K', 'Q']:
          value = 10
      else:
          value = int(rank)

      card = {'rank': rank,'suit': suit, 'value': value}
      deck.append(card)

  random.shuffle(deck)

  return deck

def deal_card(deck):
  card = deck.pop()
  return card

game_deck = create_deck()
print(f"Deck's starting size: {len(game_deck)}")

card_1 = deal_card(game_deck)
card_2 = deal_card(game_deck)

player_hand = [card_1, card_2]
print(f"Player's starting hand: {player_hand}")

print(f"Deck cards: {len(game_deck)} un.")
