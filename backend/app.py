from typing import Union
from fastapi import FastAPI

import pymysql

app = FastAPI()

# getters and setters


@app.get("/movies")
async def get_movies():
    connection = pymysql.connect(
        host="localhost", user="root", password="", database="crown_db"
    )
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()

    connection.close()

    return movies
