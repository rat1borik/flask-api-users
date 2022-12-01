create table if not exists users(
    id integer primary key autoincrement,
    dt datetime not null default (datetime('now','localtime')),
    username varchar(20) not null unique check(length(username) > 5),
    password blob not null,
    email varchar(100),
    status varchar(100) default 'online',
    birthdate date not null
)