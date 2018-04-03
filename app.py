from flask import Flask, request
import psycopg2


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello world!"


@app.route('/testpost', methods=["POST", "GET"])
def testpost():
    conn = psycopg2.connect(host="localhost", user="postgres", dbname="test")
    cur = conn.cursor()
    print(cur.execute("insert into tabela1 (id,ime,prezime,email) values (6,'{ime}','sdaas','gdfg')".format(ime=request.json['test'])))
    print(conn.commit())
    return "nje"


if __name__ == '__main__':
    app.run()
