from flask import Flask, render_template, request, redirect, url_for
from Wordle import * 
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def printWord():
    word = request.form['word']
    finalString, newEncoding = run(word)
    return render_template('index.html', result=zip(finalString, newEncoding))

@app.route('/random', methods=['POST'])
def printRandom():
    hiddenWord = request.form['notseen']
    # value = request.form['hide']
    finalString, newEncoding, word = runRandom('true')
    print(word)
    return render_template('index.html', result=zip(finalString, newEncoding), notseen=hiddenWord)

@app.route('/compare', methods=['POST'])
def checkWord():
    newWord = request.form['newword']
    finalString, newEncoding, word = runRandom('false')
    print(word)
    if newWord == word:
        message = "Hurrey! You have guessed the word."
        return render_template('index.html', result=zip(finalString, newEncoding), message=message, notseen='true')
    else:
        message = "Sorry! Try again."
        return render_template('index.html', result=zip(finalString, newEncoding), message=message, notseen='true')
    

if __name__ == "__main__":
    app.run(debug=True) 