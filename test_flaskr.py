# Import all dependencies
import unittest
import json
from __init__ import create_app
from models import setup_db, Book


class ResourceTestCase(unittest.TestCase):
    """This class represents the resource test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "test_db"
        self.database_path = "postgres://{}:{}@{}/{}".format('lyuben', 'temp123!','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
    
        self.new_book = {
            'title': 'Time and Power',
            'author': 'Petar Deunov',
            'rating': 5
        }
    def tearDown(self):
        """Executed after each test"""
        pass

    def test_get_paginated_books(self):
        res = self.client().get('/books')
        print(res.data)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total'])
        self.assertTrue(len(data['books']))
    
    def test_404_send_requesting_beyond_valid_page(self):
        res = self.client().get('/books?page=1000', json={'rating': 1})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found!')

    def test_update_book_rating(self):
        res = self.client().patch('/books/1', json={'rating': 1})
        data = json.loads(res.data)
        book = Book.query.filter(Book.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(book.format()['rating'], 1)
    
    def test_400_for_failed_update(self):
        res = self.client().patch('/books/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Bad request!")

    def test_delete_book(self):
        res = self.client().delete('/books/7')
        data = json.loads(res.data)

        book = Book.query.filter(Book.id == 7).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 7)
        self.assertTrue(data['total_books'])
        self.assertTrue(len(data['books']))
        self.assertEqual(book, None)

    def test_404_if_book_does_not_exist(self):
        res = self.client().delete('/books/100')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Unprocessable!")

    def test_create_book(self):
        res = self.client().post('/books', json=self.new_book)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['books']))

    def test_405_if_books_creating_not_allowed(self):
        res = self.client().post('/books/45', json=self.new_book)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Method not allowed!")
    
    def test_search(self):
        res = self.client().post('/books', json={'search': 'Time and Power'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_books'])
        self.assertEqual(len(data['books']), 5)

    def test_search_fail(self):
        res = self.client().post('/books', json={'search': 'Poggies'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_books'], 0)
        self.assertEqual(len(data['books']), 0)





    
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()