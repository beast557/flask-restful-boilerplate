
from flask import Flask, redirect, render_template, request, flash, session, url_for
from flask_mysqldb import MySQL
from functools import wraps

app = Flask(__name__)
# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crime_report'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# init MYSQL
mysql = MySQL(app)


@app.route("/")
def index():
    return "<p>Hello, World!</p>"


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM user WHERE email = %s", [email])
        if result > 0:
            data = cur.fetchone()
            password_candidate = data['password']
            if(password == password_candidate):
                session['logged_in'] = True
                session['email'] = email
                flash('You are now logged in', 'success')
                return redirect(url_for('home'))
            flash('username or password didn\'t match')
        flash('username or password didn\'t match')
    return render_template('login.html', title="Login")


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        phone_number = request.form['phone_number']

        cur = mysql.connection.cursor()

        result = cur.execute("INSERT INTO user(first_name,last_name,email,password,phone_number) VALUES(%s,%s,%s,%s,%s)",
                             (first_name, last_name, email, password, phone_number))
        if(result):
            data = cur.execute("SELECT id from user WHERE email = %s", [email])
            data = cur.fetchone()
            data = data['id']
            cur.execute(
                "INSERT INTO user_role(role,user_id) VALUES(%s,%s)", ("user", data))
        mysql.connection.commit()
        cur.close()
        flash('You are now registered and can login ', 'sucess')
        return redirect(url_for('signup'))
    return render_template('signup.html', title="Sign up")


@app.route("/home")
def home():
    return render_template('home.html')

# Check if user logged in


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap


@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


@app.route("/add_complain_type")
def complain_type():
    return "<p>Hello, World!</p>"


@app.route("/complain")
def make_complain():
    return "<p>Hello, World!</p>"


@app.route("/complain")
def complain():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    # db.init_app(app)
    app.secret_key = 'secret123'
    app.run(port=5000, debug=True)
