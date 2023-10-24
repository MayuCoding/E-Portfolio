from application import app, db
from flask import render_template


@app.route('/')
def home():
    """
    Route for the home page.
    """

    return render_template('home.html')

@app.route('/projects')
def projects():
    """
    Route for the projects page.
    """
    return render_template('projects.html')

@app.route('/games')
def games():
    """
    Route for the games page.
    """
    return render_template('games.html')

@app.route('/users')
def users():
    """
    Route for the users page.
    """

    user_list = db.session.execute(db.select(User).order_by(User.id)).scalars().all()

    return render_template('users.html', users=user_list)