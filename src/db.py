# Welcome To My Project Fast Api Offline
# In this file, we want to create the project database.


# imports
import sqlite3 
import requests_api


# Fixed Variabels
DB_NAME = "Movies.db"

# Function Create DB
def init_db():
    # This function creates a raw database.
    
    with sqlite3.connect(DB_NAME) as conn:
        pass
init_db()

# Function Create Table DB
def create_table():
    # In this function, three columns 
    # are created for the database.
    # columns(id, title, country, year, imdb_rating)

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        query = '''
        Create Table If Not Exists Movies
        (
        Id Integer Primary Key Autoincrement,
        Title Text,
        Country Text,
        Year Integer,
        Imdb_Rating Real
        )
        '''
        cursor.execute(query)
create_table()

# Function Insert Record To DB
def insert_record_db(title:str, country:str, year:int, imdb_rating:float):
    # With this function, we can add a movie to the database.

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        query = '''
        Insert Into Movies(Title, Country, Year, Imdb_Rating)
        Values(?,?,?,?)
        '''
        cursor.execute(query, (title, country, year, imdb_rating))


# Function Insert Record By API Id To DB
def insert_record_by_apiid_db(movie_id:int):
    # With this function, we get the information of 
    # a movie through the API ID and put it into the database.

    result = requests_api.requests_id(movie_id)
    if result == None:
        return "Error"
    else:
        title, country, year, imdb_rating = result
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            query = '''
            Insert Into Movies(Title, Country, Year, Imdb_Rating)
            Values(?,?,?,?)
            '''
            cursor.execute(query, (title, country, year, imdb_rating))
    
# Function Insert Record By API Movie Name To DB
def insert_record_by_apimoviename_db(movie_name:str):
    # With this function, we get the information about 
    # a movie through the moviename API and put it into the database.
    result = requests_api.requests_moviename(movie_name)
    if result == None:
        return "Error"
    else:
        title, country, year, imdb_rating = result
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            query = '''
            Insert Into Movies(Title, Country, Year, Imdb_Rating)
            Values(?,?,?,?)
            '''
            cursor.execute(query, (title, country, year, imdb_rating))


# Functio Select All Record DB
def select_all_record_db():
    # With this function, we can see all the database information.

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        query = '''
        Select *
        From Movies
        '''
        result = cursor.execute(query).fetchall()
        return result

# Function Select Record By ID Movie
def select_record_by_movieid_db(movie_id:int):
    # With this function, we can see all the 
    # information about the desired movie ID.

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        query = '''
        Select *
        From Movies
        Where Id=?
        '''
        result = cursor.execute(query, (movie_id,)).fetchall()
        return result

# Function Update Record By Movie ID
def update_record_by_movieid_db(movie_id:int, country:str, imdb_rating:float):
    # With this function, we can update the pull 
    # and rating columns via the movie ID.

    result = select_record_by_movieid_db(movie_id) # Checks if an ID exists or not.
    if not result:
        return "Error"
    else:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            query = '''
            Update Movies
            Set Country=?, Imdb_Rating=?
            Where Id=?
            '''
            cursor.execute(query, (country, imdb_rating, movie_id))

# Function Delete Record By Movie ID
def delete_record_by_movieid_db(movie_id:int):
    # With this function, we can 
    # delete a movie via its movie ID.

    result = select_record_by_movieid_db(movie_id) # Checks if an ID exists or not.
    if not result:
        return "Error"
    else:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            query = '''
            Delete From Movies
            Where Id=?
            '''
            cursor.execute(query, (movie_id,))
