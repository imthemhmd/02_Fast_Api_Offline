# Welcome To My Project Fast Api Offline
# In this file, we send two requests to the
# site using the API via the id and movie name.
# And we extract the information from the movies.


# imports
import requests

# Function Requests  By Id
def requests_id(movie_id:int):
    # In this function, you want to send a request 
    # to the site via the ID.
    # Outputs of this function: title, country, year, imdb_rating
    url = f"https://moviesapi.ir/api/v1/movies/{movie_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    else:
        response = response.json()
        title = response['title']
        country = response['country']
        year = response['year']
        imdb_rating = response['imdb_rating']
        return title, country, year, imdb_rating
    

# Function Requests By Movie Name
def requests_moviename(movie_name:str):
    # In this function, you want to send a request
    # to the site using the movie name.
    # Outputs of this function: title, country, year, imdb_rating

    url = f"https://moviesapi.ir/api/v1/movies"
    parameters = {
        'q' : movie_name
    }
    response = requests.get(url, params=parameters)
    if response.status_code != 200:
        return None
    
    response = response.json()
    response = response.get('data', [])
    if not response:
        return None
    
    else:
        response = response[0]
        title = response['title']
        country = response['country']
        year = response['year']
        imdb_rating = response['imdb_rating']
        return title, country, year, imdb_rating
