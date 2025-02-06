import random  
import matplotlib.pyplot as plt  

# Initialize the deck  
suits = ['spade', 'heart', 'diamond', 'club']  
values = list(range(1, 11)) + [10, 10, 10] 
deck = [{'value': value, 'suit': suit} for suit in suits for value in values]  
  
# Game statistics  
game_stats = {'banker_wins': 0, 'player_wins': 0, 'draws': 0}  

def shuffle_deck(deck):  
    random.shuffle(deck)  
    return deck

def update_statistics(winner, game_stats):  
    if winner == 'Banker':  
        game_stats['banker_wins'] += 1  
    elif winner == 'Player':  
        game_stats['player_wins'] += 1  
    else:  
        game_stats['draws'] += 1  

def show_statistics(game_stats):  
    labels = list(game_stats.keys())  
    values = list(game_stats.values())  
    
    fig = plt.figure(figsize = (10, 5)) 

    plt.bar(labels, values, color=['grey', 'green', 'orange'])  
    plt.xlabel('Result Outcome')  
    plt.ylabel('Number of Wins')  
    plt.title('Game Statistics')  
    plt.show()  

def calculate_sum(hand):  
    total_value = sum(card['value'] for card in hand)  
    if total_value > 9:  
        total_value = total_value % 10  
    return total_value

def determine_winner(banker, player):  
    banker_value = calculate_sum(banker)  
    player_value = calculate_sum(player)  
      
    if player_value > banker_value:  
        return 'Player'  
    elif banker_value > player_value:  
        return 'Banker'  
    else:  
        return 'Draw'  

def deal_cards(deck):  
    if len(deck) < 4:  
        raise Exception("Cards insufficient. Please reshuffle.")  
      
    banker = [deck.pop(), deck.pop()]  
    player = [deck.pop(), deck.pop()]  
      
    return banker, player  

def main():  
    global deck, game_stats  

    deck = shuffle_deck(deck)  
      
    while True:  
        action = input("Enter 'play' to start the game or 'shuffle' to reshuffle the deck or press 'exit' to quit: ").strip().lower()  
          
        if action == 'play':  
            try:  
                banker_value, player_value = deal_cards(deck)  
                winner = determine_winner(banker_value, player_value)  
                update_statistics(winner, game_stats)  
                  
                print(f"Banker value: {banker_value}, Player value: {player_value}")  
                print(f"Winner: {winner}")  
                  
                show_statistics(game_stats)  
            except Exception as e:  
                print(e)  
          
        elif action == 'shuffle':  
            deck = shuffle_deck(deck)  
            print("Deck reshuffled.")  
        
        elif action == 'exit':
            print("Quitting the game...")
            break 

        else:  
            print("Invalid action. Please enter 'play' or 'shuffle'.")
  
if __name__ == "__main__":  
    main()  