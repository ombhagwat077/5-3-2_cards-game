import random
Suits= ['spades','clubs','diamonds','hearts']
Ranks=['A','K','Q','J','10','9','8','7']
Quota_cards =[5, 3, 2]
def custom_deck():
    deck=[]
    for suit in Suits:
        for rank in Ranks:
            if rank =='7' and suit not in ['hearts','spades']:
                continue
            deck.append((rank, suit))
    return deck

def deal_cards(deck):
    random.shuffle(deck)
    return {
        'Player1': deck[0:10],
        'Player2': deck[10:20],
        'Player3': deck[20:30]
    }

def select_trump(trump_chooser):
    print(f"\n{trump_chooser} will choose the trump suit.")
    while True:
        suit =input(f"{trump_chooser}, enter trump suit (spades / hearts / clubs / diamonds): ").strip().lower()
        if suit in Suits:
            print(f"Trump suit selected: {suit}")
            return suit
        else:
            print("Invalid suit. Try again.")

def display_hand(player_hand):
    return ', '.join([f"{rank} of {suit}" for rank,suit in player_hand])

def trick_winner(trick_cards,trump_suit):
    lead_suit=trick_cards[0][1][1]
    winning_player =trick_cards[0][0]
    winning_card =trick_cards[0][1]
    
    def card_rank(card):
        return Ranks.index(card[0])
    
    for player, card in trick_cards[1:]:
        if card[1]==trump_suit:
            if winning_card[1] !=trump_suit or card_rank(card)<card_rank(winning_card):
                winning_player=player
                winning_card =card
        elif card[1]== lead_suit and winning_card[1]==lead_suit:
            if card_rank(card)<card_rank(winning_card):
                winning_player =player
                winning_card = card
    return winning_player

def pick_roles():
    cards= [5, 3, 2]
    random.shuffle(cards)
    choices={}
    positions ={1: cards[0], 2: cards[1], 3: cards[2]}
    taken_positions = []

    for player in ['Player1','Player2']:
        while True:
            print(f"\n{player}, pick a card position:")
            for pos in [1,2,3]:
                if pos not in taken_positions:
                    print(f"Position {pos}")
            try:
                pos =int(input(f"{player}'s choice: "))
                if pos in [1, 2, 3] and pos not in taken_positions:
                    taken_positions.append(pos)
                    picked =positions[pos]
                    choices[player]=picked
                    print(f"{player} picked: {picked}")
                    break
                else:
                    print("Invalid or already picked position.")
            except:
                print("Invalid input.")

    third_pos =list(set([1, 2, 3]) - set(taken_positions))[0]
    third_player ='Player3'
    choices[third_player]= positions[third_pos]
    print(f"\n{third_player} got the remaining card: {positions[third_pos]}")
    role_map ={}
    for player, quota in choices.items():
        role_map[quota] =player
    trump_chooser =role_map[5]
    dealer =role_map[2]
    quotas ={v: k for k,v in role_map.items()}
    return trump_chooser,dealer,quotas


def play_game():
    trump_chooser, dealer,quotas= pick_roles()
    deck= custom_deck()
    players =deal_cards(deck)
    playersList =['Player1', 'Player2','Player3']
    print("\nWelcome to the 5-3-2 Card Game")
    print(f"Dealer: {dealer}")
    print(f"Trump chooser: {trump_chooser}")
    
    trump_suit =select_trump(trump_chooser)
    tricks_won ={'Player1': 0, 'Player2':0,'Player3':0}
    play_order=['Player1','Player2','Player3']
    print("\nGame Start")
    
    for round_num in range(1, 11):
        print(f"\nTrick {round_num}")
        trick_cards= []
        lead_suit =None
        
        for player in play_order:
            print("\n")
            print(f"{player}'s turn.")
            hand =players[player]
            print("Your hand:",display_hand(hand))
            
            while True:
                user_input=input("Play a card (e.g. A spades): ").strip().split()
                if len(user_input) !=2:
                    print("Invalid format. Use 'Rank Suit' like 'A hearts'or '9 Spades'")
                    continue
                
                rank_input,suit_input=user_input[0].upper(),user_input[1].lower()
                selected_card =(rank_input,suit_input)
                
                if selected_card not in hand:
                    print("You don't have that card. Try again.")
                    continue
                
                if lead_suit:
                    if any(card[1] ==lead_suit for card in hand) and selected_card[1] !=lead_suit:
                        print(f"You must follow the lead suit: {lead_suit}")
                        continue
                hand.remove(selected_card)
                
                trick_cards.append((player,selected_card))
                
                if not lead_suit:
                    lead_suit =selected_card[1]
                break
            
        winner = trick_winner(trick_cards,trump_suit)
        tricks_won[winner] += 1
        print(f"{winner} wins the trick.")
        
    print("\nGame Over")
    print("\nTricks won:")
    
    for player, count in tricks_won.items():
        print(f"{player}: {count}")
    print("\nQuotas:")
    
    for player in playersList:
        print(f"{player}: {quotas[player]}")
    print("\nResult:")
    
    for player in playersList:
        quota = quotas[player]
        if tricks_won[player] >=quota:
            print(f"{player} met their quota")
        else:
            print(f"{player} did not meet their quota (Loser)")

if __name__ =="__main__":
    play_game()
