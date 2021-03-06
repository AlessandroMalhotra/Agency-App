# Capstone
Agency App

# Capstone Project - Casting Agency

This is the capstone project for the Udacity Full Stack Nanodegree program. 
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. The agency employs a casting assistant, casting director and an executive producer who all have different roles / permissions in the agency.

# Motivation
With this app i could really demonstrate all the skills i learned throughout the Udacity course and really binded all of the learning together. Builing this app from scratch really instiled complex topics and I feel very competent in building apps on my own in the future.

### URLs

Casting Agency URL: https://agency-application.herokuapp.com/
Heroku GitHub repository: https://git.heroku.com/agency-application.git

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once the virtual environment is setup and running, install dependencies by navigating to the working project directory and running:

```bash
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM used to handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension used to handle cross origin requests. 

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run -h localhost -p 5001
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to application `app.py`. 

## Authentication

### Casting Assistant
A casting assistant is the lowest level of authority and is only permitted to view actors and movies.

#### Permissions:
```bash
get:actors | get:movies
```
#### Login details:
```bash
email: alesssandro2@icloud.com
password: Mrgentleman1
```

### Casting Director
A casting director mid-level authority and is permitted to view actors and movies as well as deleting an actor or adding an actor in the database and lastly, modifying actors and movies.

#### Permissions:
```bash
get:actors    | get:movies 
delete:actors | delete:movies
post:actors   | post:movies
```
#### Login details:
```bash
email: alessandro4926@gmail.com
password: Mrgentleman1
```

### Executive Producer
The executive producer is the highest level of authority and is permitted to do any of the actions across the application.

#### Permissions:
```bash
get:actors    | get:movies 
delete:actors | delete:movies 
post:actors   | post:movies
patch:actors  | patch:movies
```
#### Login details:
```bash
email: alessandro244@outlook.com
password: Mrgentleman1
```

## Endpoints

GET '/movies'
- First checks that the token provided is allowed to perform this operation. If authorized, then fetches a dictionary of movies.
- Request Arguments: token
- Returns: Each object in the movies dictionary and an object showing the total number of movies. 
```bash
{
    "movies": [
        {
            "id": 1,
            "release_date": "2007",
            "title": "Fast and Furious Tokyo Drift"
        },
        {
            "id": 2,
            "release_date": "2012",
            "title": "Fast and Furious 5"
        },
        {
            "id": 3,
            "release_date": "1999",
            "title": "Shawshank Redemption"
        }
    ],
    "success": true
}
```

GET '/actors'
- First checks that the token provided is allowed to perform this operation. If authorized, then fetches a dictionary of actors.
- Request Arguments: token
- Returns: Each object in the actors dictionary and an object showing the total number of actors. 
```bash
{
    "actors": [
        {
            "age": 53,
            "gender": "male",
            "id": 1,
            "movies_id": 1,
            "name": "Vin Diesal"
        },
        {
            "age": 43,
            "gender": "male",
            "id": 2,
            "movies_id": 2,
            "name": "Paul Walker"
        }

    ],
    "success": true
}
```

DELETE '/movies/<int:id>/delete'
- First checks that the token provided is allowed to perform this operation. If authorized, then takes in a movie ID, if the movie exists, then it is deleted from the database
- Request Arguments: token, movie_id 
- Returns: The ID of the deleted movie and each object in the list of modified movies and an object showing the total number of movies.
```bash
{
    "id": 1,
    "success": true,
}
```

DELETE '/actors/<int:id>/delete'
- First checks that the token provided is allowed to perform this operation. If authorized, then takes in a actor ID, if the actor exists, then it is deleted from the database
- Request Arguments: token, actor_id 
- Returns: The ID of the deleted actor and each object in the list of modified actors and an object showing the total number of actors.
```bash
{
    "id": 1,
    "success": true,
}
```

POST '/movies/create'
- First checks that the token provided is allowed to perform this operation. If authorized, then takes in an object with key value pairs for the new movie namely the title and release_date. 
- Request Arguments: token
- Returns: An object containing the newly created movie's id, each object in the list of modified movies and an object showing the total number of movies.
```bash
{
    "new_movie": [
        {
            "id": 4,
            "release_date": "1997",
            "title": "Lion King"
        }
    ],
    "success": true
}
```

POST '/actors/create'
- First checks that the token provided is allowed to perform this operation. If authorized, then takes in an object with key value pairs for the new actor namely the name, age and gender. 
- Request Arguments: token
- Returns: An object containing the newly created actors's id, each object in the list of modified actors and an object showing the total number of actors.
```bash
{
    "new_actor": [
        {
            "age": 43,
            "gender": "male",
            "id": 2,
            "movies_id": 2,
            "name": "Paul Walker"
        }
    ],
    "success": true
}
```

PATCH '/movies/<int:id>/update'
- First checks that the token provided is allowed to perform this operation. If authorized, then takes in an object with key value pairs for the desired fields to be changes. 
- Request Arguments: token, movie_id
- Returns: An object containing the updated movie.
```bash
{
    "movies": [
        {
            "id": 3,
            "release_date": "1996",
            "title": "Shawshank Redemption"
        }
    ],
    "success": true
}
```

PATCH '/actors/<int:id>/update'
- First checks that the token provided is allowed to perform this operation. If authorized, then takes in an object with key value pairs for the desired fields to be changes. 
- Request Arguments: token, actor_id
- Returns: An object containing the updated actor.
```bash
{
    "success": true,
    "updated_actor": [
        {
            "age": 44,
            "gender": "male",
            "id": 2,
            "movies_id": 2,
            "name": "Paul Walker"
        }
    ]
}
```
