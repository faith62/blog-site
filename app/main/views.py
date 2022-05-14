from flask import render_template,redirect,request,url_for
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'one minute pitch'
    return render_template('index.html',title=title)