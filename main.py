from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from pprint import pprint as print
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

conn = pymysql.connect(
  database = "world",
  user = "dlawrence",
  password = "244557575",
  host = "10.100.33.60",
  cursorclass=pymysql.cursors.DictCursor
)

app = Flask(__name__)



auth = HTTPBasicAuth()

@app.route('/')
def index ():
    return render_template("home.html.jinja")





@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Do this for every input in your form
        username = request.form["username"]
        password = request.form["password"]
        bio = request.form["bio"]
        birthday = request.form["birthday"]


        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO `user` (__PUT_COLUMNS_HERE__) VALUES ('{username}', '{password}', '{bio}')")
        cursor.close()
        conn.commit()
    
    return render_template("register.html.jinja")