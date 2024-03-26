from flask import Flask, g, render_template, request, redirect
import flask_login
import pymysql
import pymysql.cursors
from flask_httpauth import HTTPBasicAuth
from dynaconf import Dynaconf

app = Flask(__name__)
app.secret_key = "top_secret"

settings = Dynaconf(
    settings_file=['settings.toml']
)

def get_id(self):
    return str(self.id)

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

def connect_db():
    return pymysql.connect(
        host="10.100.33.60",
        user=settings.user,
        password=settings.passw,
        database=settings.name,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )
@app.route('/')
def index():
    cursor = get_db().cursor()
    if request.method == 'POST':
        cursor.execute("SELECT * FROM `Name`")
        rests = cursor.fetchall()
        get_db().commit()
    return render_template('index.html.jinja', rests=rests)


@app.route('/aboutus')
def about():
    return render_template('Aboutus.html.jinja')

if __name__ == '__main__':
    app.run(debug=True)