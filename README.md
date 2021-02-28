# Bookshelf App
Back-end Application developed in Python using Flask, SQLAlchemy with a RESTful API, Unit Tests and API tests
## Introduction
This is a simple Back-End application to store Books.
To start the application clone the Github repository. Open the project directory and set up Flask environment in a terminal execute the following commands:
<br/>
<code>
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
TODO : expose all existing ednpoints to README




