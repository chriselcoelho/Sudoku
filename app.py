from flask import Flask, render_template, request, redirect, url_for
from sudoku import generate_sudoku

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game', methods=['POST'])
def game():
    difficulty = request.form.get('difficulty')
    # if difficulty == 'easy':
    #     grid = generate_sudoku(9, 20)
    # elif difficulty == 'medium':
    #     grid = generate_sudoku(9, 40)
    # elif difficulty == 'hard':
    #     grid = generate_sudoku(9, 60)
    # else:
    #     grid = generate_sudoku(9, 20)
    board= generate_sudoku(difficulty)
    return render_template('game.html', board=board)

if __name__ == '__main__':
    app.run(debug=True)

