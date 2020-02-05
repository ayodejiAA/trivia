# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Features

1. Enable cross-domain request.
2. Handles GET requests for questions, includes pagination(every 10 questions). This endpoint returns a list of questions, number of total questions, current      category, categories.
3. An endpoint that returns all available categories on request. 
4. An endpoint to delete question using its valid ID. 
5. Post a new question whuch includes the answer and category. 
6. An endpoint to get questions based on category.
7. A POST endpoint to get questions based on a search term. It returns any          questions for whom the search term is a substring of the question. 
8. A POST endpoint to randomly get question and answer to play quiz. 


## API Reference

```

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 

{
  '1' : "Science",
  '2' : "Art",
  '3' : "Geography",
  '4' : "History",
  '5' : "Entertainment",
  '6' : "Sports"
}



GET '/questions'
- Fetches questions including pagination (of every 10 questions). 
- Returns a list of questions, number of total questions, current category, categories. 

{
  
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },

  "questions": [
    {
      "answer": "Blue",
      "category": 1,
      "difficulty": 1,
      "id": 1,
      "question": "What color is facebook"
    },
    ...,
    ...,
    ...,
    {
      "answer": "Tel..",
      "category": 2,
      "difficulty": 3,
      "id": 10,
      "question": "Who is ...."
    }
  ],

  "success": true,
  "total_questions": 37
}


DELETE '/questions/<id>':
- Deletes question using a valid question ID.
- Returns an object

{
  'success': True
}


POST '/questions' (Create a new question):
- Creates a new question, which will require the question and answer text, 
  category, and difficulty score.
- Returns an object

{
  'success': True,
  "question_id": 30
}


POST '/questions' (Search for question with searchTerm Argument):
- Get questions based on the search term provided. 
- Returns any questions for whom the search term is a substring of the question.

{
  "questions": [
    {
      "answer": "Blue",
      "category": 1,
      "difficulty": 1,
      "id": 1,
      "question": "What color is facebook"
    },
    ...,
    ...,
    ...,
    {
      "answer": "Tel..",
      "category": 2,
      "difficulty": 3,
      "id": 10,
      "question": "What is ...."
    }
  ],
  'total_questions': 37
}


GET '/categories/<id>/questions':
- Gets questions based on category.
- ID: Category id.
- Returns object.

{
  'success': True,
  'questions': "questions": [
    {
      "answer": "Blue",
      "category": 1,
      "difficulty": 1,
      "id": 1,
      "question": "What color is facebook"
    },
    ...,
    ...,
    ...,
    {
      "answer": "Tel..",
      "category": 1,
      "difficulty": 3,
      "id": 27,
      "question": "Who is ...."
    }
  ]
  'total_questions': 10
}


POST '/quizzes':
- Endpoint to get questions to play the quiz.
- Take category and previous question parameters.
- Returns a random questions within the given category, if provided, and that is   not one of the previous questions.

{
  'success': True,
  'question':  {
      "answer": "Tel..",
      "category": 1,
      "difficulty": 3,
      "id": 27,
      "question": "Who is ...."
  }
}

```




## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
