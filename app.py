from flask import Flask, render_template, session, request, redirect, url_for
import spotify, utils
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')


@app.route('/results')
def results():
    results = "<h1>Results</h1>"
    #results = "<button href='" + spotify "' />Go to your playlist</button>"
    return render_template('results.html', results = results)


if __name__ == '__main__':
    app.secret_key = 'DONT PUT THIS ON GITHUB IF YOU WANT SECURITY'
    app.run('0.0.0.0', port=8000)
