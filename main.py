from flask import Flask, request
import sqlite3
from hashlib import md5
import re

app = Flask(__name__)

# DB Init
dbconn = sqlite3.connect('users.db')
with open('ddl.sql') as f:
    dbconn.executescript(f.read())


def get_db_connection():
    connection = sqlite3.connect('users.db')
    connection.row_factory = sqlite3.Row
    return connection


def query_db(query: str, conn: sqlite3.Connection, args=(), commit=False):
    cur = conn.execute(query, args)
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    if commit:
        conn.commit()
    return r


@app.route('/api/users', methods=['POST'])
def create_user():
    cur = get_db_connection()

    try:

        r = re.compile('\d\d\d\d-\d\d\-\d\d')

        if 'username' not in request.json or request.json['username'] == '':
            return 'no username', 400
        elif 'birthdate' not in request.json or request.json['birthdate'] == '':
            return 'no birthdate', 400
        elif 'password' not in request.json or request.json['password'] == '':
            return 'no password', 400
        elif len(request.json['password']) < 8:
            return 'too weak password (minimum 8 symbols)', 422
        elif r.match(request.json['birthdate']) is None:
            return 'wrong birthdate format (YYYY-MM-DD)', 422

        newid = query_db('INSERT INTO users (username, birthdate, status, password, email) \
                            VALUES (?, date(?), ?, ?, ?) RETURNING id', cur, (request.json['username'],
                                                                              request.json['birthdate'],
                                                                              request.json['status'],
                                                                              md5(str(request.json['password']).encode(
                                                                                  'utf-8')).hexdigest(),
                                                                              request.json['email']), True)

        return newid
    except Exception as err:
        return str(err), 500
    finally:
        cur.close()


@app.route('/api/users', methods=['GET'])
def get_users():
    cur = get_db_connection()

    try:
        users = query_db("select * from users", cur)
        return users
    except Exception as err:
        return str(err), 500
    finally:
        cur.close()


@app.route('/api/users/<int:id>', methods=['PUT'])
def set_status(id):
    cur = get_db_connection()

    try:
        for k, v in request.json.items():
            if k not in ('status', 'email', 'password', 'username'):
                return 'wrong params to update', 422
            elif v == '':
                return 'value is empty', 422

            if k == 'password':
                if len(v) < 8:
                    return 'too weak password (minimum 8 symbols)', 422
                v = md5(str(request.json['password']).encode(
                    'utf-8')).hexdigest()

            res = query_db("UPDATE users SET " + k + " = ? where id = ? RETURNING id",
                           cur, (v, id), True)

            if len(res) == 0:
                return 'no such user', 412

        return 'successful'
    except Exception as err:
        return str(err), 500
    finally:
        cur.close()


@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    cur = get_db_connection()

    try:
        res = query_db("DELETE FROM users WHERE id = ? RETURNING id",
                       cur, (id, ), True)
        if len(res) == 0:
            return 'no such user', 412
        return 'successful'
    except Exception as err:
        return str(err), 500
    finally:
        cur.close()


@app.route('/api/users/auth', methods=['POST'])
def auth_user():
    cur = get_db_connection()

    if 'username' not in request.json or request.json['username'] == '':
        return 'no username', 400
    elif 'password' not in request.json or request.json['password'] == '':
        return 'no password', 400

    try:
        res = query_db("SELECT case when ? = password then true else false end auth FROM users where username = ?",
                       cur, (md5(str(request.json['password']).encode('utf-8')).hexdigest(), request.json['username']), True)
        if len(res) == 0:
            return 'no such user', 412
        if not res[0]['auth']:
            return 'wrong password user', 401
        return 'successful'
    except Exception as err:
        return str(err), 500
    finally:
        cur.close()
