# Card game taken from tutorial with @mbriscoe
# Clone this repository at &lt;script src=&quot;https://gist.github.com/mbriscoe/e86a35fd2ba1541ab72c408c19bfc33f.js&quot;&gt;&lt;/script&gt;
# <script src="https://gist.github.com/mbriscoe/e86a35fd2ba1541ab72c408c19bfc33f.js"></script>

import random

# create the deck 
suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
numbers = [13, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
deck = []


def create_deck():
    for i in range(1, 52):
        card = [random.choice(numbers), random.choice(suits)]
        deck.append(card)

    return deck

# and define the special cards
def process_card(cardNumber):
    if cardNumber == 13:
        return "Ace"
    elif cardNumber == 10:
        return "Jack"
    elif cardNumber == 11:
        return "Queen"
    elif cardNumber == 12:
        return "King"
    else:
        return cardNumber


deck_of_cards = create_deck()


# what happens when the cards run out
while len(deck_of_cards) > 0:
    input("press enter to deal")
    player_1_card = random.choice(deck_of_cards)
    deck_of_cards.remove(player_1_card)

    player_2_card = random.choice(deck_of_cards)
    deck_of_cards.remove(player_2_card)

    player_1_text = f" Player 1 Card: {process_card(player_1_card[0])} of {
        player_1_card[1]}"
    player_2_text = f" Player 2 Card: {process_card(player_2_card[0])} of {
        player_2_card[1]}"

    print(player_1_text)
    print(player_2_text)

    # if Ace of Spaces is drawn
    if player_1_card[0] == 13 and player_1_card[1] == "Spades":
        print("Player 1 Wins GAME OVER!")
        break
    elif player_2_card[0] == 13 and player_2_card[1] == "Spades":
        print("Player 2 Wins GAME OVER!")
        break

    # if matching cards are drawn
    elif player_1_card[0] > player_2_card[0]:
        print("Player 1 Wins!")
    elif player_1_card[0] < player_2_card[0]:
        print("Player 2 Wins!")
    elif player_1_card[0] == player_2_card[0]:
        print("SNAP!!!!")
        break
    else:
        print("It's a draw!!")

    print(f"Number of cards left: {len(deck_of_cards) + 1}")
