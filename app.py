# project/__init__.py
from flask import Flask
app = Flask(__name__)


@app.route('/',methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # db = get_db()
        # error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        # elif db.execute(
        #     'SELECT id FROM user WHERE username = ?', (username,)
        # ).fetchone() is not None:
        #     error = 'User {} is already registered.'.format(username)

        # if error is None:
        #     db.execute(
        #         'INSERT INTO user (username, password) VALUES (?, ?)',
        #         (username, generate_password_hash(password))
        #     )
        #     db.commit()
        else:
            return redirect(url_for('home'))

        # flash(error)

    return render_template('index.html')


@app.route('/home',methods=('GET', 'POST'))
def home():
    return render_template("templates/home.html")

@app.rout('/edit', methods=('GET', 'POST'))
def edit():
    return render_template("templates/edit.html")

