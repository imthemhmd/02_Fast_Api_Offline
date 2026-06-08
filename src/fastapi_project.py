# Welcome To My Project Fast Api Offline
# In this file, we want to integrate fastapi 
# with the database and api.


# imports
from fastapi_offline import FastAPIOffline
import db

# Fixed Variable
app = FastAPIOffline()

# Root Path
@app.get('/')
def home():
    return "Home Root"

@app.post('/insert_record_db/')
def insert_record(movie_name:str, country:str, year:int, imdb_rating:float):
    db.insert_record_db(movie_name, country, year, imdb_rating)
    return f"Movie {movie_name} Successfuly Add To DB"

@app.post('/insert_record_by_apiid_db/')
def insert_record_apiid(movie_id:int):
    result = db.insert_record_by_apiid_db(movie_id)
    if result == "Error":
        return f"Not Found Movie ID {movie_id}"
    else:
        return f"Add Movie Id {movie_id} Successfuly To DB"

@app.post('/insert_record_by_apimoviename_db/{movie_name}')
def insert_record_apimoviename(movie_name:str):
    result = db.insert_record_by_apimoviename_db(movie_name)
    if result == "Error":
        return f"Not Found Movie Name {movie_name}"
    else:
        return  F"Add Movie Name {movie_name} Successfuly To DB"
    
@app.get('/select_all_record_db/')
def select_all_record():
    result = db.select_all_record_db()
    return result

@app.get('/select_record_by_movieid_db/{movie_id}')
def select_record_by_movieid(movie_id:int):

    result = db.select_record_by_movieid_db(movie_id)
    if not result:
        return f"Not Found Movie {movie_id}"
    else:
        return result

@app.put("/update_record_by_movieid_db/{movie_id}")
def update_record_by_movieid(movie_id:int, country:str, imdb_rating:float):
    result = db.update_record_by_movieid_db(movie_id, country, imdb_rating)
    if result == "Error":
        return f"Not Found Movie Id {movie_id}"
    else:
        return f"Movie Id {movie_id} Update Successfuly"

@app.delete("/delete_record_by_movieid_db/")
def delete_record_by_movieid(movie_id:int):

    result = db.delete_record_by_movieid_db(movie_id)
    if result == "Error":
        return f"Not Found Movie Id {movie_id}"
    else:
        return f"Movie Id {movie_id} Delete Successfuly"
    
