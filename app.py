# project/__init__.py
from flask import Flask
app = Flask(__name__)


@app.route('/', methods=('POST'))
def login():
    username = request.form['username']
    password = request.form['password']
    # db = get_db()
    # error = None

    if not username:
        error = 'Username is required.'
    elif not password:
        error = 'Password is required.'

    ##############不管用户名密码是什么都login#############
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
    #     return redirect(url_for('auth.login'))

    # flash(error)

    return render_template('/.html')
