from flask import render_template,redirect,request,url_for
from . import main
from flask_login import login_required

# Views
@main.route('/')
@login_required #intercept a request and check if the user is authenticated
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'one minute pitch'
    return render_template('index.html',title=title)