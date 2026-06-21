# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.
- [X] Detail which bugs you found.
- [X] Explain what fixes you applied.

## 📸 Demo Walkthrough

Follow these numbered steps to see the fixed game in action:

1. **Launch the app.** Run `python -m streamlit run app.py` and open the page in your browser.
2. **Pick a difficulty.** Use the sidebar to choose Easy, Normal, or Hard. The "Range" and "Attempts allowed" captions update to match: Easy is 1–20 with 5 attempts, Normal is 1–50 with 6 attempts, and Hard is 1–100 with 8 attempts.
3. **Make a guess.** Enter a number and click **Submit**. The secret number stays the same across submissions instead of changing every click, and only valid numeric guesses use up an attempt.
4. **Follow the hints.** When your guess is too high the game now correctly tells you to "Go LOWER," and when it's too low it tells you to "Go HIGHER." Use the hints to narrow in on the secret.
5. **Watch your score.** A win awards points that scale with how few attempts you used (full 100 on a first-try win, down to a floor of 10), and wrong guesses cost points but never push the score below 0.
6. **Win or run out of attempts.** When you guess correctly you win; "Attempts left" counts down accurately as you play.
7. **Start over.** Click **New Game** to get a fresh secret within the current difficulty's range and a reset round — fully playable again even after a previous win or loss.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
