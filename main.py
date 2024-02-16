from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from pprint import pprint as print
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import flask_login

conn = pymysql.connect(
  database = "world",
  user = "dlawrence",
  password = "244557575",
  host = "10.100.33.60",
  cursorclass=pymysql.cursors.DictCursor
)

app = Flask(__name__)


app.secret_key = "sauce" # change this!
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

class User:
    is_authentication = True
    is_anonymous = False
    is_active = True
def __init__(self, id, username):

    self.username = username
    self.id = id

    def get_id(self):

        return str(self.id)

@login_manager.user_loader
def load_user(user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * from `users` WHERE `id` = " + user_id)
    result = cursor.fetchone()
    cursor.close()
    conn.commit()

    if result is None:
        return None
    return User(result["id"] , result["username"])




@app.route('/')
def landing_page():
    if flask_login.current_user.is_authenticated:
        return redirect('/feed')
    return render_template("landing.html.jinja")




"""
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Do this for every input in your form
        username = request.form["username"]
        password = request.form["password"]
        bio = request.form["bio"]
        birthday = request.form["birthday"]
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO `user` (`username`, `password`, `birthday`) VALUES ('{username}', '{password}', '{bio}')")
        cursor.close()
        conn.commit()

"""
   
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Do this for every input in your form
        username = request.form["username"]
        password = request.form["password"]
        bio = request.form["bio"]
        birthday = request.form["birthday"]


        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO `user`('{username}', '{password}', '{bio}')")
        cursor.close()
        conn.commit()
    
    return render_template("landing.html.jinja")
   
   
@app.route('/feed')
@flask_login.login_required
def feed():
   return flask_login.current_user



def connect_db():
    return pymysql.connect(
        host="10.100.33.60",
        user="YOUR_USERNAME",
        password="YOUR_PASSWORD",
        database="YOUR_DATABASE_NAME",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )

def get_db():
    '''Opens a new database connection per request.'''        
    if not hasattr(g, 'db'):
        g.db = connect_db()
    return g.db    

@app.teardown_appcontext
def close_db(error):
    '''Closes the database connection at the end of request.'''    
    if hasattr(g, 'db'):
        g.db.close() 


cursor = get_db().cursor()

   
   # cursor.execute(f """ SELECT * FROM `users` WHERE `username` = `{username}` """)
   #user = cursor.fetchone()

   #if password == user["password"]:
        #return redirect('/feed')

   #cursor.close()
       # conn.commit()

   # return render_template("register.html.jinja")