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
@app.route('/results')
def index():

    cursor = mysql.connection.cursor()

    query = "SELECT * from grades WHERE module_code='MATH101';"

    cursor.execute(query)
    results = cursor.fetchall()
 
    list_of_surnames = []
    list_of_forenames = []
    list_of_grades = []
    for row in results:
        list_of_surnames.append(row[0].encode("utf-8"))
        list_of_forenames.append(row[1].encode("utf-8"))
        list_of_grades.append(row[3])

    ordered_list = []
    for i in range(len(list_of_forenames)):
        ordered_list.append(
            [list_of_forenames[i],
            list_of_surnames[i],
            list_of_grades[i]]
        )
    results_tuple_cleaned = tuple(ordered_list)

    cursor.close()

    return render_template('results.html', scores=results_tuple_cleaned)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
