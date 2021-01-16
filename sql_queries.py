# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS  time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(
                        songplay_id SERIAL PRIMARY KEY,
                        start_time TIMESTAMP NOT NULL,
                        level varchar NOT NULL,
                        song_id varchar,
                        artist_id varchar,
                        session_id int NOT NULL,
                        location varchar,
                        userAgent varchar,
                        user_id int NOT NULL)
            
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users(
                    user_id int NOT NULL PRIMARY KEY,
                    firstName varchar NOT NULL,
                    lastName varchar NOT NULL,
                    gender varchar,
                    level varchar NOT NULL,
                    UNIQUE(user_id ))                
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(
                    artist_id varchar NOT NULL,
                    duration numeric NOT NULL,
                    song_id varchar NOT NULL PRIMARY KEY,
                    title varchar NOT NULL,
                    year int)
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(
                       artist_id varchar NOT NULL PRIMARY KEY,
                       artist_name varchar NOT NULL,
                       artist_location varchar, 
                       artist_latitude numeric, 
                       artist_longitude numeric)
                
                       
                    
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(
                    start_time TIMESTAMP NOT NULL PRIMARY KEY,
                    year int NOT NULL,
                    month int NOT NULL, 
                    day int NOT NULL, 
                    hour int NOT NULL, 
                    weekofyear int NOT NULL,
                    dayofweek int NOT NULL,
                    UNIQUE(start_time))
            
                    
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays(start_time,level,song_id,artist_id,session_id,location,userAgent,user_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
""")
user_table_insert = ("""INSERT INTO users(user_id,firstName,lastName,gender,level) 
                    VALUES (%s,%s,%s,%s,%s) ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

song_table_insert = ("""INSERT INTO songs(artist_id,duration,song_id,title,year) \
                     VALUES (%s,%s,%s,%s,%s)""")
#
artist_table_insert = ("""INSERT INTO artists(artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
                       VALUES (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING 
""")


time_table_insert = ("""INSERT INTO time(start_time,year,month,day,hour,weekofyear,dayofweek) \
                    VALUES (%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = ("""SELECT songs.song_id, artists.artist_id FROM songs JOIN artists ON songs.artist_id = artists.artist_id 
               WHERE artists.artist_name = %s AND songs.title = %s AND songs.duration = %s;""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]