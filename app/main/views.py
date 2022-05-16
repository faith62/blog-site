from flask import render_template,redirect,request,url_for,abort
from . import main
from flask_login import current_user, login_required
from ..models import User,Post,Upvote,Downvote,Comment
from .forms import UpdateProfile
from .. import db, photos


# Views
@main.route('/')

def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'one minute pitch'
    return render_template('index.html',title=title)

@main.route('/posts')
@login_required #intercept a request and check if the user is authenticated
def posts():
    posts = Post.query.all()
    likes = Upvote.query.all()
    user = current_user
    return render_template('pitch_display.html', posts=posts, likes=likes, user=user)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))