
# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"
#songplay_table_drop = "DROP TABLE IF EXISTS songplays"
# CREATE TABLES



songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays(
songplay_id serial CONSTRAINT songplay_pk PRIMARY KEY ,
start_time timestamp NOT NULL REFERENCES time (start_time) ,
user_id int NOT NULL REFERENCES users (user_id),
level varchar NOT NULL ,
song_id varchar  REFERENCES songs (song_id),
artist_id varchar  REFERENCES artists (artist_id) ,
session_id int NOT NULL ,
location text,
user_agent text
)""")
#start_time timestamptz CONSTRAINT time_pk PRIMARY KEY REFERENCES songplays (start_time),
#time_table_create = (""" CREATE TABLE IF NOT EXISTS time(
#start_time timestamp CONSTRAINT time_pk PRIMARY KEY ,
#hour int NOT NULL,
#day int NOT NULL,
#week int NOT NULL,
#month int NOT NULL,
#year int NOT NULL,
#weekday varchar NOT NULL
#)
#""")

user_table_create = (""" CREATE TABLE IF NOT EXISTS users(
user_id int CONSTRAINT user_pk PRIMARY KEY ,
first_name varchar,
last_name varchar,
gender varchar,
level varchar NOT NULL
)
""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists(
artist_id varchar CONSTRAINT artist_PK PRIMARY KEY NULL ,
name varchar NOT NULL,
location text,
latitude double precision,
longitude double precision
)
""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS songs(
song_id varchar CONSTRAINT song_pk PRIMARY KEY ,
title varchar NOT NULL,
artist_id varchar NOT NULL,
year integer CHECK (year >= 0),
duration numeric NOT NULL
)
""")


time_table_create = (""" CREATE TABLE IF NOT EXISTS time(
start_time timestamp CONSTRAINT time_pk PRIMARY KEY ,
hour int NOT NULL,
day int NOT NULL,
week int NOT NULL,
month int NOT NULL,
year int NOT NULL,
weekday varchar NOT NULL
)
""")

#start_time timestamptz REFERENCES time (start_time) ,
#songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays(
#songplay_id int CONSTRAINT songplay_pk PRIMARY KEY ,
#start_time timestamptz  ,
#user_id int NOT NULL ,
#level int,
#song_id int NOT NULL ,
#artist varchar NOT NULL ,
#session_id int NOT NULL ,
#location text,
#user_agent text
#)
#""")

# INSERT RECORDS
#
songplay_table_insert = (""" INSERT INTO songplays (
    start_time, user_id, level, song_id, artist_id, 
    session_id, location, user_agent) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)    
    ON CONFLICT (songplay_id) DO NOTHING;
""")
#
user_table_insert = (""" INSERT INTO users 
    (user_id, first_name, last_name, gender, level)    
    VALUES (%s, %s, %s, %s, %s)    
    ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;
""")
#
song_table_insert = (""" INSERT INTO songs 
    (song_id, title, artist_id, year, duration)    
    VALUES (%s, %s, %s, %s, %s)    
    ON CONFLICT  DO NOTHING;
""")
#
artist_table_insert = (""" INSERT INTO artists 
    (artist_id, name, location, latitude, longitude)    
    VALUES (%s, %s, %s, %s, %s)    
    ON CONFLICT  DO NOTHING;
""")
#
time_table_insert = (""" INSERT INTO time 
    (start_time, hour, day, week, month, year, weekday)    
    VALUES (%s, %s, %s, %s, %s, %s, %s)    
    ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = (""" SELECT song_id, artists.artist_id
    FROM songs JOIN artists ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s
    AND artists.name = %s
    AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [ user_table_create,song_table_create,artist_table_create,  time_table_create,songplay_table_create]
drop_table_queries = [ user_table_drop, song_table_drop,artist_table_drop, time_table_drop ,songplay_table_drop]