from flask import Flask
from vsearch import search4letters
from flask import Flask,render_template, request, escape
app = Flask(__name__)
def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['Phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',the_title=title,the_results=results,the_letters=letters,the_Phrase=phrase,)



@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title="Welcome to search4letters on the web")


@app.route('/viewlog')

def view_the_log() -> str:
    contents=[]
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    headers = ['data','ip','browser','user_agent']

    return render_template('view_log.html',data = contents,h = headers)

@app.route('/td')
def td_temp() -> 'html':
    a = [['shahad', 'suman'],['ram','kumar'],['h','lovely'],['raj','k']]
    # return render_template('view_log.html', data=a,h = ['sNo','first_name','last_name',] ,sNo = a.index)
    # a = [['1','shahad', 'suman'],['2','ram','kumar'],['3', 'h','lovely'],['raj','k']]
    return render_template('view_log.html', data=a,h = ['first_name','last_name'])

@app.route('/notes')
def notes_page() -> "html":
    toc = []
    with open('MyPythonNotes_Toc.txt', 'r') as contentsFile:
        for line in contentsFile:
            toc.append(tuple(line.split('|')))

    # toc = [('pythonSyntax','Python Syntax'), ('pythonDictionaries','Dictionaries')]
    return render_template('notes.html', toc = toc)


@app.route('/pythonSyntax')
def python_syntax() -> "html":
    return render_template('python_syntax.html')

    
app.run(debug=True)