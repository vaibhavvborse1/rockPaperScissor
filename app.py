import streamlit as st
import random
import time
import requests
from streamlit_lottie import st_lottie


from streamlit_lottie import st_lottie
import requests

def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---------------------
# Load Lottie safely
# ---------------------
def load_lottie(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None


ANIMATIONS = {
    "✊": "https://assets6.lottiefiles.com/packages/lf20_touohxv0.json",
    "✋": "https://assets6.lottiefiles.com/packages/lf20_u4yrau.json",
    "✌️": "https://assets6.lottiefiles.com/packages/lf20_1egfck.json"
}

# ---------------------
# Session State
# ---------------------
if "player_score" not in st.session_state: st.session_state.player_score = 0
if "computer_score" not in st.session_state: st.session_state.computer_score = 0
if "round" not in st.session_state: st.session_state.round = 1
if "history" not in st.session_state: st.session_state.history = []
if "streak" not in st.session_state: st.session_state.streak = 0

# ---------------------
# Player Personalization
# ---------------------
st.title("🎮 Rock Paper Scissors - App Style")
player_name = st.text_input("Enter your name:", "player")
avatar_options = ["👩‍💻", "🧑‍🚀", "🦸", "👸", "💃", "🧝‍♀️"]
player_avatar = st.selectbox("Choose your avatar:", avatar_options)

# ---------------------
# Game Container (App Style)
# ---------------------
st.markdown("""
<style>
.game-card {
    background-color: #f0f2f6;
    border-radius: 100px;
    padding: 1px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.2);
    margin-bottom: 20px;
}
.center { display: flex; justify-content: center; align-items: center; flex-direction: column; }
.move-button { font-size: 36px; padding: 10px 25px; margin: 5px; border-radius: 15px; background-color: #e0e7ff; border: none; cursor: pointer; }
.move-button:hover { background-color: #c7d2fe; }
</style>
""", unsafe_allow_html=True)

# ---------------------
# Round Info
# ---------------------
with st.container():
    st.markdown('<div class="game-card center">', unsafe_allow_html=True)
    st.subheader(f"Round: {st.session_state.round}/5")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------
# Player Move Selection
# ---------------------
with st.container():
    st.markdown('<div class="game-card center">', unsafe_allow_html=True)
    st.subheader("Choose Your Move")
    col1, col2, col3 = st.columns(3)
    player_choice = None
    if col1.button("✊", key="rock"): player_choice = "✊"
    if col2.button("✋", key="paper"): player_choice = "✋"
    if col3.button("✌️", key="scissors"): player_choice = "✌️"
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------
# Play Game Logic
# ---------------------
if player_choice:
    computer_choice = random.choice(["✊", "✋", "✌️"])

    # Countdown animation
    placeholder = st.empty()
    for c in ["Rock...", "Paper...", "Scissors...", "Shoot!"]:
        placeholder.text(c)
        time.sleep(0.5)

    st.write(f"{player_avatar} {player_name} chose: {player_choice}")
    st.write(f"CPU chose: {computer_choice}")

    # Show animations
    player_anim = load_lottie(ANIMATIONS[player_choice])
    cpu_anim = load_lottie(ANIMATIONS[computer_choice])

    if player_anim:
        st_lottie(player_anim, height=150, key=f"player{st.session_state.round}")
    else:
        st.write(f"{player_avatar} played: {player_choice}")

    if cpu_anim:
        st_lottie(cpu_anim, height=150, key=f"cpu{st.session_state.round}")
    else:
        st.write(f"CPU played: {computer_choice}")

    # Lucky Round 10% chance
    lucky_round = random.random() < 0.1
    bonus_msg = " ⚡ Lucky Round! Double points!" if lucky_round else ""

    # Determine winner
    if player_choice == computer_choice:
        result = "🤝 It's a tie! This round doesn't count, play again."
        st.session_state.streak = 0
    elif (player_choice == "✊" and computer_choice == "✌️") or \
            (player_choice == "✋" and computer_choice == "✊") or \
            (player_choice == "✌️" and computer_choice == "✋"):
        points = 2 if lucky_round else 1
        result = f"🎉 {player_name} wins this round!{bonus_msg}"
        st.session_state.player_score += points
        st.session_state.round += 1
        st.session_state.streak += 1
        st.balloons()
    else:
        points = 2 if lucky_round else 1
        result = f"💀 {player_name} loses this round!{bonus_msg}"
        st.session_state.computer_score += points
        st.session_state.round += 1
        st.session_state.streak = 0

    st.write(result)
    st.session_state.history.append(
        f"Round {st.session_state.round - 1 if 'tie' not in result else st.session_state.round}: {player_avatar} {player_choice} vs CPU {computer_choice} → {result}"
    )

# ---------------------
# Scoreboard & History
# ---------------------
with st.container():
    st.markdown('<div class="game-card center">', unsafe_allow_html=True)
    st.subheader("Scoreboard")
    st.write(f"{player_name}: {st.session_state.player_score} | CPU: {st.session_state.computer_score}")
    st.write(f"Current Win Streak: {st.session_state.streak}")
    st.markdown("</div>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="game-card center">', unsafe_allow_html=True)
    st.subheader("Round History")
    for h in st.session_state.history:
        st.write(h)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------
# Game Over & Restart
# ---------------------
if st.session_state.round > 5:
    st.write("🏆 **Game Over!**")
    if st.session_state.player_score > st.session_state.computer_score:
        st.success(f"🎉 {player_name} wins the game!")
    elif st.session_state.player_score < st.session_state.computer_score:
        st.error(f"💀 {player_name} lost the game!")
    else:
        st.info("🤝 It's a tie game!")

    if st.button("Restart Game"):
        st.session_state.player_score = 0
        st.session_state.computer_score = 0
        st.session_state.round = 1
        st.session_state.history = []
        st.session_state.streak = 0

