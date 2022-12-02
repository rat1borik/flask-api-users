# flask-api-users

All queries available with ThunderClient extension for VSCode by importing from file 
https://github.com/rat1borik/flask-api-users/blob/master/thunder-collection_flask-api-example.json

## Users API

### User Adding

POST 127.0.0.1:3005/api/users
```
{
  "username":"y.rybnikov1934",
  "password":"shizofaziya332",
  "birthdate":"1934-12-31",
  "status":"online",
  "email":"shiza@aye.com"
}
```
![image](https://user-images.githubusercontent.com/101923002/205243286-fb38880f-1c4b-4cff-8831-4e3e528d02e8.png)

Status: 200 OK
Size: 24 Bytes
Time: 21 ms
```
[
  {
    "id": 2
  }
]
```
  - User Adding exception

![image](https://user-images.githubusercontent.com/101923002/205244206-5c9d8bbe-ef5b-4e50-9668-5f5ee6208467.png)

### User Modifying

PUT 127.0.0.1:3005/api/users/2
```
{
    "status":"busy"
}
```
![image](https://user-images.githubusercontent.com/101923002/205244399-2c4d3d9e-9eb8-4509-a00c-f1e7e188071e.png)

Status: 200 OK
Size: 10 Bytes
Time: 9 ms

successful

  - User Modifying exception

![image](https://user-images.githubusercontent.com/101923002/205244487-64a45ccc-956b-425d-87e3-129cca9ced4b.png)

### User Deleting

DELETE 127.0.0.1:3005/api/users/1

![image](https://user-images.githubusercontent.com/101923002/205244649-b6ea5067-0a8d-4d48-b0fa-ec6b0ed95aa3.png)

Status: 200 OK
Size: 10 Bytes
Time: 7 ms

successful

  - User Deleting exception

![image](https://user-images.githubusercontent.com/101923002/205244718-e706c2a2-9c89-4120-986c-d8abe8779e3d.png)

### Users Viewing

GET 127.0.0.1:3005/api/users

![image](https://user-images.githubusercontent.com/101923002/205245011-d4d2e71a-ea0b-4d82-a859-7c3be1c248d6.png)

Status: 200 OK
Size: 226 Bytes
Time: 11 ms

```
[
  {
    "birthdate": "1934-12-31",
    "dt": "2022-12-02 11:02:47",
    "email": "shiza@aye.com",
    "id": 2,
    "password": "93cf9e2a0644bb4a79c2c9e8cf04289d",
    "status": "busy",
    "username": "y.rybnikov1934"
  }
]
```

### User Viewing

GET 127.0.0.1:3005/api/users
```
{
  "id":2
}
```
![image](https://user-images.githubusercontent.com/101923002/205245121-3d0f4332-946d-479f-90dc-dfbd69e6b33a.png)

Status: 200 OK
Size: 226 Bytes
Time: 5 ms

```
[
  {
    "birthdate": "1934-12-31",
    "dt": "2022-12-02 11:02:47",
    "email": "shiza@aye.com",
    "id": 2,
    "password": "93cf9e2a0644bb4a79c2c9e8cf04289d",
    "status": "busy",
    "username": "y.rybnikov1934"
  }
]
```

### User Authentification

POST 127.0.0.1:3005/api/users/auth

```
{
  "username":"y.rybnikov1934",
  "password":"shizofaziya332"
}
```

![image](https://user-images.githubusercontent.com/101923002/205245288-a4c56d04-1f82-4bba-9949-31c413c15e94.png)

Status: 200 OK
Size: 10 Bytes
Time: 9 ms

successful

  - User Authentification exception

![image](https://user-images.githubusercontent.com/101923002/205245391-e96a92cf-45c9-415f-92ab-a8efcaff7656.png)

## Music API

### Music Adding

POST 127.0.0.1:3005/api/music
```
{
  "title":"Tp na ame",
    "artist":"SEREGA PIRAT OFFICIAL",
     "releaseDate":"2019-12-05",
     "album":"SomethingSheet"
}
```
![image](https://user-images.githubusercontent.com/101923002/205245893-83fd7411-ec17-4686-8c3c-e90d3220dac1.png)

Status: 200 OK
Size: 24 Bytes
Time: 8 ms
```
[
  {
    "id": 4
  }
]
```

### Music Modifying

PUT 127.0.0.1:3005/api/music/4
```
{
  "album":"World`s Classical Masterpieces"
}
```

![image](https://user-images.githubusercontent.com/101923002/205246407-30560634-c730-47a9-9caa-488318145852.png)

Status: 200 OK
Size: 10 Bytes
Time: 13 ms

successful

### Musics Viewing

GET 127.0.0.1:3005/api/music

![image](https://user-images.githubusercontent.com/101923002/205246755-7cbec686-5699-40fb-b192-7eff746a51bd.png)

Status: 200 OK
Size: 227 Bytes
Time: 10 ms
```
[
  {
    "album": "World`s Classical Masterpieces",
    "artist": "SEREGA PIRAT OFFICIAL",
    "dt": "2022-12-02 11:08:22",
    "id": 4,
    "listen_amount": 0,
    "release_date": "2019-12-05",
    "title": "Tp na ame"
  }
]
```

### Music Viewing

GET 127.0.0.1:3005/api/music
```
{
  "id":4
}
```
![image](https://user-images.githubusercontent.com/101923002/205246976-986d5c75-edc4-476d-afa9-665844c691f0.png)

Status: 200 OK
Size: 227 Bytes
Time: 5 ms
```
[
  {
    "album": "World`s Classical Masterpieces",
    "artist": "SEREGA PIRAT OFFICIAL",
    "dt": "2022-12-02 11:08:22",
    "id": 4,
    "listen_amount": 0,
    "release_date": "2019-12-05",
    "title": "Tp na ame"
  }
]
```

### Music Deleting

DELETE 127.0.0.1:3005/api/music/4

![image](https://user-images.githubusercontent.com/101923002/205247299-7b72d4d2-fe61-43a2-91a0-85cc0ffe7448.png)

Status: 200 OK
Size: 10 Bytes
Time: 13 ms

successful

### Musing Listening

POST 127.0.0.1:3005/api/music/listen
```
{
  "data":"tp%SEREGA"
}
```
![image](https://user-images.githubusercontent.com/101923002/205247630-5c4c2a51-5f0e-4942-a6db-7c7c25f94672.png)

Status: 200 OK
Size: 18 Bytes
Time: 13 ms

Mmm... Sounds nice

## Extra

I am Teapot

GET 127.0.0.1:3005/api/iamteapot

![image](https://user-images.githubusercontent.com/101923002/205247901-79d698e7-94bc-4007-8a74-3e6b0ebd09da.png)

Status: 418 I'M A TEAPOT
Size: 14 Bytes
Time: 4 ms

Enjoy your tea
