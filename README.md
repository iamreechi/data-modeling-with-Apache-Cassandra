Data Modeling with Postgres & ETL Pipeline for Sparkify

Table of Content 
Required Libraries for installation
 
Project Summary 

File Overview/ Description

 
ETL Process 
 
Usage 
 
Fact and Dimension Tables 
 
Acknowledgement 

Required Libraries for installation
To be able to perform all the task in the different phases, Python should be installed with the following libraries
pandas
psycopg2
sql_queries

Project Summary 
Sparkify is a music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, their data resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. However, this cannot provide an easy way to query the data.
The goal of this project is to build a PostgreSQL database utilizing the data on users activity and songs metadata. Building the database helps us do complex analytics regarding users activity as well as song play analysis to help Sparkify's analytics team.

File overview/ description
data/song_data/ - contains our song data in json format. files are partitioned by the first three letters of each song's track ID
data/log_data/ - contains our user activity logs in json format. files are partitioned by year and month
sql_queries.py - states all of our SQL queries for: droping tables, creating tables, inserting rows, and a query for finding song_id, artist_id given a song name, artist name, and song duration
create_tables.py - Python script that drops and then creates our tables.
etl.py - Our ETL pipeline. Iterates through our song and log files and pipes the data into our database tables.
test.ipynb - Runs SQL queries to check the first few values of each of our database tables.
etl.ipynb - Exploratory work that can be used to look at our json files and test various etl approaches for getting data from the json files into our databases

Be sure to close all database connections and run create_tables.py before running etl.py or etl.ipynb.

After Running either of those etl files, you can run test.ipynb to check the values of each of our database tables.


ETL Processes
The summary of ETL processes is below. For more details, see etl.ipynb, etl.py and sql_queries.py.

Songs metadata
#1: songs table
Parse and read a song JSON file by using pandas.read_json function.
Select columns for song ID, title, artist ID, year, and duration from dataframe.
Execute an insert query to songs table in PostgreSQL.
If the song ID confliction is occured, do nothing.
Repeat the process iterably for all songs data.

#2: artists table
Parse and read a song JSON file by using pandas.read_json function.
Select columns for artist ID, name, location, latitude, and longitude from dataframe.
Execute an insert query to artists table in PostgreSQL.
If the artist ID confliction is occured, do nothing.
Repeat the process iterably for all songs data.

User activity logs
#3: time table
Parse and read a JSON file of user activity log by using pandas.read_json function.
Filter records by NextSong action.
Convert the ts timestamp column to datetime.
Extract the timestamp, hour, day, week of year, month, year, and weekday from dataframe.
Execute an insert query to time table in PostgreSQL.
Repeat the process iterably for all log files.

#4: users table
Parse and read a JSON file of user activity log by using pandas.read_json function.
Filter records by NextSong action.
Select columns for user ID, first name, last name, gender and level from dataframe.
Execute an insert query to songs table in PostgreSQL.
If the user ID confliction is occured, Update value of level on the recored.
Repeat the process iterably for all log files.

#5: songsplays table
Parse and read a JSON file of user activity log by using pandas.read_json function.
Filter records by NextSong action.
Select the timestamp, user ID, level, song ID, artist ID, session ID, location, and user agent from dataframe.
Log files don't include song ID and artist ID, so get these ID by executing select query to songs and artists tables.
Execute an insert query to songs table in PostgreSQL.
Repeat the process iterably for all log files.

Usage
Create tables and execute ETL.
%run -i "create_tables.py"
%run -i "etl.py"

To check the databse present 
!echo "\l" | sudo -u postgres psql

create sparkifydb if not available 
!echo "create database sparkifydb" | sudo -u postgres psql

Fact and Dimension Tables
Facts Table: songplays
Dimension Table:users, songs, artists and time 

All this was done for the sole purpose to help the Sparkify's analytics team carry out analysis of the users of the app such as 
Top 10 most listened to song 
know the number of users based on a particular time 
Who are our most active users, are they paying users or not 
What's the most active day of the week for users

Acknowledgement
I wish to thank Udacity for advice and review