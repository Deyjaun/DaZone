import pymysql
import pymysql.cursors

conn = pymysql.connect(
  database = "world",
  user = "dlawrence",
  password = "244557575",
  host = "10.100.33.60",
  cursorclass=pymysql.cursors.DictCursor
)

#users = {
 #   "john": generate_password_hash("hello")
  #  "susan": generate_password_hash("bye")
#

#@auth.verify_password
#def verify_password(username, password):
 #   if username in users and \
  #          check_password_hash(users.get(username), password):
 #       return username

 # list = ["sleep", "game", "griddy"]

