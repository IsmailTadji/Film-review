# Film-review

### Application functionalities:

- User can register an account, log in and log out.
- User can add films to the application
- User can review added films.
- User can view other users film reviews.

## Välipalautus 2 review:
- Application UI is barebones with minimal bootstrap.
- User is able to Register, however username and password verification is not done.
- User is able to Log In.
- User is able to add a film review to the application, so far its on a 0-10 rating.
- User is able to view film ratings that were made by him and other users.

## Running the application
- Currently the application can only be ran locally with the follwing steps:

1. Clone the repository and create a .env file in its root folder with following variables:
- ```DATABASE_URL```: URL to your PostgreSQL database
- ```SECRET_KEY```: Flask app secret key

2. Create a virtual environment and install dependencies in the root folder:
```
python3 -m venv venv
source venv/bin/activate
pip install -r ./requirements.txt
```
3. Create the database with the following command:
```psql < schema.sql```

4. Run the application:
```python3 src/app.py```
