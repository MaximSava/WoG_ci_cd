from Utils import SCORES_FILE_NAME
import os


def add_score(difficulty_number):
    """The function’s input is a variable called difficulty. The function will try to read
    the current score in the scores file, if it fails it will create a new one and will use it to save
    the current score.
    POINTS_OF_WINNING = (DIFFICULTY X 3) + 5"""
    file_exists = os.path.isfile(SCORES_FILE_NAME)
    points_of_winning = (difficulty_number * 3) + 5
    print(points_of_winning)
    if file_exists:
        with open(SCORES_FILE_NAME, 'r+') as file:
            read_score = file.read()
            print(read_score)
            new_score = int(read_score) + int(points_of_winning)
            print(new_score)
            file.seek(0)
            file.write(str(new_score))
            file.close()
    elif not file_exists:
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(points_of_winning))
            file.close()
