# ############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


import art
import random
from replit import clear
print(art.logo)

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


# -------- version 1--------
def black_jack():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  player = []
  cp = []
  player_win = True
  cp_win = False
  # pick cards
  if player == []:
    for i in range(2):  
      player.append(random.choice(cards))
      cp.append(random.choice(cards))
  pick_one_more = True
  A_not_in_player = True
  # player = [11, 11]
  while pick_one_more:
    pick_one_more = False
    # Add up
    total_player = sum(player)
    total_cp = sum(cp)
    # Display the result
    print("Player", player, total_player)
  
    # player got 21?
    if total_player == 21:
      print("1p")
      player_win = True
      pick_one_more = False
    elif total_cp == 21:
      print("2c")
      player_win = False
      pick_one_more = False
    
  
  
    # player got > 21 ?
    else:
      # sum point > 21
      if total_player > 21:
        
        # A in cards?
        # A in cards
        
          
        while 11 in player:
          player.remove(11)
          player.append(1)
          total_player = sum(player)
          A_not_in_player = False
          
        if total_player > 21 and A_not_in_player:
          print("3c")
          player_win = False
          pick_one_more = False
             
        # A not in cards
        elif A_not_in_player:
          print("4c")
          player_win = False
          pick_one_more = False
        
      # A in cards + tot < 21 / sum point < 21
      else:
        one_more_card = input("Do you want another card? y/n ")
        # want another card
        if one_more_card == "y":
          player.append(random.choice(cards))
          pick_one_more = True
        # don't want more card
        else:
          pick_one_more = False


        

  if total_player < 21:
    
    if total_cp < 17:
      cp.append(random.choice(cards))
      total_cp = sum(cp)
    
    if total_cp > 21:
      print("5p")
      player_win = True
      
    else:
      
      if total_cp > total_player:
        print(total_player)
        print("6c")
        player_win = False
      elif total_cp == total_player:
        print("7 Draw")
        player_win = False
        cp_win = True
      else:
        if total_player < 21:
          print("8p")
          player_win = True
  elif total_player == 21:
    print("9p")
    player_win = True

  else:
    print("10c")
    player_win = False
        
      
  print("C", cp, total_cp)

  if player_win:
    print("Player Win")
  
  elif cp_win:
    print("Draw")
  
  else:
    print("Player Lose")


          
 
# black_jack()
# pick cards


# --------------------------

# -------- version 2--------

def pick_cards():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# sum up the point in cards
def calculate_point(all_cards):
  
  if all_cards == 21 and len(all_cards) == 2:
    return 0
  if 11 in all_cards and sum(all_cards) > 21:
    all_cards.remove(11)
    all_cards.append(1)    

  return sum(all_cards)

# compare
def compare(player_score,dealer_score):
  if player_score == dealer_score:
    return "DRAW!! 😎 "
  elif player_score == 0:
    return "You got a BlackJack! WIN! 🎉 "
  elif dealer_score == 0:
    return "Dealer win with a BlackJack!🃏"
  elif player_score > 21:
    return "You lose. Too much point😫"
  elif dealer_score >21:
    return"Dealer went too far. You win. 👻"
  elif player_score > dealer_score:
    return "You win! 😊 "
  else:
    return "You Lose. 😤"

# start a game
def play_game():
  print(art.logo)
  player = []
  dealer = []

  # both get cards
  for i in range(2):
    player.append(pick_cards())
    dealer.append(pick_cards())
    game_over = False
  while not game_over:
    player_score = calculate_point(player)
    dealer_score = calculate_point(dealer)
    
    print(f"Player's card: {player} and total point {player_score}")
    print(f"Dealer's first card: {dealer[0]}")
    
    if player_score == 0 or dealer_score == 0 or player_score > 21:
      game_over = True
    else:
      one_more_card = input("Do you want another card? y/n ")
      if one_more_card == 'y':
        player.append(pick_cards())
      else:
        game_over = True
  
  # Dealer's card < 17 keep take card:
  while dealer_score < 17 and dealer_score != 0:
    dealer.append(pick_cards())
    dealer_score = calculate_point(dealer)
  
  
  print(f"Your final card. {player} and score {player_score}")
  print(f"Dealer's final card. {dealer} and score {dealer_score}")
  
  print(compare(player_score,dealer_score))


while input("Wanna play a game? 👾 type 'y' start the game ") == 'y':
  clear()
  play_game()