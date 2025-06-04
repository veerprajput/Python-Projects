from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    def __repr__(self):
        return f'<Book {self.title}>'


# db.drop_all()
db.create_all()

all_books = []

@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = {
            "title": request.form["book_title"],
            "author": request.form["book_author"],
            "rating": request.form["book_rating"]
        }
        all_books.append(book)
        new_book = Book(title=book['title'], author=book['author'], rating=book['rating'])
        db.session.add(new_book)
        db.session.commit()
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

