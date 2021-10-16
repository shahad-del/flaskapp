from flask import Flask
from vsearch import search4letters
from flask import Flask,render_template, request
app = Flask(__name__)
@app.route('/')
def hello() -> str:
    return __name__

@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['Phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',the_title=title,the_results=results,the_letters=letters,the_Phrase=phrase,)
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title="Welcome to search4letters on the web")
    
app.run(debug=True)