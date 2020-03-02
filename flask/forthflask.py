import psycopg2
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
        database="postgres", user="postgres", password="tongji2018openedu", host="202.120.167.50", port="5432")


@app.route('/rest/anon/tasks',methods=['POST'])
def create():
    cur = conn.cursor()
    data = request.get_json()
    cur.execute("insert into taskthree(performer, description, begintime, endtime, state, title) values(%s,%s,%s,%s,%s,%s)",
             (data['performer'], data['description'], data['begintime'], data['endtime'], data['state'], data['title']))
    conn.commit()
    return "1"


@app.route('/rest/anon/tasks',methods=['GET'])
def read():
    cur = conn.cursor()
    cur.execute(
        "select * from taskthree")
    rows = cur.fetchall()
    l = []
    for row in rows:
        print(row)
        dic= {'id': str(row[0]),'description': str(row[1]),'begintime':str(row[2]),'endtime':str(row[3]),'performer':str(row[4]),'state':str(row[5]),'title':str(row[6])}
        l.append(dic)
    return jsonify(l)


@app.route('/rest/anon/tasks/<string:id>', methods=['PUT'])
def update(id):
    cur = conn.cursor()
    data = request.get_json()

    cur.execute("UPDATE taskthree SET performer = '{}', title = '{}', description = '{}', state = '{}', begintime = '{}', endtime = '{}'  WHERE id = {}"
        .format(data['performer'],data['title'],data['description'],data['state'],data['begintime'],data['endtime'], id))


    conn.commit()
    return "1"


@app.route('/rest/anon/tasks/<string:id>', methods=['DELETE'])
def delete(id):
    cur = conn.cursor()
    cur.execute("DELETE from taskthree where id="+ id)
    conn.commit() 
    return "1"


if __name__ == '__main__':
    app.run()
