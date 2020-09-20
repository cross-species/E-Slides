# project/__init__.py
from flask import flash, abort, Flask, jsonify, render_template, redirect, url_for, request, make_response, send_from_directory, send_file
from flask_wtf.form import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, SubmitField, TextAreaField, Form
from wtforms.validators import Length, DataRequired, Optional
from call import *
import time
# import flask_login

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

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if username == "abc" and password == "abc":
            return redirect(url_for("project"))
        else:
            return f"<html><body>Welcome! Please regester.</body></html>"


@app.route('/md', methods=['GET', 'POST'])
def markdown():
    if request.method == 'GET':
        return render_template('/md.html')


@app.route('/test_post/mindmap', methods=['POST'])
def post_mindmap():
    print(request.form['data'])
    md_name = "example" # TODO:file_name is extracted from DB
    # with open("static/data/" + md_name + ".md", "w") as f:
    #     f.write(request.form['data'])
    # f.close()
    save_md(request.form['data'], md_name)
    mmp_name = md_name + "_mindmap_"+str(time.time())
    callMindMap(md_name, mmp_name)
    return jsonify({'code': True, 'message': mmp_name})

@ app.route("/show/<file_name>", methods=['GET'])
def show_file(file_name):
    return app.send_static_file("data/"+file_name)

@app.route('/get_file/<file_name>', methods=['GET'])
def get_file(file_name):
    directory = config.APP_PATH #TODO: your local directory
    try:
        response = make_response(
            send_from_directory(directory, file_name, as_attachment=True))
        return response
    except Exception as e:
        return jsonify({"code": "异常", "message": "{}".format(e)})


# status = False
@app.route('/test_post/jupyter', methods=['POST'])
def new_jupyter():
    pj_path = "D:\\E-Slides\\static\\data\\" # TODO:path is extracted from DB, according to user id
    # if not status:
    #     status = startJupyter(pj_path)
    # if status:
    file_name = "example" # TODO:file_name is extracted from DB, according to user id
    url = "http://localhost:8889/notebooks/" + file_name + ".ipynb"
    return jsonify({'code': True, 'jupyter_home':"http://localhost:8889/tree", 'jupyter_file': url})


@app.route('/test_post/slides', methods=['POST'])
def post_slides():
    print(request.form['data'])
    md_name = "example"
    save_md(request.form['data'], md_name)
    sld_name = md_name + "_slides_"+ str(time.time())
    callSlides(md_name, sld_name, file_type='html', style='slidy')
    return jsonify({'code': True, 'message': sld_name})

@app.route('/projects', methods=('GET', 'POST'))
def project():
    return render_template("/projects.html")


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




# @app.route('/custom', methods=['GET', 'POST'])
# def custom():
#     if request.method == 'POST':
#         fuck = request.form.get('fuck')
#         return 'Successfully sent {}'.format(fuck)


if __name__ == "__main__":
    app.run(debug=True)
