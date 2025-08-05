# 🔼 Higher Lower Game (Python)

A fun and addictive **command-line game** inspired by the popular *Higher Lower* format. In this game, you're shown two celebrities and must guess who has more **Instagram followers**. With each correct guess, your score increases — but one wrong answer, and it's game over!

---

## 🧠 Game Concept

- You're shown **two celebrities** (A and B), along with their professions and countries.
- You must guess who has **more Instagram followers** by typing `'A'` or `'B'`.
- Get it right? Your score increases and the game continues.
- Get it wrong? Game over — your final score is displayed.

---

## 🖼️ ASCII Art Logo

<pre>
  _   _ ___ ____ _   _ _____ ____  
 | | | |_ _/ ___| | | | ____|  _ \ 
 | |_| || | |  _| |_| |  _| | |_) |
 |  _  || | |_| |  _  | |___|  _ < 
 |_| |_|___\____|_| |_|_____|_| \_\ 
  _     _____        _______ ____  
 | |   / _ \ \      / / ____|  _ \ 
 | |  | | | \ \ /\ / /|  _| | |_) |
 | |__| |_| |\ V  V / | |___|  _ < 
 |_____\___/  \_/\_/  |_____|_| \_\ 

 </pre>



---

## 🎯 Features

| Feature             | Description |
|---------------------|-------------|
| 🧑‍🤝‍🧑 Celebrity Dataset | Predefined list of 30+ celebrities with follower counts |
| 🔁 Infinite Rounds  | Keep playing as long as you guess correctly |
| ⬆️ Higher or Lower  | Guess based on your knowledge or intuition |
| 🧾 Score Tracking   | Shows your current and final score |
| 🎮 CLI Based        | Fully playable from the command line |

---

## 🛠️ How to Run

### ✅ Requirements

- Python 3.x installed
- No external libraries needed

### 🚀 Steps to Play

# Clone the repository
git clone https://github.com/sairahul777/higher-lower-game-python.git
cd higher-lower-game-python

# Run the game
python higher_lower_game.py

---

👨‍💻 Sample Gameplay


<pre>

  _   _ ___ ____ _   _ _____ ____  
 | | | |_ _/ ___| | | | ____|  _ \ 
 | |_| || | |  _| |_| |  _| | |_) |
 |  _  || | |_| |  _  | |___|  _ < 
 |_| |_|___\____|_| |_|_____|_| \_\ 
  _     _____        _______ ____  
 | |   / _ \ \      / / ____|  _ \ 
 | |  | | | \ \ /\ / /|  _| | |_) |
 | |__| |_| |\ V  V / | |___|  _ < 
 |_____\___/  \_/\_/  |_____|_| \_\ 
 
current score is: 0
Drake is a Rapper and singer and from Canada
              
 __   _____   
 \ \ / / __|  
  \ V /\__ \_ 
   \_/ |___(_)
              

Khloé Kardashian is a Reality TV star and from United States
who has more followers. type 'A' or 'B': b




current score is: 1
Chris Hemsworth is a Actor and from Australia
              
 __   _____   
 \ \ / / __|  
  \ V /\__ \_ 
   \_/ |___(_)
              

Virat Kohli is a Cricketer and from India
who has more followers. type 'A' or 'B': a
you guessed it wrong.
your final score is: 1
Better luck next time!👍

  
</pre>

---

🧱 Project Structure

📂 higher-lower-game-python
├── higher_lower_game.py   # Main game logic
└── README.md              # Game documentation


---

🎓 Learning Outcomes

- This project is great for learning:

- Python fundamentals

- Dictionaries & data structures

- random module

- Conditional logic

- Loops & user input

- Basic CLI design

---


🌟 Future Improvements

- Add categories: sports, entertainment, music

- Add follower ranges instead of exact counts

- Introduce a GUI using Tkinter or PyGame

- Add score leaderboard using local storage

