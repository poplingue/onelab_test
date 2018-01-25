from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/my_postgres_db'
db = SQLAlchemy(app)

from model import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('GET/api/users', methods=['GET'])
def query_all_user():
	User.query_all()

@app.route('GET/api/users/<email>', methods=['GET'])
def query_user_by_email():
	User.query_by_email()

@app.route('GET/api/users/<email>', methods=['PUT'])
def query_put():
	User.modify_firstname_lastname()

if __name__ == '__main__':
    app.run()
