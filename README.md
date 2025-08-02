# 5-3-2 Card Game (CLI Version)

A command-line Python implementation of the classic 3-player card game 5-3-2 (also known as 3-2-5 or Teen-Do-Panch), commonly played in India and Nepal.

## Objective

To simulate the 5-3-2 card game logic via a CLI-based Python program where:
- 3 players participate
- A 30-card custom deck is used
- Roles (Dealer, Trump Chooser, Other) are assigned via picking cards (5, 3, 2)
- Trump is chosen by the player who picks 5
- The game proceeds for 10 tricks and evaluates who met their quotas

## How to Play

1. On running the game, players are prompted to choose cards from positions 1–3 (hidden 5, 3, 2).
2. The player who picks:
   - **5** becomes the **Trump Chooser** and must win **5 tricks**
   - **3** becomes the **Other Player** and must win **3 tricks**
   - **2** becomes the **Dealer** and must win **2 tricks**
3. The Trump Chooser selects the trump suit (`spades`, `hearts`, etc.).
4. Cards are dealt randomly (10 each).
5. The **Trump Chooser starts the first trick**, followed by the other player and the dealer (counter-clockwise).
6. For each trick:
   - Players must follow the lead suit if they can.
   - If a trump is played, the highest trump wins.
   - If no trump is played, the highest card of the lead suit wins.
7. After 10 tricks, the game prints:
   - Tricks won by each player
   - Whether they met their required quota

## How to Run

1. Open Terminal ( Command Prompt) and go to path.
2. Make sure Python 3 is installed.
3. Run the game with:

python 5_3_2_cardgame.py
