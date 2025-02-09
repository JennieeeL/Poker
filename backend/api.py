from flask import Flask, jsonify
import random

app = Flask(__name__)

# Initialize the deck and game stats
suits = ['spade', 'heart', 'diamond', 'club']
values = list(range(1, 11)) + [10, 10, 10]
deck = [{'value': value, 'suit': suit} for suit in suits for value in values]

game_stats = {'banker_wins': 0, 'player_wins': 0, 'draws': 0}

# Shuffle the deck
def shuffle_deck():
    random.shuffle(deck)

# Calculate the hand value
def calculate_sum(hand):
    total_value = sum(card['value'] for card in hand)
    if total_value > 9:
        total_value = total_value % 10
    return total_value

# Determine the winner
def determine_winner(banker, player):
    banker_value = calculate_sum(banker)
    player_value = calculate_sum(player)
    if player_value > banker_value:
        return 'Player'
    elif banker_value > player_value:
        return 'Banker'
    else:
        return 'Draw'

# Deal cards
def deal_cards():
    if len(deck) < 4:
        raise Exception("Cards insufficient. Please reshuffle.")
    banker = [deck.pop(), deck.pop()]
    player = [deck.pop(), deck.pop()]
    return banker, player

@app.route('/play', methods=['POST'])
def play_game():
    try:
        banker, player = deal_cards()
        winner = determine_winner(banker, player)

        # Update statistics
        if winner == 'Banker':
            game_stats['banker_wins'] += 1
        elif winner == 'Player':
            game_stats['player_wins'] += 1
        else:
            game_stats['draws'] += 1

        # Return game results
        return jsonify({
            'success': True,
            'banker_value': calculate_sum(banker),
            'player_value': calculate_sum(player),
            'winner': winner
        })

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/shuffle', methods=['POST'])
def shuffle():
    shuffle_deck()
    return jsonify({'message': "Deck shuffled successfully."})

@app.route('/stats', methods=['GET'])
def stats():
    return jsonify(game_stats)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
