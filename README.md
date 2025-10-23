.

📁 Project Structure
wifey_rps_app/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # List of Python packages needed
├── leaderboard.csv        # Stores leaderboard scores (auto-created if missing)
├── README.md              # Project description & instructions
└── assets/                # Optional folder for images or extra Lottie files

📌 File Descriptions
1. app.py

Core Streamlit code.

Features included:

Player name & avatar selection

Tie-safe best-of-5 rounds

Scoreboard & round history

Win streak tracking

Lucky/double-point rounds

Confetti animations for wins

Lottie animations (or emoji fallback) for moves

Interactive buttons for moves

Game over logic & restart button

Persistent leaderboard (reads/writes leaderboard.csv)

2. requirements.txt

Lists all Python packages for deployment.

streamlit
streamlit-lottie
pandas
requests

3. leaderboard.csv

Keeps track of top scores across sessions.

Columns:

Player,Score,Max Streak


Auto-created if missing.

4. README.md

Explains the project:

Project overview

How to run locally

How to deploy on Streamlit Cloud

Features list (interactive gameplay, leaderboard, animations, etc.)

5. assets/ (Optional)

Store custom images or Lottie JSON files if needed.

Could include:

Extra avatars

Background animations

Sound effects (if added later)

📌 Key Features Overview
Feature	Description
Player Name & Avatar	Personalization
Tie-Safe Rounds	Ties don’t count toward the 5 rounds
Scoreboard & Round History	Tracks scores & moves
Win Streak Tracking	Shows current streak
Lucky / Double-Point Rounds	Randomly triggered extra points
Confetti Animation	Visual reward for wins
Lottie Animations or Emoji Fallback	For player & CPU moves
Interactive Buttons	Clickable emoji-based moves
Restart Button	Resets game
Persistent Leaderboard	Tracks top players across sessions
