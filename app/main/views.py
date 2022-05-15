from flask import render_template,redirect,request,url_for,abort
from . import main
from flask_login import login_required
from ..models import User

# Views
@main.route('/')
@login_required #intercept a request and check if the user is authenticated
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'one minute pitch'
    return render_template('index.html',title=title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)