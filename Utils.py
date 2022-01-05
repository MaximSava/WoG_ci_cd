import os
# SCORES_FILE_NAME = "c:\\temp\\scores.txt"
SCORES_FILE_NAME = "/wog/scores/scores.txt"

BAD_RETURN_CODE = ""


def screen_cleaner():
    """A function to clear the screen (useful when playing memory game or
    before a new game starts)."""
    os.system('cls||clear')
