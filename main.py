

import random
from art import logo
from replit import clear

print(logo)


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
comp_hand = []
user_score = 0
comp_score = 0
game_choice="y"

should_continue = True
gameover = False



def reset_game():
    global should_continue
    global comp_score
    global user_score
    global game_choice
    #if gameover:
    game_choice = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':")
    new_game()

def new_game():
    global should_continue
    global game_choice
    global comp_score
    global user_score
 #   print(f"Game choice is {game_choice}")
    if game_choice == "y":
        should_continue = True
        user_hand.clear()
        comp_hand.clear()
        comp_score = 0
        user_score = 0
        clear()
        print(logo)
        deal_cards("user")
        deal_cards("comp")
        deal_cards("user")
        deal_cards("comp")
        print_deck()
    elif game_choice == "n":
        should_continue = False


def deal_cards(player_hand):
    global user_score
    global comp_score
    if player_hand == "user":
        user_hand.append(random.choice(cards))
        user_score = sum(user_hand)
    else:
        comp_hand.append(random.choice(cards))
        comp_score = sum(comp_hand)


def print_deck():
    global user_score
    print(f" Your cards: {user_hand}, current score: {user_score}")
    if user_score <= 21:
        print(f"Computer's first card: {comp_hand[0]}")
    else:
        print(f"Computer's cards: {comp_hand}, final score: {comp_score}")


def handle_ace():
    global user_score
    global user_hand
    while 11 in user_hand:
        user_hand[user_hand.index(11)] = 1
        user_score = sum(user_hand)


def print_final():
    global user_score
    global comp_score
    print(f"\n Your final hand: {user_hand}, final score: {user_score}")
    print(f" Computer's final hand: {comp_hand}, final score: {comp_score}\n")


def compare():
    global user_score
    global comp_score
   # global gameover
    
    if user_score > 21:
        handle_ace()
    if user_score > 21:
        return("You went over. You lose 😤")
    elif user_score == 21 and len(user_hand)==2:
        return("BLACK JACK!!! You WIN!!! 😊")
    elif comp_score > 21:
        return("Dealer went over. You win 😊")
    elif user_score == 21:
        return(" You WIN!!! 😊")
    elif comp_score==21 and len(comp_hand)==2:
        return("Dealer BlackJack!!! You LOSE 😤 ")
    elif comp_score==21:
        return("You lose 😤")
    elif user_score == comp_score and turn=="n":
        return("It's a draw 😐")
    elif user_score > comp_score and turn=="n":
        return("You win 😊")
    elif user_score < comp_score and turn=="n":
        return("You lose 😤")
    else:
        return("continue")
    

def calculate_score():
    global user_score
    global comp_score
#    global gameover
    if not compare()=="continue":
      print_final()
      print(compare())
      reset_game()
      

new_game()
#print_deck()


while should_continue:
    turn = input("Type 'y' to get another card, type 'n' to pass: \n")
    if turn == "y":
        deal_cards("user")
#        calculate_score()
        if not compare()=="continue":
          print_final()
          print(compare())
          reset_game()
        else:
          print_deck()
    elif turn == "n":
        while comp_score < 17:
            deal_cards("comp")
        print_final()
        print(compare())
        reset_game()
        
             
       

