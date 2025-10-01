import random

def create_deck():
  suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
  ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

  deck = []

  # Calculating each card's value
  for suit in suits:
    for rank in ranks:
      if rank == 'A':
          value = 11 # The Ace beggins as 11. If needed, it's adjusted in calculate_hand().
      elif rank in ['J', 'K', 'Q']:
          value = 10
      else:
          value = int(rank)

      card = {'rank': rank,'suit': suit, 'value': value}
      deck.append(card)

  random.shuffle(deck)

  return deck


#
def deal_card(deck):
  card = deck.pop() # Taking the last card from the shuffled deck
  return card


#
def calculate_hand(hand):
  total = 0
  ace_count = 0

  for card in hand:
    total += card['value']

  for card in hand:
    if card['rank'] == 'A':
      ace_count += 1

  while total > 21 and ace_count > 0:
    total -= 10
    ace_count -= 1

  return total


#
def player_turn(deck, player_hand):
  while True:
    player_score = calculate_hand(player_hand)

    hand_text_list = []
    for card in player_hand:
        hand_text_list.append(f"{card['rank']} of {card['suit']}")

    print(f"Your hand: {', '.join(hand_text_list)}")
    print(f"Your Score: {player_score}")

    if player_score > 21:
      break

    player_choice = input("\nWhat do you want to do? \n1 - Hit\n2 - Stand\nChoice: ")

    if player_choice == '1':
      new_card = deal_card(deck)
      player_hand.append(new_card)
    elif player_choice == '2':
      print("\nYou chose to stand.")
      break
    else:
      print("Enter a valid option.")


#
def dealer_turn(deck, dealer_hand):
  print("--Dealer's turn--")


#
def play_game():
  game_deck = create_deck()

  player_hand = []
  dealer_hand = []

  for _ in range(2):
    player_hand.append(deal_card(game_deck))
    dealer_hand.append(deal_card(game_deck))

  print(f"Dealer shows: {dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}")

  player_turn(game_deck, player_hand)
  player_score = calculate_hand(player_hand)

  if player_score > 21:
    print("\nYou busted!!")
    print(f"Final score: {player_score}")
  else:
    dealer_hand = dealer_turn(game_deck, dealer_hand)

play_game()
