
from flask import Flask, render_template, request, redirect, session, url_for
import mysql.connector, json

app = Flask(__name__, template_folder='./templates', static_folder='./static')
app.secret_key = 'your_secret_key'

# Connect to the database
cnx = mysql.connector.connect(host='localhost',
                              user='root',
                              password='FD3npAChvj#',
                              database='com4003')



#routing
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def indexrender():
    return render_template('index.html')

@app.route('/home')
def homerender():
    try:
        messages = session['messages']
        return render_template('home.html', messages=json.loads(messages))
    except:
        return redirect('/')

@app.route('/login')
def loginrender():
    return render_template('login.html')

@app.route('/accounting')
def accountingrender():
    return render_template('accounting.html')

@app.route('/dentalA')
def dentalArender():
    return render_template('dentalA.html')

@app.route('/signup')
def signuprender():
    return render_template('signup.html')

@app.route('/employees')
def employeesrender():
    return render_template('employees.html')

@app.route('/employers')
def employersrender():
    return render_template('employers.html')

@app.route('/jack')
def jackrender():
    return render_template('jack.html')

@app.route('/james')
def jamesrender():
    return render_template('james.html')

@app.route('/jane')
def janerender():
    return render_template('jane.html')

@app.route('/john')
def johnrender():
    return render_template('john.html')

@app.route('/mecheng')
def mechengrender():
    return render_template('mecheng.html')

@app.route('/retail')
def retailrender():
    return render_template('retail.html')





#log in
@app.route('/login', methods=['POST'])
def login():

    email = request.form['email']
    password = request.form['password']



    
    cursor = cnx.cursor()

    query = 'SELECT * FROM users WHERE email = %s AND password = %s'
    cursor.execute(query, (email, password))

    results = cursor.fetchall()

    if results:
        current_user = results[0][0]
        

        session["messages"] = json.dumps({"person":current_user})

        return redirect("/home")


    else:
        return redirect('/signup')
#sign up
@app.route('/signup', methods=['POST'])
def signup():

    password = request.form['password']


    fname = request.form['fname']
    sname = request.form['sname']

    email = request.form['email']



    cursor = cnx.cursor()

    query = 'INSERT INTO users (fname, sname, email, password) VALUES (%s, %s, %s, %s)'
    cursor.execute(query, (fname, sname, email, password))

    cnx.commit()
    cursor.close()

    return redirect('/login')
#logout
@app.route('/logout')
def logout():

    session.pop('messages')
    return redirect('/index')


if __name__ == '__main__':
    app.run(debug=True)