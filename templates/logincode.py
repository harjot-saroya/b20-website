from flask import Flask, session, redirect, url_for, escape, request, render_template, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlachemy.sql import text
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////user_info.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
	if request.authorization and request.authorization.username == 'username' and request.authorization.password == 'password':
		return '<h1>you are logged in</h1>'
	return make_response('Could not verify!',401,{'WWW-Authenticate':'Basic realm="Login Required"'})


if __name__== "__main__":
	app.run(debug = True, host = '0.0.0.0', port = 5000)