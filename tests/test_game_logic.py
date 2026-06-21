import random

from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- tests for the high/low hint bug ---
# The old check_guess paired "Too High" with "📈 Go HIGHER!" and "Too Low" with
# "📉 Go LOWER!", so the hint always pointed the player in the wrong direction.

def test_too_high_hint_tells_player_to_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_hint_tells_player_to_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message


# --- tests for the scoring bug ---
# The old update_score subtracted 5 for every wrong guess with no lower bound,
# gave an arbitrary +5 bonus for "Too High" on even attempts, and the win
# formula used (attempt_number + 1), underpaying fast wins.

def test_score_never_goes_negative_on_repeated_wrong_guesses():
    # Starting from 0, many wrong guesses must clamp at 0, not go negative.
    score = 0
    for attempt in range(1, 11):
        score = update_score(score, "Too Low", attempt)
        assert score >= 0
    for attempt in range(1, 11):
        score = update_score(score, "Too High", attempt)
        assert score >= 0
    assert score == 0


def test_wrong_guess_subtracts_but_clamps_at_zero():
    # A wrong guess costs 5 points...
    assert update_score(20, "Too Low", 1) == 15
    assert update_score(20, "Too High", 2) == 15
    # ...but can never drop below 0.
    assert update_score(3, "Too Low", 1) == 0
    assert update_score(0, "Too High", 1) == 0


def test_too_high_has_no_arbitrary_bonus():
    # The old code added +5 on even attempts; "Too High" must always cost points.
    assert update_score(20, "Too High", 2) == 15
    assert update_score(20, "Too High", 4) == 15


def test_win_on_first_attempt_pays_full_points():
    # A first-try win should award the full 100, not an underpaid amount.
    assert update_score(0, "Win", 1) == 100


def test_win_points_scale_down_with_attempts_and_floor_at_ten():
    assert update_score(0, "Win", 2) == 90
    assert update_score(0, "Win", 3) == 80
    # Never pays less than 10, no matter how many attempts were used.
    assert update_score(0, "Win", 20) == 10

