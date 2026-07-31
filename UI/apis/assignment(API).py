## topic : library management system
from flask import Flask, request
from flask_cors import CORS
from flasgger import Swagger
from library_manager import read , read_by_id , add , update , delete
app = Flask(__name__)
CORS(app)
Swagger(app)
@app.route("/")
def home():
    """
    Home API
    ---
    responses:
      200:
        description: Ok
      404:
        description: Page not found
    """
    return "Welcome to Library Management System"
@app.route("/library", methods=["GET"])
def get_library():
    """
    Returns Library Record
    ---
    responses:
      200:
        description: Ok
      400:
        description: Bad Request
    """
    library = read()
    return library
@app.route("/library/<int:id>", methods=["GET"])
def get_library_by_id(id):
    """
    Returns Library Record Against provided Id
    ---
    parameters:
      - in: path
        name: id
        required: true
        type: integer
        description: id 
    responses:
      200:
        description: Ok
      404:
        description: Book not found
    """
    book = read_by_id(id)
    return book
@app.route("/books", methods=["POST"])
def add_book():
    """
    Adds a new book to the library
    ---
    parameters:
      - in: body
        name: book
        required: true
        schema:
          type: object
          properties:
            id:
              type: integer
            book_name:
              type: string
              description: The name of the book
            author:
              type: string
              description: The author of the book
            category:
              type: string
              description: The category of the book
            availability:
              type: string
              description: yes
    responses:
      200:
        description: Book added successfully
      400:
        description: Bad Request
    """
    book = request.get_json()
    add(book)
    
    return "book added successfully"
@app.route("/update/<int:id>", methods=["PUT"])
def update_book(id):
    """
    Updates a book in the library
    ---
    parameters:
      - in: path
        name: id
        required: true
        type: integer
        description: The ID of the book to update
      - in: body
        name: book
        required: true
        schema:
          type: object
          properties:
            book_name:
              type: string
              description: The name of the book
            author:
              type: string
              description: The author of the book
            category:
              type: string
              description: The category of the book
            availability:
              type: string
              description: The availability of the book
    responses:
      200:
        description: Book updated successfully
      404:
        description: Book not found
    """
    book = request.get_json()
    update(id, book)
    return "Book updated successfully"
@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_book(id):
    """
    Deletes a book from the library
    ---
    parameters:
      - in: path
        name: id
        required: true
        type: integer
        description: The ID of the book to delete
    responses:
      200:
        description: Book deleted successfully
      404:
        description: Book not found
    """
    delete(id)
    return "Book deleted successfully"
app.run(debug=True)