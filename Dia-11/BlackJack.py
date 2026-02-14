import art
import random

def soma(hand):
    total = 0
    for carta in hand:
        total += carta

    while total > 21 and 11 in hand:
        posicao = hand.index(11)
        hand[posicao] = 1
        total -= 10

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
    print(f"Your hand: {player_hand}, current score: {player_score}")

    computer_score = soma(computer_hand)
    print(f" Computer's first card: {computer_hand[1]}")

    another_card = input("Type 'y' to get another card or type 'n' to pass: ").lower()
    while another_card == 'y':
        player_hand.append(deck.pop())
        player_score = soma(player_hand)
        print(f"Your hand: {player_hand}, score: {player_score}")

        if computer_score < 17:
            computer_hand.append(deck.pop())
            computer_score = soma(computer_hand)
            if computer_score > 21:
                print(f"Computer's hand: {computer_hand}, score: {computer_score}")
                print("You Win!")
                return

        if player_score > 21:
            print(f"Computer's hand: {computer_hand}, score: {computer_score}")
            print("You Lose!")
            return
        elif player_score > computer_score:
            print(f"Your hand: {player_hand}, score: {player_score}")
            print(f"Computer's hand: {computer_hand}, score: {computer_score}")
            print("You Win!")
            return
        else:
            print(f"Your hand: {player_hand}, score: {player_score}")
            print(f"Computer's hand: {computer_hand}, score: {computer_score}")
            print("You Lose!")
            return


    while computer_score < 17:
        computer_hand.append(deck.pop())
        computer_score = soma(computer_hand)
        if computer_score > 21:
            print(f"Computer's hand: {computer_hand}, score: {computer_score}")
            print("You Win!")
            return
    if player_score > computer_score:
        print(f"Your hand: {player_hand}, score: {player_score}")
        print(f"Computer's hand: {computer_hand}, score: {computer_score}")
        print("You Win!")
        return
    else:
        print(f"Your hand: {player_hand}, score: {player_score}")
        print(f"Computer's hand: {computer_hand}, score: {computer_score}")
        print("You Lose!")
        return

print(art.logo)

play = input("Do you want to play a game of BlackJack? Typer 'y' or 'n': ").lower()
if play == 'y':
    play = True

while play:
    print(art.logo)

    blackjack()
    play = input("Do you want to play a game of BlackJack? Typer 'y' or 'n': ").lower()
    if play == 'n':
        play = False
