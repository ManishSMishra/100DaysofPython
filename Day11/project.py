# BlackJack Game
import random




user_hand=[]
dealer_hand=[]
face_value=[11,2,3,4,5,6,7,8,9,10]
def deal(player):
    player.append(random.choice(face_value))
    if sum(player) >21 and 11 in player:
        player.remove(11)
        player.append(1)


    
def check_winner(user_hand,dealer_hand):
    while sum(dealer_hand)<17:
        deal(dealer_hand)
    if sum(user_hand) > sum(dealer_hand) and sum(user_hand) <=21:
        print("You won")
        print(f"Your hand {user_hand}")
        print(f"Dealer hand {dealer_hand}")
    elif sum(user_hand) < sum(dealer_hand) and sum(dealer_hand) <=21:
        print("You Lost")
        print(f"Your hand {user_hand}")
        print(f"Dealer hand {dealer_hand}")
    else:
        print("It's a Draw!")
        print(f"Your hand {user_hand}")
        print(f"Dealer hand {dealer_hand}")
    



def main():
    for i in range(0,2):
        deal(user_hand)
        deal(dealer_hand)
    print(f"Player Hand: {user_hand}\n Dealer Hand: {dealer_hand[0]}")
    isPlay=True
    while sum(user_hand) < 21 and isPlay:
        choice=input("Do you want to draw: 'y' or 'n': ").lower()
        if choice=='y':
            deal(user_hand)
            print(user_hand)
        else:
            isPlay=False
    check_winner(user_hand,dealer_hand)


main()
