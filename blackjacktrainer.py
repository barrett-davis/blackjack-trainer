import random
import time

def main():
    while True:
        play_game()
        while True:
            restart_game = input("Would you like to play again? (y/n): ").lower()
            if restart_game == 'y':
                break
            elif (restart_game == 'n'):
                print("Thanks for playing!")
                return
            else:
                print("Invalid input. Please enter 'y' or 'n'.")




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

def calculate_hand(hand):
    total = sum(card[1] for card in hand)
    num_aces = sum(1 for card in hand if "A" in card[0])

    while (total > 21 and num_aces > 0):
        total -= 10
        num_aces -= 1

    return total


def display_hand(name, hand, total = None, hide_second_card = False):
    if (hide_second_card):
        print(f"{name}: ['{hand[0][0]}', '??'] {hand[0][1]}")
    else:
        print(f"{name}: {str([card[0] for card in hand])} {total}")

def play_game():
    dealer_hand = []
    player_hand = []

    player_hand.append(draw_card())
    player_hand.append(draw_card())
    player_total = calculate_hand(player_hand)

    dealer_hand.append(draw_card())
    dealer_total = calculate_hand(dealer_hand)

    display_hand("Dealer", dealer_hand, dealer_total, hide_second_card=True)
    display_hand("Player", player_hand, player_total)


    if (player_total == 21):
        print("Blackjack! You win!\n")
        return

    while (player_total < 21):
        action = input("Would you like to hit (h) or stand (s)? ").lower()
        if (action == 'h'):
            print("Player hits.\n")
            time.sleep(1)
            player_hand.append(draw_card())
            player_total = calculate_hand(player_hand)
            display_hand("Dealer", dealer_hand, dealer_total, hide_second_card=True)
            display_hand("Player", player_hand, player_total)
            print("")
            time.sleep(1)
            if player_total > 21:
                print("Player busts.\n")
                break
        elif (action == 's'):
            print("Player stands.\n")
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.\n")

    while (dealer_total < 17):
        dealer_hand.append(draw_card())
        dealer_total = calculate_hand(dealer_hand)
        display_hand("Dealer", dealer_hand, dealer_total)
        display_hand("Player", player_hand, player_total)
        print("")
        time.sleep(1)
        if (dealer_total > 21):
            print(f"Dealer busts.")

    if ((dealer_total > 21) or (player_total > dealer_total and player_total <= 21)):
        print("Player wins. Congratulations!\n")
    elif (player_total == dealer_total):
        print("It's a tie.\n")
    else:
        print("Dealer wins.\n")


main()