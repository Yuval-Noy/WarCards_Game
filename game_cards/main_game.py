from game_cards.Player import Player
from game_cards.CardGame import CardGame


p1 = Player(input("Enter Player 1 Name: "))         # Player 1 name
p2 = Player(input("Enter Player 2 Name: "))         # Player 2 name
new_game = CardGame(p1, p2)                         # Set a new game

print("----- Players Information -----")
print(f"""{p1}
{p2}""")
print("------- War Card Game -------")

new_game.new_game()

for i in range(10):                                 # Game of 10 rounds
    p1_card = p1.get_card()                         # Random card from p1 deck
    p2_card = p2.get_card()                         # Random card from p2 deck
    print(f"Player 1 Card: {p1_card}")
    print(f"Player 2 Card: {p2_card}")
    if p1_card > p2_card:                           # p1 Winner of the round
        p1.add_card(p1_card)
        p1.add_card(p2_card)
        print(f"{new_game.p1.name} won this round!")
    else:                                           # p2 Winner of the round
        p2.add_card(p1_card)
        p2.add_card(p2_card)
        print(f"{new_game.p2.name} won this round!")

winner = new_game.get_winner()                      # Match winner
if winner is None:
    print("--- Draw! ---")
elif winner == p1:
    print(f"""------- The Winner is: -------
{p1}""")
else:
    print(f"""------- The Winner is: -------
{p2}""")
