from flask import render_template, url_for, flash, redirect
from flaskblog.models import User, Post
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm

posts = [
    {
        'title': 'Learn flask in a better way!',
        'author': 'Chogi24',
        'created_on': '25th October 2020'
    },
    {
        'title': 'Destroy all aliens!',
        'author': 'Ben 10',
        'created_on': '10th October 2010'
    }
]


@app.route('/')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Incorrect login credentials!', 'danger')
    return render_template('login.html', title='Login', form=form)
