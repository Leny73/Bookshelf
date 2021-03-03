# Bookshelf App
Back-end Application developed in Python using Flask, SQLAlchemy with a RESTful API, Unit Tests and API tests for Udacity Course in API Development and Documentation
## Getting Started
This is a simple Back-End application to store Books.
To run API tests just run test_flaskr.py file with python.
Example: <code>python3 test_flaskr.py</code> 
To start the application clone the Github repository. Open the project directory and set up Flask environment in a terminal execute the following commands:
<br/>
<code>
export FLASK_ENV = development
export FLASK_APP = flaskr
</code>
</br>
<code>
flask run
</code>

Make sure you have flask installed to be able to host this project locally. After typing this into terminal you should be running the flask app
on port http://127.0.0.1:5000/ and see a message in the terminal: 
<section>
 * Environment: development <br>
 * Debug mode: on <br>
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)<br>
 * Restarting with stat<br>
 * Debugger is active!<br>
 * Debugger PIN: 473-405-251<br>
</section>
This version of the application does not contain any Authentication.
# Api Reference
## Error Handling
Errors are returned as JSON objects in the following format: 
<code>
{
  "success": False,
  "error": 400,
  "message": "Bad request!"
}
</code>

The API will retern three error types when requests fail:

<section>
 * 400: Bad Request! <br>
 * 404 Resource Not Found <br>
 * 422 Not Processable<br>
</section> 

## Endpoints
GET /books
- Returns a list of book objects, value of success and a total number of books
- Results are paginated in groups of 8. Include a request argument to choose page number, starting from 1.
* Sample : In terminal with curl installe type: <code>curl http://127.0.0.1:5000/books</code>
* Sample Response : <code> {
  "books": [
    {
      "author": "Petar Deunov", 
      "id": 1, 
      "rating": 10, 
      "title": "Paneurythmy"
    }, 
    {
      "author": "Petar Deunov", 
      "id": 3, 
      "rating": 10, 
      "title": "The two ways"
    }, 
    {
      "author": "Nikolay Doinov", 
      "id": 5, 
      "rating": 10, 
      "title": "Astrology"
    }
  ], 
  "success": true, 
  "total": 3
}
</code>
POST /books
- General:
 - Creates a new book using the submitted title, author and rating. Return the id of the created book, success value, total vooks and book list based on current page number to update.
 - Example: <code> curl http://127.0.0.1:5000 -X POST -H "Content-Type: application/json" -d '{"title":"Masons", "author":"Jean Palu", "rating":"5"}'</code>
 - Example response: <code> {
  "books": [
    {
      "author": "Petar Deunov", 
      "id": 1, 
      "rating": 10, 
      "title": "Paneurythmy"
    }, 
    {
      "author": "Petar Deunov", 
      "id": 3, 
      "rating": 10, 
      "title": "The two ways"
    }, 
    {
      "author": "Nikolay Doinov", 
      "id": 5, 
      "rating": 10, 
      "title": "Astrology"
    }, 
    {
      "author": "Jean Palu", 
      "id": 6, 
      "rating": 5, 
      "title": "Masons"
    }
  ], 
  "created": 6, 
  "success": true, 
  "total_books": 4
}
</code>
DELETE /books/{book_id}
- General:
 - Deletes a selected book id. Returns books, success value, total length and deleted id.
 - Example: <code> curl -X DELETE http://127.0.0.1:5000/books/6</code>
 - Example Response: <code> {
  "books": [
    {
      "author": "Petar Deunov", 
      "id": 1, 
      "rating": 10, 
      "title": "Paneurythmy"
    }, 
    {
      "author": "Petar Deunov", 
      "id": 3, 
      "rating": 10, 
      "title": "The two ways"
    }, 
    {
      "author": "Nikolay Doinov", 
      "id": 5, 
      "rating": 10, 
      "title": "Astrology"
    }
  ], 
  "deleted": 6, 
  "success": true, 
  "total_books": 3
}
</code>
PATCH /books/{book_id}

- General:
 - If provided, updates rating of the specific book_id. Return success value and id of the updated Book.
 - Example: <code> curl -X PATCH http://127.0.0.1:5000/books/5 -H "Content-Type: application/json" -d '{"rating":"11"}'
 - Example Response: <code> {
  "id": 5, 
  "success": true
}
  </code>




