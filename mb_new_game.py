import random
import os

os.system("clear")

# import random package from python standard library

# define suits and numbers of cards
suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
numbers = [14, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
deck = []
player1_card = []
player2_card = []
player1_pack = []
player2_pack = []


# create a deck of cards
def create_deck():
    for suit in suits:
        for number in numbers:
            card = [number, suit]
            deck.append(card)

    # shuffle the deck of cards
    random.shuffle(deck)

    return deck


# process the card number to display the card name
def process_card(card_number):
    if card_number == 14:
        return "Ace"
    elif card_number == 11:
        return "Jack"
    elif card_number == 12:
        return "Queen"
    elif card_number == 13:
        return "King"
    else:
        return card_number


# create a deck of cards
deck_of_cards = create_deck()

# play the game
while len(deck_of_cards) > 1:
    # pause game and wait for input
    input("press enter to deal")

    # deal player 1 and remove card from deck
    player1_card = random.choice(deck_of_cards)
    deck_of_cards.remove(player1_card)  # remove card from deck

    # deal player 2 and remove card from deck
    player2_card = random.choice(deck_of_cards)
    deck_of_cards.remove(player2_card)  # remove card from deck

    # clear the console
    os.system("clear")

    # display the cards
    print(f" Player 1 Card: {process_card(
        player1_card[0])} of {player1_card[1]}")
    print(f" Player 2 Card: {process_card(
        player2_card[0])} of {player2_card[1]}")

    # compare the cards
    if player1_card[0] > player2_card[0]:
        print("Player 1 wins this hand!")

        # add the cards to the player's pack
        player1_pack.append(player1_card)
        player1_pack.append(player2_card)

    elif player1_card[0] < player2_card[0]:
        print("Player 2 wins this hand!")

        # add the cards to the player's pack
        player2_pack.append(player1_card)
        player2_pack.append(player2_card)

    else:
        print("It's a draw!!")

        # add the cards to the player's pack
        player1_pack.append(player1_card)
        player2_pack.append(player2_card)

    # display the number of cards left in the deck
    print(f"\nNumber of cards left: {len(deck_of_cards)}\n")


# determine the winner
if len(player1_pack) > len(player2_pack):
    print(
        f"Player 1 Wins the game with {len(player1_pack)} cards over {
            len(player2_pack)} cards!"
    )
elif len(player1_pack) < len(player2_pack):
    print(
        f"Player 2 Wins the game with {len(player2_pack)} cards over {
            len(player1_pack)} cards!"
    )
else:
    print("It's a draw!!")

print()
if input("would you like to see the cards in the player packs (y/n)?").upper() == "Y":
    # display the cards in the player packs
    for card in player1_pack:
        print(f"Player 1 Pack: {process_card(card[0])} of {card[1]}")

    for card in player1_pack:
        print(f"Player 2 Pack: {process_card(card[0])} of {card[1]}")

    print(f"\nThanks for playing!\n")
else:

    print(f"\nThanks for playing!\n")