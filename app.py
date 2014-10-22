from collections import OrderedDict
from flask import Flask, render_template, g
from itertools import islice
from os import listdir
from string import rstrip

app = Flask(__name__)

# App settings
app.config.from_object(__name__)
app.config.update(dict(
    BGIMAGES=False,
    DEBUG=True,
))

class Project:
    def __init__(self, name, link, desc):
        self.name, self.link, self.desc = name, link, desc

# Backgrounds
@app.before_request
def load_bgs():
    if app.config['BGIMAGES'] == True:
        g.bgs = [bg for bg in listdir("static/bg") if bg.endswith("texture.png")]
    else:
        g.bgs = []

@app.route('/')
def root():
    with open("static/content/projects.txt") as project_file:
        projects = list()
        while True:
            project_info = [s.rstrip() for s in islice(project_file, 4)]
            if not project_info:
                break
            name, link, desc = project_info[:3]
            project = Project(name, link, desc)
            projects.append(project)

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
