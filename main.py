import random
import art
from replit import clear

card_deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 14, 14]
player_hand = []
computer_hand = []
divider = "------------------------------------------------------------"

def deal_cards(deck, hand, split):
    random.shuffle(deck)
    if split == "y":
        split_deck = card_deck[:int(len(card_deck)/2)], card_deck[(len(card_deck) - int(len(card_deck)/2)):]
        
        return split_deck[0], split_deck[1]
    else: 
        return deck + hand

def war(deck, player, computer):
    # Assemble the war rewards deck
    for n in range(1, 3):
        deck.append(player.pop())
        deck.append(computer.pop())

    # Display the cards compared in the war
    print(f"You draw: {art.card_art[deck[len(deck) - 2] - 2]}")
    print(f"Computer draws: {art.card_art[deck[len(deck) - 1] - 2]}")

    # Check if player wins the war
    if deck[len(deck) - 2] > deck[len(deck) - 1]:
        print("Player wins war!")
        
        return deal_cards(deck, player, "n"), computer
    else:
        print("Computer wins war!") # Decide what to do if a second matching set of cards occurs; for now the computer will just win
        
        return player, deal_cards(deck, computer, "n")

def compare_cards(player, computer):
     # Assemble the rewards deck
    reward_cards = [player.pop(), computer.pop()]

    # Display cards drawn
    print(f"You draw: {art.card_art[reward_cards[0] - 2]}")
    print(f"Computer draws: {art.card_art[reward_cards[1] - 2]}")
    
    if reward_cards[0] == reward_cards[1]:
        # Initiate a war
        print("Uh oh... This means war!")
        
        return war(reward_cards, player, computer) 
        
    elif reward_cards[0] > reward_cards[1]:
        # Add reward cards to front of player's hand
        print("You win the round!")
        
        return deal_cards(reward_cards, player, "n"), computer
    else:
        # Add reward cards to front of computer's hand
        print("The computer wins the round!")
        
        return player, deal_cards(reward_cards, computer, "n")


# Greet user
print(art.logo)
print("Welcome to War!")
print(divider)

# Generate player and computer starting hands
player_hand, computer_hand = deal_cards(card_deck, player_hand, "y")

# Main gameplay loop runs while both players have cards in their hands
continue_playing = True
while continue_playing:
    # Stop game if player or computer has no cards left in hand
    if len(player_hand) != 0 and len(computer_hand) != 0:
        start_round = input("Type 'r' to draw cards: ").lower()
        # start_round = "r"
        
        if start_round == "r":
            clear()
            print(art.logo)
            print("Game in progress!")
            print(divider)

            # Compare drawn cards and update player and computer hands
            player_hand, computer_hand = compare_cards(player_hand, computer_hand)

            print(f"You have {len(player_hand)} cards left.")
            print(f"The computer has {len(computer_hand)} cards left.")
            print(divider)
        else:
            print("Okay, maybe next time. Goodbye!")
            continue_playing = False
    else:
        continue_playing = False
        
# Display winner if player did not quit
if start_round == "r":
    print(divider)
    if len(player_hand) > 0:
        print("Congrats, you win!")
    else:
        print("Oops, looks like the computer wins.")