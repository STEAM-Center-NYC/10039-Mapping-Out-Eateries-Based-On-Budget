from flask import Flask, g, render_template, request, redirect
import flask_login
import pymysql
import pymysql.cursors
from flask_httpauth import HTTPBasicAuth
from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from pprint import pprint as print
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from dynaconf import Dynaconf

settings = Dynaconf(
    settings_file=['settings.toml']
)

def connect_db():
    return pymysql.connect(
        host="10.100.33.60",
        user=settings.user,
        password=settings.passw,
        database=settings.name,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )

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
    if request.method == 'POST':
     new_todo = request.form["new_todo"]
     todolist.append(new_todo)
     cursor = conn.cursor()
     cursor.execute(f"INSERT INTO `todos`(`description`) VALUES ('{new_todo}')")
     cursor.close()
     conn.commit()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM `todos` ORDER BY `complete`")

    results = cursor.fetchall()

    cursor.close()

    print(results)
   
    return render_template("todo.html.jinja", my_todos=results) 
    return "Hello, {}!".format(auth.current_user())




@app.route('/delete_todolist/<int:todo_index>', methods = ['POST'])
def todo_delete(todo_index):
   cursor = conn.cursor()
   cursor.execute(f"DELETE FROM `todos` WHERE id = {todo_index}")
   
   cursor.close()
   conn.commit()


   return redirect('/')

@app.route('/complete_todolist/<int:todo_index>', methods = ['POST'])
def complete_todo (todo_index):
   cursor = conn.cursor()
   cursor.execute(f"UPDATE `todos` SET `complete` = 1 WHERE `id` = {todo_index} ")
   
   cursor.close()
   conn.commit()


   return redirect('/')



@app.route('/ping')
def ping ():
    return "<h1>PONG<h1>"
@app.route('/hello/<name>')
def hello(name):
    return f"Hello {name}"

@app.route('/', methods= ['GET','POST'] )
@auth.login_required
def index():
    if request.method == 'POST':
     username = request.form["username"]
     password = request.form["username"]
     bio = request.form["username"]
     birthday = request.form["username"]



     todolist.append(new_todo)
     cursor = conn.cursor()
     cursor.execute(f"INSERT INTO `user`(`...`) VALUES ('{username}')")
     cursor.close()
     conn.commit()
