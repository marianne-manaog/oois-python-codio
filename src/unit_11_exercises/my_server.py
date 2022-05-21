from flask import Flask
from flask_mysqldb import MySQL
from flask import Flask, render_template

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'

app.config['MYSQL_USER'] = <MY_USERNAME>
app.config['MYSQL_PASSWORD'] = <MY_PASSWORD>

app.config['MYSQL_DB'] = 'students'

mysql = MySQL(app)


@app.route('/')
@app.route('/index')
def index():

    cursor = mysql.connection.cursor()

    query = "SELECT * from grades;"

    cursor.execute(query)
    results = cursor.fetchall()
 
    cursor.close()


    return render_template('index.html', scores=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
