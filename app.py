# project/__init__.py
from flask import flash, abort, Flask, jsonify, render_template, redirect, url_for, request
from flask_wtf.form import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SubmitField, TextAreaField, Form
from wtforms.validators import  Length, DataRequired, Optional
import flask_login
# from 

import uuid
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = '123456781'

# login_manager = flask_login.LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('/index.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    # # db = get_db()
    # # error = None

    # if not username:
    #     error = 'Username is required.'
    # elif not password:
    #     error = 'Password is required.'

        if username == "abc" and password == "abc":
            return f"<html><body>Welcome {username}</body></html>"
        else:
            return f"<html><body>Welcome!</body></html>"

@app.route('/md', methods=['GET', 'POST'])
def markdown():
    if request.method == 'GET':
        return render_template('/md.html')
    # if request.method == 'POST':
    #     username = request.form['username']
    #     password = request.form['password']
    # # # db = get_db()
    # # # error = None

    # # if not username:
    # #     error = 'Username is required.'
    # # elif not password:
    # #     error = 'Password is required.'

    #     if username == "abc" and password == "abc":
    #         return f"<html><body>Welcome {username}</body></html>"
    #     else:
    #         return f"<html><body>Welcome!</body></html>"


    

@app.route('/test_post/mindmap', methods=['POST'])
def test_post_mindmap():
    print(request)
    from lxml import etree
    # f = open("./data/" + "example" + ".html","r",encoding="utf-8") #读取文件
    # f = f.read()
    # html = etree.HTML(f)
    return jsonify({'code' : True,'message' : 'example'})

@app.route('/test_post/slides', methods=['POST'])
def test_post_slides():
    print(request.form['data'])
    from lxml import etree
    # f = open("./data/" + "example" + ".html","r",encoding="utf-8") #读取文件
    # f = f.read()
    # html = etree.HTML(f)
    
    return jsonify({'code' : True,'message' : 'example16a'})

# class MockCreate(Form):
#     # user_email = StringField("email address",[Email()])
#     # api = StringField("api",[DataRequired()])
#     submit = SubmitField("Submit")
#     # code = IntegerField("code example: 200",[DataRequired()])
#     # alias = StringField("alias for api")
#     data = TextAreaField("json format",[DataRequired()])

# @app.route("/mockservice",methods=['GET','POST'])
# def MockController():
#     form = MockCreate()
#     # code = form['code']
#     # api = form['api']
#     print(form.data)
#     return 'Successfully sent {}'.format(form.data[1:-1]) 

@app.route('/custom', methods=['GET', 'POST'])
def custom():
    if request.method == 'POST':
        fuck = request.form.get('fuck')
        return 'Successfully sent {}'.format(fuck) 

if __name__ == "__main__":
    app.run(debug=True)
