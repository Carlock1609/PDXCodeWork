#! python3

#v1

# Try a dictionary
def get_player_hand():
    deck = {"A": 1,
        "2": 2,
        "3": 3, 
        "4": 4, 
        "5": 5, 
        "6": 6, 
        "7": 7, 
        "8": 8, 
        "9": 9, 
        "10": 10, 
        "J": 10, 
        "Q": 10, 
        "K": 10}
    player_hand = []

    for i in range(3):
        get_card = deck[input("Please enter in 3 cards to be added to your hand: (A,1,2,3,4,5,6,7,8,9,10,J,Q,K").upper()]
        player_hand.append(get_card)
        if i == 1 and sum(player_hand) < 11:
            player_hand.append(11)
    return player_hand

def get_hand_worth(player_hand):
    total_hand = player_hand[0] + player_hand[1] + player_hand[2]
    return total_hand

def main():
    play_again = True

    while play_again:
        play_again = input("Do you want blackjack advice?: (Yes or No?)").lower()     
        if play_again != "yes":
            print("Goodbye!")
            play_again = False
        else:
            get_hand = get_hand_worth(get_player_hand())
            if get_hand == 21:
                print("Blackjack!")
            elif get_hand >= 18:
                print("Stay!")
            else:
                print("Hit!")

            if play_again != "yes":
                play_again = False
                     
main()