from app import app, db
from flask import request, jsonify
from models import Book

#Get all books

@app.route("/api/books", methods = ["GET"])
def get_books():
    books = Book.query.all() #get all books as py Book obj

    #Convert every book to json to be usable
    res = [book.to_json() for book in books]

    return jsonify(res)

# POST
@app.route("/api/books", methods = ["POST"])
def create_book():
    try:
        #Convert requests to json
        data = request.json

        # Make sure all required fields are provided
        required_fields = ["name", "genre", "desc"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error":f'Missing required field: {field}'}), 400
        #---------------------#
        

        id = data.get("id")
        name = data.get("name")
        genre = data.get("genre")
        desc = data.get("desc")

        #Fetch book cover
        img_url = f"https://avatar.iran.liara.run/public"

        new_book = Book(name = name, genre = genre, desc = desc, img_url = img_url)

        db.session.add(new_book)
        db.session.commit()

        return jsonify({"msg":"Book added"}), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}), 500



# DELETE A BOOK
@app.route("/api/books/<int:id>", methods = ["DELETE"])
def delete_book(id):
    try:
        book = Book.query.get(id)
        if book is None:
            return jsonify({"error":"Book not found"}), 404 
        else:
            print(f"DELETE request for book ID: {id}")
        
        db.session.delete(book)
        db.session.commit()
        return jsonify({"msg":"Book deleted"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}), 500