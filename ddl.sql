create table if not exists users(
    id integer primary key autoincrement,
    dt datetime not null default (datetime('now','localtime')),
    username varchar(20) not null unique check(length(username) > 5),
    password blob not null,
    email varchar(100),
    status varchar(100) default 'online',
    birthdate date not null
);

create table if not exists music(
    id integer primary key autoincrement,
    dt datetime not null default (datetime('now','localtime')),
    title varchar(50) not null,
    artist varchar(50) not null,
    album varchar(50) not null,
    listen_amount integer default 0,
    release_date date not null
)