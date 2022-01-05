from flask import Flask, render_template
from Utils import SCORES_FILE_NAME
import os

app = Flask(__name__)


@app.route("/")
def score_server():
    file_exists = os.path.isfile(SCORES_FILE_NAME)
    if file_exists:
        with open(SCORES_FILE_NAME, 'r') as file:
            score = file.read()
            file.close()
        return render_template('index.html', score=score)
    elif not file_exists:
        return render_template('error.html', error="File not Found")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
