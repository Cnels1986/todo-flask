from flask import Flask, url_for, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'

app.config['MYSQL_DATABASE_DB'] = 'todo'

mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/post/<int:post_id>', methods=['GET'])
def show(post_id):
    return "Showing post: %d" % post_id


@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == "POST":
        todo = request.form
        title = todo['title']
        message = todo['message']
        cursor.execute("INSERT INTO posts(title, message) VALUE(%s, %s)", (title, message))
        conn.commit()
        return 'success'
    return render_template('create.html')

if __name__ == '__main__':
    app.run()
