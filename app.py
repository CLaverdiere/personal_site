from collections import OrderedDict
from flask import Flask, render_template, g
from os import listdir

app = Flask(__name__)

# App settings
app.config.from_object(__name__)
app.config.update(dict(
    DEBUG=True,
))

# Backgrounds
@app.before_request
def load_bgs():
    g.bgs = [bg for bg in listdir("static/bg") if bg.endswith(".png")]

@app.route('/')
def root():
    with open("static/content/projects.txt") as project_file:
        projects = OrderedDict()
        for line in project_file:
            name, link = line.partition('=')[::2]
            projects[name] = link
    with open("static/content/books.txt") as book_file:
        books = book_file.readlines()
    return render_template('index.html', projects=projects, books=books)

@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.DEBUG = True
    app.run()
