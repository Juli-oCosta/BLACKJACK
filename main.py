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

def calculate_hand():
  return False

def player_turn(deck, player_hand):
  while True:
    player_choice = input("\nWhat do you want to do? \n1 - Hit\n2 - Stand\nChoice: ")

    if player_choice == '1':
      new_card = deal_card(deck)
      player_hand.append(new_card)
    elif player_choice == '2':
      print("\nYou chose to stand.")
      break
    else:
      print("Enter a valid option.")








game_deck = create_deck()
print(f"Deck's starting size: {len(game_deck)}")

card_1 = deal_card(game_deck)
card_2 = deal_card(game_deck)

player_hand = [card_1, card_2]
print(f"Player's starting hand: {player_hand}")

print(f"Deck cards: {len(game_deck)} un.")
