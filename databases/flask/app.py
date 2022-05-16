from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://faith@localhost:5432/test'
db = SQLAlchemy(app)

@app.route('/')
def greet():
    return 'Hello World!'

if __name__ == '__main__':
   app.run(host="0.0.0.0")
