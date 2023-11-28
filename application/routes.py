from application import app, db
from flask import render_template

with app.app_context():
    from application.models import User, Admin, create_test_data
    from application import db

    if not db.inspect(db.engine).has_table(db.engine, "user"):
        db.create_all()
        create_test_data(db)
        

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

@app.route('/register')
def register():
    """
    Route for the register page.
    """
    return render_template('register.html')

@app.route('/signin')
def signin():
    """
    Route for the signin page.
    """
    return render_template('signin.html')

@app.route('/users')
def users():
    """
    Route for the users page.
    """
    users_list = db.session.execute(db.select(User).order_by(User.id)).scalars().all()

    return render_template('users.html', users=users_list)

@app.route('/users/<int:user_id>')
def user(user_id):
    """
    Route for the user page.
    """
    user = db.session.execute(db.select(User).filter(User.id == user_id)).scalars().first()

    return render_template('user.html', user=user)

@app.route('/teatalk')
def teatalk():
    """
    Routes for a tea talk.
    """

    return render_template("teatalk.html")