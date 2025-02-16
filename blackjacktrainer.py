import random
import time

def print_wait(string):
    print(string)
    time.sleep(1)

def main():
    while True:
        play_game()
        while True:
            restart_game = input("Would you like to play again? (y/n): ").lower()
            if restart_game == 'y':
                break
            elif (restart_game == 'n'): # if player enters "n", end the game
                print_wait("Thanks for playing!")
                return
            else:
                print_wait("Invalid input. Please enter 'y' or 'n'.")



# draw a card from the deck and assign a value to face/ace
def draw_card():
    card_int = random.randint(1, 13)

    match card_int:
        case 1:
            card_label = 'A'
            card_value = 11
        case 10:
            card_label = '10'
            card_value = 10
        case 11:
            card_label = 'J'
            card_value = 10
        case 12:
            card_label = 'Q'
            card_value = 10
        case 13:
            card_label = 'K'
            card_value = 10
        case _:
            card_value = card_int
            card_label = str(card_value)

    return card_label, card_value
    # return 'J', 10 # DEBUG - always draw J

# calculate the point value of the hand
def calculate_hand(hand):
    total = sum(card[1] for card in hand)
    num_aces = sum(1 for card in hand if "A" in card[0]) # check for Aces to consider 1/11 assignment

    while (total > 21 and num_aces > 0):
        total -= 10
        num_aces -= 1

    return total

# print_wait the hand and (optional) point value
def display_hand(name, hand, total = None, hide_second_card = False):
    if (hide_second_card):
        print(f"{name}: ['{hand[0][0]}', '??']")
    else:
        print_wait(f"{name}: {str([card[0] for card in hand])} {total}")
            
# player turn to hit or stand
def player_turn(player_hand, dealer_hand):
    player_total = calculate_hand(player_hand)

    while (player_total < 21):
        action = input("Would you like to hit (h) or stand (s)? ").lower()

        if (action == 'h'):
            print_wait("Player hits.")
            player_hand.append(draw_card())
            player_total = calculate_hand(player_hand)
            display_hand("Dealer", dealer_hand, hide_second_card=True)
            display_hand("Player", player_hand, player_total)

            if player_total > 21:
                print_wait("Player busts.")
                return
            
            if player_total == 21:
                print_wait("Player has 21")
                return

        elif (action == 's'):
            print_wait("Player stands.")
            break

        else:
            print_wait("Invalid input. Please enter 'h' or 's'.")

def dealer_turn(dealer_hand):
    # dealer draws while below 17
    dealer_total = calculate_hand(dealer_hand)
    while (dealer_total < 17):
        dealer_hand.append(draw_card())
        dealer_total = calculate_hand(dealer_hand)
        display_hand("Dealer", dealer_hand, dealer_total)
        if (dealer_total > 21):
            print_wait(f"Dealer busts.")
            return # end game if dealer busts
        if (dealer_total >= 17):
            print_wait(f"Dealer stands.")
        
        
# display the final results
def results(hand_name, player_hand, dealer_hand):
    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)

    print_wait(f"{hand_name} Results:")
    display_hand("Dealer", dealer_hand, dealer_total, hide_second_card=False)
    display_hand("Player", player_hand, player_total)

    if ((player_total <= 21) and ((dealer_total > 21) or (player_total > dealer_total))):
        print_wait("Player wins. Congratulations!")
    elif (player_total == dealer_total):
        print_wait("It's a tie.")
    else:
        print_wait("Dealer wins.")


def play_game():
    # create the dealer and player hands and draw two cards for each
    dealer_hand = []
    player_hand = []

    player_hand.append(draw_card())
    player_hand.append(draw_card())
    player_total = calculate_hand(player_hand)

    dealer_hand.append(draw_card())
    dealer_hand.append(draw_card())

    display_hand("Dealer", dealer_hand, hide_second_card=True)
    display_hand("Player", player_hand, player_total)

    # check for blackjack
    if (player_total == 21):
        print_wait("Blackjack! You win!")
        return
    
    # check for split
    if (player_hand[0][0] == player_hand[1][0]):
        while True:
            action = input(f"Would you like to split? (y/n) ").lower()
            if (action == 'y'):
                print_wait(f"Player splits.")
                hand1 = [player_hand[0], draw_card()]
                hand2 = [player_hand[1], draw_card()]

                display_hand("Dealer", dealer_hand, hide_second_card=True)
                display_hand("Player H1", hand1, calculate_hand(hand1))
                player_turn(hand1, dealer_hand)

                display_hand("Dealer", dealer_hand, hide_second_card=True)
                display_hand("Player H2", hand2, calculate_hand(hand2))
                player_turn(hand2, dealer_hand)

                dealer_turn(dealer_hand)

                results("Player H1", hand1, dealer_hand)
                results("Player H2", hand2, dealer_hand)

                return

            elif (action == 'n'):
                break

            else:
                print_wait("Invalid input. Please enter 'y' or 'n'.")

    else:
        player_turn(player_hand, dealer_hand)
        dealer_turn(dealer_hand)
        results("Player H1", player_hand, dealer_hand)

main()