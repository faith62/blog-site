from .import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))



    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model): #define all the different roles
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic") # db.relationship to create a virtual column that will connect with the foreign key. We pass in 3 arguments. The first one is the class that we are referencing which is User. Next backref allows us to access and set our User class. We give it the value of role now because when we want to get the role of a user instance we can just run user.role. Lazy parameter is how SQLAlchemy will load our projects. The lazy option is our objects will be loaded on access and filtered before returning.



    def __repr__(self):
        return f'User {self.name}'