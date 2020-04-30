#!/usr/bin/python3
import os
import random

def add_cards(deck, amount):
    hand = []
    for i in range(amount):
        random.shuffle(deck)
        card = deck.pop()

        if card == 11:
            card = 'J'
        if card == 12:
            card = 'K'
        if card == 13:
            card = 'Q'
        if card == 14:
            card = 'A'

        hand.append(card)
    return hand

def total(hand):
    points = 0
    for card in hand:
        if card in {'J', 'K', 'Q'}:
            points += 11
        elif card == 'A':
            if points >= 11:
                points += 1
            else:
                points += 11
        else: points += int(card)
    return points

def the_end(player, dealer):
    if total(dealer) >= 21 < total(player):
        print("\nDealer overshot ({} points)! Player won.".format(total(dealer)))
        return True
    elif total(dealer) <= 21 < total(player):
        print("\nPlayer overshot ({} points)! Dealer won.".format(total(player)))
        return True
    elif total(player) == 21:
        print("\nPlayer got a blackjack!")
        return True
    elif total(dealer) == 21:
        print("\nDealer got a blackjack!")
        return True
    elif total(player) > 21 > total(dealer):
        print("\nDraw! Both overshot!")
        return True
    elif len(player) >= 5 or len(dealer) >= 5:
        if total(dealer) > total(player) and total(dealer) <= 21:
            print("\nDealer won!")
            return True
        elif total(player) > total(dealer) and total(player) <= 21:
            print("\nPlayer won!")
            return True
        else:
            print("\nDraw! Both overshot!")
            return True

def restart():
    inp = input("Play again? [Y]es or [n]o: ").lower()
    if inp == "y":
        main()
    elif inp == "n":
        os._exit(0)

def main():
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

    player_hand = add_cards(deck, 2)
    dealer_hand = add_cards(deck, 2)

    inp = ""

    while True:
        os.system('clear')

        if the_end(player_hand, dealer_hand):
            restart()

        print("\nDealer: {} ({})".format(dealer_hand, total(dealer_hand)))
        print("Player: {} ({})".format(player_hand, total(player_hand)))

        if total(dealer_hand) <= 21:
            if total(player_hand) < 19 < total(dealer_hand) and len(dealer_hand) <= 4:
                continue
            dealer_hand += add_cards(deck, 1)

        inp = input("\n(h)it, (s)tand or (q)uit: ").lower()
        if inp == "h":
            player_hand += add_cards(deck, 1)
        elif inp == "s":
            continue
        elif inp == "q":
            break

main()
