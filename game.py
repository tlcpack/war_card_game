import random,time

all_cards_dict = { 
    'H2': 2, 
    'H3': 3, 
    'H4': 4, 
    'H5': 5, 
    'H6': 6, 
    'H7': 7, 
    'H8': 8, 
    'H9': 9, 
    'H10': 10, 
    'HJ': 11, 
    'HQ': 12, 
    'HK': 13, 
    'HA': 14,
    'C2': 2, 
    'C3': 3, 
    'C4': 4, 
    'C5': 5, 
    'C6': 6, 
    'C7': 7, 
    'C8': 8, 
    'C9': 9, 
    'C10': 10, 
    'CJ': 11, 
    'CQ': 12, 
    'CK': 13, 
    'CA': 14,
    'D2': 2, 
    'D3': 3, 
    'D4': 4, 
    'D5': 5, 
    'D6': 6, 
    'D7': 7, 
    'D8': 8, 
    'D9': 9, 
    'D10': 10, 
    'DJ': 11, 
    'DQ': 12, 
    'DK': 13, 
    'DA': 14, 
    'S2': 2, 
    'S3': 3, 
    'S4': 4, 
    'S5': 5, 
    'S6': 6, 
    'S7': 7, 
    'S8': 8, 
    'S9': 9, 
    'S10': 10, 
    'SJ': 11, 
    'SQ': 12, 
    'SK': 13, 
    'SA': 14 
    }

all_cards_list = list(all_cards_dict.keys())
random.shuffle(all_cards_list)

player_deck = all_cards_list[0:26]
opp_deck = all_cards_list[26:52]

# print(all_cards_dict.get(player_deck[0]))
# print(all_cards_dict.get(opp_deck[0]))
# if all_cards_dict.get(player_deck[0]) > all_cards_dict.get(opp_deck[0]):
#     print("Win")
# else:
#     print("lose")

def game(player, opponent):

    if all_cards_dict.get(player[0]) > all_cards_dict.get(opponent[0]):
        print("P: " + str(player[0]) + ", O: " + str(opponent[0]))
        print("Win")
        player.append(opponent[0])
        opponent.pop(0)
    else:
        print("P: " + str(player[0]) + ", O: " + str(opponent[0]))
        print("Lose")
        opponent.append(player[0])
        player.pop(0)

num_player_cards = len(player_deck)
num_opp_cards = len(opp_deck)
    
print("Welcome to war!")
time.sleep(2)
print(f"Player has {num_player_cards}. Opponent has {num_opp_cards}")
time.sleep(2)
print("Press enter when ready to draw")
input()
game(player_deck, opp_deck)
    