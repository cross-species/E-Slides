# project/__init__.py
from flask import flash, abort, Flask, render_template, redirect, url_for, request
from flask_wtf.form import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import  Length,DataRequired,Optional
import flask_login

import uuid
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = '123456781'

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # Here we use a class of some kind to represent and validate our
#     # client-side form data. For example, WTForms is a library that will
#     # handle this for us, and we use a custom LoginForm to validate.
#     form = LoginForm()
#     if form.validate_on_submit():
#         # Login and validate the user.
#         # user should be an instance of your `User` class
#         login_user(user)

#         flask.flash('Logged in successfully.')

#         next = flask.request.args.get('next')
#         # is_safe_url should check if the url is safe for redirects.
#         # See http://flask.pocoo.org/snippets/62/ for an example.
#         if not is_safe_url(next):
#             return flask.abort(400)

#         return flask.redirect(next or flask.url_for('index'))
#     return flask.render_template('login.html', form=form)

# @app.route('/login/', methods=('GET', 'POST'))  # 登录
# def login():
#     form = LoginForm()
#     emsg = None
#     if form.validate_on_submit():
#         user_name = form.username.data
#         password = form.password.data
#         user_info = get_user(user_name)  # 从用户数据中查找用户记录
#         if user_info is None:
#             emsg = "用户名或密码密码有误"
#         else:
#             user = User(user_info)  # 创建用户实体
#             if user.verify_password(password):  # 校验密码
#                 flask_login.login_user(user)  # 创建用户 Session
#                 return redirect(request.args.get('next') or url_for('index'))
#             else:
#                 emsg = "用户名或密码密码有误"
#     return render_template('login.html', form=form, emsg=emsg)

class LoginForm(FlaskForm):
    username = StringField('账户名：', validators=[DataRequired(), Length(1, 30)])
    password = PasswordField('密码：', validators=[DataRequired(), Length(1, 64)])
    remember_me = BooleanField('记住密码', validators=[Optional()])

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flash('Logged in successfully.')

        next = request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        # if not is_safe_url(next):
        #     return abort(400)

        return redirect(next or url_for('index'))
    return render_template('login.html', form=form)

# @app.route('/', methods=('GET', 'POST'))
# def login():
#     # username = request.form['username']
#     # password = request.form['password']
#     # # db = get_db()
#     # # error = None

#     # if not username:
#     #     error = 'Username is required.'
#     # elif not password:
#     #     error = 'Password is required.'

#     ##############不管用户名密码是什么都login#############
#     # elif db.execute(
#     #     'SELECT id FROM user WHERE username = ?', (username,)
#     # ).fetchone() is not None:
#     #     error = 'User {} is already registered.'.format(username)

#     # if error is None:
#     #     db.execute(
#     #         'INSERT INTO user (username, password) VALUES (?, ?)',
#     #         (username, generate_password_hash(password))
#     #     )
#     #     db.commit()
#     #     return redirect(url_for('auth.login'))

#     # flash(error)

#     return render_template('index.html')

# class User(flask_login.UserMixin):
#     pass


# @login_manager.user_loader
# def user_loader(email):
#     if email not in users:
#         return

#     user = User()
#     user.id = email
#     return user


# @login_manager.request_loader
# def request_loader(request):
#     email = request.form.get('email')
#     if email not in users:
#         return

#     user = User()
#     user.id = email

#     # DO NOT ever store passwords in plaintext and always compare password
#     # hashes using constant-time comparison!
#     user.is_authenticated = request.form['password'] == users[email]['password']

#     return user



# # ...
# USERS = [
#     {
#         "id": 1,
#         "name": 'lily',
#         "password": generate_password_hash('123456781')
#     },
#     {
#         "id": 2,
#         "name": 'tom',
#         "password": generate_password_hash('123456781')
#     }
# ]

# # ...
# def create_user(user_name, password):
#     """创建一个用户"""
#     user = {
#         "name": user_name,
#         "password": generate_password_hash(password),
#         "id": uuid.uuid4()
#     }
#     USERS.append(user)

# def get_user(user_name):
#     """根据用户名获得用户记录"""
#     for user in USERS:
#         if user.get("name") == user_name:
#             return user
#     return None


# from flask_login import UserMixin  # 引入用户基类
# from werkzeug.security import check_password_hash
# # ...
# class User(UserMixin):
#     """用户类"""
#     def __init__(self, user):
#         self.username = user.get("name")
#         self.password_hash = user.get("password")
#         self.id = user.get("id")

#     def verify_password(self, password):
#         """密码验证"""
#         if self.password_hash is None:
#             return False
#         return check_password_hash(self.password_hash, password)

#     def get_id(self):
#         """获取用户ID"""
#         return self.id

#     @staticmethod
#     def get(user_id):
#         """根据用户ID获取用户实体，为 login_user 方法提供支持"""
#         if not user_id:
#             return None
#         for user in USERS:
#             if user.get('id') == user_id:
#                 return User(user)
#         return None


# @login_manager.user_loader  # 定义获取登录用户的方法
# def load_user(user_id):
#     return User.get(user_id)

# from wtforms import StringField, PasswordField
# from wtforms.validators import DataRequired, EqualTo
# # ...
# class LoginForm(FlaskForm):
#     """登录表单类"""
#     username = StringField('用户名', validators=[DataRequired()])
#     password = PasswordField('密码', validators=[DataRequired()])

#     if __name__ == '__main__':
#     app.run(debug=True)