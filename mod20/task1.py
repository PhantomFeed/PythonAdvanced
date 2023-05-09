from sqlalchemy import Column, Integer, String, Date, Float, Boolean
from sqlalchemy.ext.hybrid import hybrid_property
from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime


app = Flask(__name__)
Base = declarative_base()
engine = create_engine('sqlite:///hw.db')
Session = sessionmaker(bind=engine)
session = Session()


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Authors(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_all_scholarship_students(cls):
        return session.query(Students).filter(Students.scholarship == True).all()

    @classmethod
    def get_all_good_students(cls, score: float):
        return session.query(Students).filter(Students.average_score > score).all()


class ReceivingBook(Base):
    __tablename__ = 'receiving_books'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(Date, nullable=False)
    date_of_return = Column(Date)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @hybrid_property
    def count_days_since_receiving_books(self):
        if self.date_of_return:
            return (self.date_of_return - self.date_of_issue).days
        else:
            return (datetime.date(datetime.now()) - self.date_of_issue).days


@app.before_request
def before_request_func():
    Base.metadata.create_all(engine)


@app.route('/books', methods=['GET'])
def get_books():
    books_list = []
    books = session.query(Books).all()
    for book in books:
        books_list.append(book.to_json())
    return jsonify(books_list), 200


@app.route('/overdue', methods=['GET'])
def get_overdue_books():
    overdue_books = []
    receiving_books = session.query(ReceivingBook).filter(ReceivingBook.date_of_return == None).all()
    for receiving_book in receiving_books:
        if receiving_book.count_days_since_receiving_books > 14:
            overdue_books.append(receiving_book.to_json())
    return jsonify(overdue_books), 200


@app.route('/give_book', methods=['POST'])
def give_book():
    book_id = request.form.get('book_id', type=int)
    student_id = request.form.get('student_id', type=int)
    if not book_id or not student_id:
        return jsonify({'Ошибка': 'Неправильный ID книги или студента'})
    receiving_book = ReceivingBook(book_id=book_id, student_id=student_id, date_of_issue=datetime.now())
    session.add(receiving_book)
    session.commit()
    return jsonify(f'Книга{book_id} удачно выдана студенту{student_id}'), 200


@app.route('/return_book', methods=['POST'])
def return_book():
    book_id = request.form.get('book_id', type=int)
    student_id = request.form.get('student_id', type=int)
    receiving_book = session.query(ReceivingBook).filter(ReceivingBook.book_id == book_id, ReceivingBook.student_id == student_id).one()
    if not receiving_book:
        return jsonify({'Ошибка': 'Не найдена книга по данному ID'}), 400
    receiving_book.date_of_return = datetime.now()
    session.commit()
    return jsonify({'Удачно': 'Книга успешна сдана'}), 200


if __name__ == '__main__':
    app.run(debug=True)
