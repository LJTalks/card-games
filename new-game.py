import random

# Create a full deck of cards with all numbers and suits
def create_deck():
    suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # 1 will be used for Ace
    deck = []

    # Create a deck of 52 unique cards
    for suit in suits:
        for number in numbers:
            deck.append((number, suit))

    return deck

# Process card numbers to return face card names
def process_card(card_number):
    if card_number == 1:
        return "Ace"
    elif card_number == 11:
        return "Jack"
    elif card_number == 12:
        return "Queen"
    elif card_number == 13:
        return "King"
    else:
        return str(card_number)

# Initialize deck and shuffle it
deck_of_cards = create_deck()
random.shuffle(deck_of_cards)

# Initialize player scores
player_1_score = 0
player_2_score = 0

# Main game loop - runs until the deck is empty or a game-ending condition is met
# while len(deck_of_cards) > 1:
    # input("Press Enter to deal cards...")

    # Draw cards for both players
    # player_1_card = deck_of_cards.pop()
    # player_2_card = deck_of_cards.pop()

    # Display the cards each player drew
    # player_1_text = f"Player 1 Card: {process_card(player_1_card[0])} of {player_1_card[1]}"
    # player_2_text = f"Player 2 Card: {process_card(player_2_card[0])} of {player_2_card[1]}"
    # print(player_1_text)
    # print(player_2_text)

    # Check for Ace of Spades win condition
    # if player_1_card[0] == 1 and player_1_card[1] == "Spades":
        # print("Player 1 draws the Ace of Spades! Player 1 Wins GAME OVER!")
        # break
    # elif player_2_card[0] == 1 and player_2_card[1] == "Spades":
        # print("Player 2 draws the Ace of Spades! Player 2 Wins GAME OVER!")
        # break

    # Compare card values to determine the winner of the round
    # if player_1_card[0] > player_2_card[0]:
        # print("Player 1 Wins the Round!")
        # player_1_score += player_1_card[0] + player_2_card[0]  # Add both card values to Player 1's score
    # elif player_1_card[0] < player_2_card[0]:
        # print("Player 2 Wins the Round!")
        # player_2_score += player_1_card[0] + player_2_card[0]  # Add both card values to Player 2's score
    # else:
        # print("SNAP!!!! Both players drew the same card value!")
        # if player_1_score > player_2_score:
            # print("Player 1 wins the SNAP round and takes all played cards!")
            # player_1_score += player_1_card[0] + player_2_card[0]  # Collect all cards for Player 1
        # elif player_2_score > player_1_score:
            # print("Player 2 wins the SNAP round and takes all played cards!")
            # player_2_score += player_1_card[0] + player_2_card[0]  # Collect all cards for Player 2
        # else:
            # print("It's a tie! No one wins the SNAP round.")

    # Print current scores
#    print(f"Scores -> Player 1: {player_1_score}, Player 2: {player_2_score}")
    # print(f"Number of cards left: {len(deck_of_cards)}")

# End of game
#print("Game Over! Final Scores:")
#print(f"Player 1: {player_1_score}")
#print(f"Player 2: {player_2_score}")

#if player_1_score > player_2_score:
#    print("Player 1 is the overall winner!")
#elif player_2_score > player_1_score:
#    print("Player 2 is the overall winner!")
#else:
#    print("The game is a draw!")
