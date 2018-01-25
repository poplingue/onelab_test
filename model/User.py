

from onelab_test import db

class User(db.Model):
    __tablename__ = "users"
    firstname = db.Column(db.String(40), unique=False)
    lastname =  db.Column(db.String(40), unique=False)
    email = db.Column(db.String(120), unique=True, primary_key=True)

    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def __repr__(self):
        return '{} {} {}'.format(self.firstname, self.lastname, self.email)

    def query_all(self):
    	return User.query.all()

    def query_by_email(self, email):
        return User.query.filter(User.email == email)

    def modify_firstname_lastname(self, email, new_firstname, new_lastname):
    	user = User.query.filter(User.email == email)
    	user.firstname = new_firstname
    	user.lastname = new_lastname
    	db.session.commit()


    