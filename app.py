from flask import Flask, render_template, request
from lib.ut.robot import Robot

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    error = None

    if request.method == 'POST':
        search_field = request.form.get('search_field')

    # Get data from search_engine



    return( render_template('index.html'))

@app.route('/search', methods=['GET'])
def search():
    robot = Robot()

    error, words, results = None, request.args.get('search_field'), robot.get_results()

    if(len(results) == 0):
        error = "По вашему запросу ничего не найдено"
    return( render_template('results.html', words=words, error=error, results=results))

@app.route('/info')
def info():
    return( render_template('info.html'))

if __name__ == '__main__':
    app.run()
