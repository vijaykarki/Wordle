from flask import Flask, render_template, request
from Wordle import run
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def printMain():
    word = request.form['word']
    finalString, newEncoding = run(word)
    
    # printColorMetrix = run()
    # return finalString
    return render_template('index.html', result=zip(finalString, newEncoding))


if __name__ == "__main__":
    app.run()