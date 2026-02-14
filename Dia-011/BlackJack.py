import art
import random

def soma(hand):
    total = sum(hand)

    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        total = sum(hand)
    return total

def start_deck():
    cartas_base = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4
    figuras = [10] * 12

    deck = cartas_base + figuras
    random.shuffle(deck)
    return deck

def card_distribution(deck):
    p_hand = []
    c_hand = []

    for carta in range(2):
        p_hand.append(deck.pop())
        c_hand.append(deck.pop())
    return p_hand, c_hand


def blackjack():
    deck = start_deck()
    player_hand, computer_hand = card_distribution(deck)
    player_score = soma(player_hand)
    computer_score = soma(computer_hand)

    if player_score == 21 or computer_score == 21:
        print(f"Your final hand: {player_hand}, score: {player_score}")
        print(f"Computer's final hand: {computer_hand}, score: {computer_score}")
        if player_score == 21 and computer_score == 21:
            print("Draw! Both have Blackjack!")
        elif player_score == 21:
            print("BLACKJACK! You won!")
        else:
            print("Blackjack! You lose!")
        return
    game_over = False
    while not game_over:
        print(f"Your hand: {player_hand}, score atual: {player_score}")
        print(f"Computer first card: {computer_hand[0]}")

        user_choice = input("Type 'y' for another card or 'n' to pass: ").lower()

        if user_choice == 'y':
            player_hand.append(deck.pop())
            player_score = soma(player_hand)

            if player_score >= 21:
                game_over = True
        else:
            game_over = True
    if player_score <= 21:
        while computer_score < 17:
            computer_hand.append(deck.pop())
            computer_score = soma(computer_hand)

    print(f"Your final hand: {player_hand}, score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, score: {computer_score}")

    if player_score > 21:
        print("You Lose! (Busted)")
    elif computer_score > 21:
        print("You Win! Computer busted!")
    elif player_score > computer_score:
        print("You Win!")
    elif player_score < computer_score:
        print("You Lose!")
    else:
        print("Draw!")
print(art.logo)

while input("Do you want to play BlackJack? Type 'y' or 'n': ").lower() == 'y':

    blackjack()
    input("\nPressione ENTER para continuar...")
    print("\n"*30)
    print(art.logo)
