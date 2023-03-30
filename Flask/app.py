from flask import Flask, render_template, request, redirect, url_for, session
import pymysql as pms
import MySQLdb.cursors
import re
from idk import search

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
#%%
conn=pms.connect(host='localhost',
                 port=3306,
                 user='root',
                 password='karu0302', 
                 )
cursor=conn.cursor()
#cursor.execute("CREATE DATABASE dbasemlt1;")
cursor.execute("USE flaskdatabase")
output=cursor.fetchall()

#%%

@app.route('/login/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ' '
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
        
        if account:
            session['loggedin'] = True
            #session['id'] = account['id']
            #session['username'] = account['username']
            msg = 'Logged in successfully!'
            return redirect(url_for('scs'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg=msg)
#%%
@app.route('/login/scs', methods=['GET', 'POST'])
def scs():
    msg = 'Logged in successfully!'
    return render_template('appp.html',msg = msg)
    
@app.route('/login/scs/scspg', methods=['GET', 'POST'])
def scspg():
    #msg='Logged in successfully!'
    if request.method == 'POST':
        book = request.form['name']
        obj = search(book)
        html_code = obj.render()
        return render_template('scspg.html', obj = html_code)
    else :
        return render_template('scspg.html')

#%%
@app.route('/login/logout')

def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))
#%%
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ' '
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
            cursor.connection.commit()
            msg = 'You have successfully registered!'
            
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)
#%%
import pickle
model = pickle.load(open('model.pkl','rb'))

#%%
if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(host = 'localhost',port = 5000)