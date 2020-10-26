from flask import Flask, render_template, url_for, flash
from forms import RegistrationForm, LoginForm
app = Flask(__name__)


app.config['SECRET_KEY'] = 'd325630d4e7fd31b967238c399a18765'

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
        flash(f'Account created for {form.username.data}!')
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
