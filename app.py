from flask import Flask, render_template
import sqlite3 as db

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', title='python flow')

if __name__ == '__main__':
	app.run(debug=True)



