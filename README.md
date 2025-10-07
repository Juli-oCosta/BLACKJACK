[Read this in Portuguese / Leia isto em Português](README-pt-br.md)

# 🃏 Blackjack (21) Game in Python
... (resto do conteúdo em inglês)

# 🃏 Blackjack (21) Game in Python

This project is a complete implementation of the classic card game Blackjack (21), developed in pure Python. The game runs entirely in the command line and was built with a focus on clean code, modularity, and the correct application of the game's rules.

## ✨ Features

* **Complete Game Logic:** Implements the essential rules of Blackjack, including:
    * Player's turn with "Hit" and "Stand" options.
    * Automated dealer's turn, who must hit until their score reaches 17.
    * Detection of "Bust" (score over 21).
* **Realistic Deck Simulation:** The program creates a finite 52-card deck that is shuffled at the start of each game. Dealt cards are removed from the deck, making the game more realistic.
* **Smart Ace Calculation:** The hand's score is dynamically calculated, treating an Ace as 11 or 1 to always provide the best possible score without busting.
* **Clear Terminal Interface:** The game presents information in an organized manner, displaying the player's and dealer's hands and scores at each step.

## 🚀 How to Run

1.  **Prerequisites:** Ensure you have Python 3.x installed on your machine.
2.  **Download:** Download or clone this repository.
3.  **Execution:** Navigate to the project folder in your terminal and run the following command:
    ```bash
    python main.py
    ```
4.  **Play:** Follow the on-screen prompts to play the game.

## 🧠 Programming Concepts Applied

This project served as a practical exercise to solidify several important software concepts:

* **Modularity with Functions:** The code is organized into functions with single responsibilities, following the **Single Responsibility Principle (SRP)**. There are dedicated functions to create the deck, deal cards, calculate scores, manage each player's turn, and determine the winner.
* **Data Structures:** Utilizes a **list of dictionaries** to represent the deck, where each card is an object with properties (`rank`, `suit`, `value`). This approach makes data access explicit and the code more readable.
* **State Management:** The `deck`, `player_hand`, and `dealer_hand` variables are managed and passed between functions, controlling the game's state throughout each round.
* **Conditional Logic:** Intensive use of `if/elif/else` structures and `while` loops to control the game flow and apply the complex rules of Blackjack.

## 🔮 Future Improvements

This project has a solid foundation that allows for several interesting expansions, such as:

* Implementing a betting system with a fictional balance for the player.
* Adding a main loop to allow the user to play multiple games in a row.
* Allowing the option to play with a multi-deck shoe.
* Improving the user experience with pauses (`time.sleep`) and screen clearing (`os.system`).
