import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "test_db"
        self.database_path = "postgresql://{}:{}@{}/{}".format('ayodeji', 'ayodeji','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            "question": "What are you passionate about?",
            "answer": "Software Engineering",
            "difficulty": 5,
            "category": 1
        }

        self.search_term = {"searchTerm": "passion"}

        self.category_1 = Category(type='Tech')
        self.category_2 = Category(type='Science')

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass
        

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_add_categories(self):

        # Add categories to database
        with self.app.app_context():
            self.db.session.add_all([self.category_1, self.category_2])
            self.db.session.commit()

    def test_add_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question_id'])

    def test_400_add_question_with_not_allowed_schema(self):
        res = self.client().post('/questions', json={
            "question": "What are you passionate about?",
            "answer": "Cooking",
            "difficulty": 3,
            "category": 1,
            "searchTerm": "set"
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_400_add_question_with_invalid_schema(self):
        res = self.client().post('/questions', json={
            "question": "What is your name?"
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_search_question(self):
        res = self.client().post('/questions', json=self.search_term)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])

    def test_400_search_question_empty_body(self):
        res = self.client().post('/questions', json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')


    def test_retrieve_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_categories'])

    def test_retrieve_questions(self):
        res = res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['categories'])

    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get('/questions?page=10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
        

    def test_delete_questions(self):
        res = self.client().post('/questions', json=self.new_question)
        question_id = json.loads(res.data)['question_id']

        res = res = self.client().delete(f'/questions/{question_id}')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_delete_question_with_invalid_id(self):
        res = res = self.client().delete('/questions/10000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')


    def test_get_questions_by_category_id(self):
        category_id = self.new_question['category']
        res = self.client().get(f'categories/{category_id}/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])

    def test_get_random_question_quizzes(self):
        res = res = self.client().post('/quizzes', json={
            "previous_questions": [],
            "quiz_category": {"id":1}
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['question']['question'], "What are you passionate about?")
        self.assertTrue(data['question']['category'])
        self.assertEqual(data['question']['answer'], "Software Engineering")

    def test_422_get_random_question_with_invalid_id(self):
        res = res = self.client().post('/quizzes', json={
            "previous_questions": [],
            "quiz_category": {"id":100000}
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "unprocessable")

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()