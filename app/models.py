from .import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))

    
    @property # decorator to create a write only class
    def password(self):
        raise AttributeError('You cannot read the password attribute') #block access to the password property

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password): #takes in a password, hashes it and compares it to the hashed password to check if they are the same.
        return check_password_hash(self.password_hash,password)


    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model): #define all the different roles
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic") # db.relationship to create a virtual column that will connect with the foreign key. We pass in 3 arguments. The first one is the class that we are referencing which is User. Next backref allows us to access and set our User class. We give it the value of role now because when we want to get the role of a user instance we can just run user.role. Lazy parameter is how SQLAlchemy will load our projects. The lazy option is our objects will be loaded on access and filtered before returning.



    def __repr__(self):
        return f'User {self.name}'