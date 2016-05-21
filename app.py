from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')


@app.route('/results')
def page1():
    return render_template('results.html')


if __name__ == '__main__':
    app.secret_key = 'DONT PUT THIS ON GITHUB IF YOU WANT SECURITY'
    app.run('0.0.0.0', port=8000)
