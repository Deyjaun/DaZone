from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from pprint import pprint as print
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)

auth = HTTPBasicAuth()

conn = pymysql.connect(
  database = "dlawrence_todos",
  user = "dlawrence",
  password = "244557575",
  host = "10.100.33.60",
  cursorclass=pymysql.cursors.DictCursor
)

users = {
    "Deyjaun": generate_password_hash("Sally"),
    "susan": generate_password_hash("bye")
}

todolist=['Do youtube','Get money']

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/', methods= ['GET','POST'] )
@auth.login_required
def index():