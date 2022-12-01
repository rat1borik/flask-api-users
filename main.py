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
            return 'wrong birthdate format (needs YYYY-MM-DD)', 422

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
        if request.content_type == 'application/json':
            if 'id' in request.json and request.json['id'] != '':
                users = query_db("SELECT * FROM users WHERE id = ?",
                                 cur, (request.json['id'],))
                return users
            return 'no id', 400
        users = query_db("SELECT * FROM users", cur)
        return users
    except Exception as err:
        return str(err), 500
    finally:
        cur.close()


@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):
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
        res = query_db("SELECT case when ? = password then true else false end auth, id FROM users WHERE username = ?",
                       cur, (md5(str(request.json['password']).encode('utf-8')).hexdigest(), request.json['username']), True)
        if len(res) == 0:
            return 'no such user', 412
        if not res[0]['auth']:
            return 'wrong password', 401
        res = query_db("UPDATE users SET status = 'online' WHERE id = ?",
                       cur, (res[0]['id'], ), True)
        return 'successful'
    except Exception as err:
        return str(err), 500
    finally:
        cur.close()

# Music


@app.route('/api/music', methods=['POST'])
def create_music():
    cur = get_db_connection()

    try:

        r = re.compile('\d\d\d\d-\d\d\-\d\d')

        if 'title' not in request.json or request.json['title'] == '':
            return 'no title', 400
        elif 'releaseDate' not in request.json or request.json['releaseDate'] == '':
            return 'no release date', 400
        elif 'album' not in request.json or request.json['album'] == '':
            return 'no album', 400
        elif 'artist' not in request.json or request.json['artist'] == '':
            return 'no artist', 400
        elif r.match(request.json['releaseDate']) is None:
            return 'wrong release date format (needs YYYY-MM-DD)', 422

        newid = query_db('INSERT INTO music (title, release_date, artist, album) \
                            VALUES (?, date(?), ?, ?) RETURNING id', cur, (request.json['title'],
                                                                           request.json['releaseDate'],
                                                                           request.json['artist'],
                                                                           request.json['album']), True)

        return newid
    except Exception as err:
        return str(err), 500
    finally:
        cur.close()


@app.route('/api/music', methods=['GET'])
def get_music():
    cur = get_db_connection()

    try:
        if request.content_type == 'application/json':
            if 'id' in request.json and request.json['id'] != '':
                music = query_db("SELECT * FROM music WHERE id = ?",
                                 cur, (request.json['id'],))
                return music
            return 'no id', 400
        music = query_db("SELECT * FROM music", cur)
        return music
    except Exception as err:
        return str(err), 500
    finally:
        cur.close()


@app.route('/api/music/<int:id>', methods=['PUT'])
def update_music(id):
    cur = get_db_connection()

    try:
        for k, v in request.json.items():
            if k not in ('title', 'album', 'artist'):
                return 'wrong params to update', 422
            elif v == '':
                return 'value is empty', 422

            res = query_db("UPDATE music SET " + k + " = ? WHERE id = ? RETURNING id",
                           cur, (v, id), True)

            if len(res) == 0:
                return 'no such music', 412

        return 'successful'
    except Exception as err:
        return str(err), 500
    finally:
        cur.close()


@app.route('/api/music/<int:id>', methods=['DELETE'])
def delete_music(id):
    cur = get_db_connection()

    try:
        res = query_db("DELETE FROM music WHERE id = ? RETURNING id",
                       cur, (id, ), True)
        if len(res) == 0:
            return 'no such music', 412
        return 'successful'
    except Exception as err:
        return str(err), 500
    finally:
        cur.close()


@app.route('/api/music/listen', methods=['POST'])
def listen_music():
    cur = get_db_connection()

    if 'data' not in request.json or request.json['data'] == '':
        return 'no data', 400
    try:
        res = query_db("SELECT id FROM music WHERE lower(title||coalesce(album, '')||coalesce(artist, '')) like lower('%" + request.json['data'] + "%') limit 1",
                       cur)
        if len(res) == 0:
            return 'no such music', 412

        id = res[0]['id']

        res = query_db("UPDATE music SET listen_amount = listen_amount + 1 WHERE id = ? RETURNING id",
                       cur, (id,), True)
        return 'Mmm... Sounds nice'
    except Exception as err:
        return str(err), 500
    finally:
        cur.close()


@app.route('/api/iamteapot', methods=['GET'])
def i_am_teapot():
    return 'Enjoy your tea', 418
