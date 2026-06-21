#FIX: Moved get_range_for_difficulty to logic_utils.py with claude
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    # FIX: Swapped Normal/Hard ranges so difficulty scales sensibly
    # (Normal 1-50, Hard 1-100) - fixed by Claude
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

#FIX: Moved check_guess to logic_utils.py and refactored the code to update lowhigh logic and remove confusing error logic using Claude
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        # Guess is too high, so the player should aim lower.
        return "Too High", "📉 Go LOWER!"
    # Guess is too low, so the player should aim higher.
    return "Too Low", "📈 Go HIGHER!"


#FIX: Implemented update_score in logic_utils, clamped score at 0 so it can't go negative, removed the arbitrary Too High parity bonus, and fixed the win formula so fast wins pay full points - fixed by Claude
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        # Full 100 for a first-attempt win, -10 per extra attempt, floored at 10.
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    # Any wrong guess costs 5 points, but the score never drops below 0.
    if outcome in ("Too High", "Too Low"):
        return max(0, current_score - 5)

    return current_score
