from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
    """Creating a persons table"""
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<ID: {self.id}, name: {self.name}>'
# Calling the create_all() method   
db.create_all()

@app.route('/')
def greet():
    person = Person.query.first()
    return 'Hello ' + person.name

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
