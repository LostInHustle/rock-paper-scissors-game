Hello, welcome to my project named `rock-paper-scissors-game`. This is a game where players can play classic rock-paper-scissors against the computer. The game includes user interface for login and playing the game, all built using PyQt6.

**Installation and Running:**

1. **Clone the Repository:**
   ```
   git clone https://github.com/LostInHustle/rock-paper-scissors-game
   ```

2. **Change Directory:**
   ``` 
   cd rock-paper-scissors-game
   ```

3. **Run the Game:**
   ```
   python -u main.py
   ```

**Features:**
- **Login Interface:** Users must login with a username and password before playing. Currently, any non-empty username and password will work to proceed to the game.
- **Gameplay:** 
  - Choose between 'R' for Rock, 'P' for Paper, 'S' for Scissors.
  - The computer makes a random choice.
  - Results are displayed in a message box.

**File Structure:**

- **main.py:** Starts the application, sets up the login UI and transitions to the game UI.
- **rps_login_ui.py:** Contains the login interface where users enter their details.
- **rps_game_ui.py:** The main game interface where players interact to play rock-paper-scissors.

**How to Play:**

1. **Start Game:** Launch the game by running `main.py`.
2. **Login:** Enter any username and password in the login screen.
3. **Choose Your Move:** Enter 'R', 'P', or 'S' in the game interface.
4. **See Results:** Click on 'Check Result' to see who won the round.
5. **Replay or Quit:** Options to play again or go back to the login screen.

**Issues or Contributions:**

- Feel free to open an issue if you find bugs or want to suggest enhancements.
- Pull requests are welcome, especially for adding features or fixing bugs.