from vsearch import search4letters
from flask import Flask, render_template, request, escape
# import mysql.connector
from contextManager import UseDatabase
app = Flask(__name__)
app.config['dbconfig'] = {'host': '127.0.0.1', 'user': 'vsearch',
                'password': 'vsearchpasswd', 'database': 'vsearchlogDB', }
 #we are adding the connection characteristics in webapp internal configuration through this app.config   built - in configuration.

def log_request(req: 'flask_request', res: str) -> None:
    # this comment out line appends in the file the data or request put by the user.you can’t use the /viewlog URL to view these latest log entries AFTER substituting it with below function, as the function associated with that URL (view_the_log) only works with the vsearch.log text file.
    # with open('vsearch.log', 'a') as log:
    # print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
    # now the below line appends the data or request put by the user in the database



#Below codes connect to the database through connector n need to be closed.

    # dbconfig = {'host': '127.0.0.1', 'user': 'vsearch',
    #             'password': 'vsearchpasswd', 'database': 'vsearchlogDB', }
    
    # conn = mysql.connector.connect(**dbconfig)
    # cursor = conn.cursor()
    # _sql = """insert into log (phrase,letters,ip,browser_string,results)values(%s,%s,%s,%s,%s)"""
    # cursor.execute(_sql, (req.form['Phrase'], req.form['letters'],
    #                req.remote_addr, req.user_agent.browser, res,))
    # conn.commit()
    # cursor.close()
    # conn.close()
#here to we are connecting to the database but using 'with' statement which needs enter and exit built in system(included in context manager) and thereby relieves us of openning and closing connections everytime.
    with UseDatabase(app.config['dbconfig']) as cursor:
        _sql = """insert into log (phrase,letters,ip,browser_string,results) values(%s,%s,%s,%s,%s)"""
        cursor.execute(_sql,(req.form['phrase'],req.form['letters'],req.remote_addr,req.user_agent.browser,res,))

@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    #return render_template('results.html')#, the_title=phrase, the_results=None, the_letters=None, the_Phrase=phrase,)
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html', the_title=title, the_results=results, the_letters=letters, the_Phrase=phrase,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title="Welcome to search4letters on the web")


@app.route('/viewlog')
# def view_the_log() -> str:
#     contents = []
#     with open('vsearch.log') as log:
#         for line in log:
#             contents.append([])
#             for item in line.split('|'):
#                 contents[-1].append(escape(item))
#     headers = ['data', 'ip', 'browser', 'user_agent']

#     return render_template('view_log.html', data=contents, h=headers)
def view_the_log() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _sql = """select phrase,letters,ip,browser_string,results from log"""
        cursor.execute(_sql)
        contents = cursor.fetchall()
    titles = ('Phrase','Letters','Remote_addr','User_agent','Results')
    return render_template('view_log.html',the_title ='View Log',the_row_titles = titles,the_data=contents,)

@app.route('/td')
def td_temp() -> 'html':
    a = [['shahad', 'suman'], ['ram', 'kumar'], ['h', 'lovely'], ['raj', 'k']]
    # return render_template('view_log.html', data=a,h = ['sNo','first_name','last_name',] ,sNo = a.index)
    # a = [['1','shahad', 'suman'],['2','ram','kumar'],['3', 'h','lovely'],['raj','k']]
    return render_template('view_log.html', data=a, h=['first_name', 'last_name'])


@app.route('/notes')
def notes_page() -> "html":
    toc = []
    with open('MyPythonNotes_Toc.txt', 'r') as contentsFile:
        for line in contentsFile:
            toc.append(tuple(line.split('|')))

    # toc = [('pythonSyntax','Python Syntax'), ('pythonDictionaries','Dictionaries')]
    return render_template('notes.html', toc=toc)

@ app.route('/class')
def class_page() -> "html":
    return render_template('class.html')
@app.route('/pythonSyntax')
def python_syntax() -> "html":
    return render_template('python_syntax.html')

@app.route('/commandLine')
def commandLine_page() -> "html":
    return render_template('commandLine.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
