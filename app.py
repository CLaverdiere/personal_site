from flask import Flask, render_template
app = Flask(__name__)

# App settings
app.config.from_object(__name__)
app.config.update(dict(
    DEBUG=True,
))

@app.route('/')
def root():
    with open("static/content/books.txt") as bookfile:
        books = bookfile.readlines()
    return render_template('index.html', books=books)

@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.DEBUG = True
    app.run()
