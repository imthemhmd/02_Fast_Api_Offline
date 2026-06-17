In this project, we created an API using fastapi.
Endpoints defined in this project through which a client can access a server and perform an operation.
In this project, you will create your own database file by running 
getting it.
EndPoint /: This endpoint is the root path.
EndPoint /insert_record_db/: In this endpoint, you can add a video to the database with the information you want.
EndPoint /insert_record_by_apiid_db/: In this endpoint, you can get information about a movie by ID and store it in your database.
EndPoint /insert_record_by_apimoviename_db/{movie_name}: In this endpoint, you can get information about a movie by movie name and save it in your database.
EndPoint /select_all_record_db/: In this endpoint you can see the details of all the movies in your database.
EndPoint /select_record_by_movieid_db/{movie_id}: In this endpoint you can see all the information about a movie in your database.
EndPoint /update_record_by_movieid_db/{movie_id}: In this endpoint, you can change the country items and movie rating by entering a movie ID.
EndPoint /delete_record_by_movieid_db/: In this endpoint, you can completely delete all information about a movie in the database by entering its ID.
