from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, Float, Boolean, func, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship, backref
from datetime import datetime, timedelta
import csv

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
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    author = relationship('Authors', backref=backref('books', cascade='all, ' 'delete-orphan', lazy='select'))
    students = relationship('ReceivingBook', back_populates='book')

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
    scholarship = Column(Boolean, default=False)
    books = relationship('ReceivingBook', back_populates='student')

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # @classmethod
    # def get_all_scholarship_students(cls):
    #     return session.query(Students).filter(Students.scholarship == True).all()
    #
    # @classmethod
    # def get_all_good_students(cls, score: float):
    #     return session.query(Students).filter(Students.average_score > score).all()


class ReceivingBook(Base):
    __tablename__ = 'receiving_books'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    date_of_issue = Column(DateTime, default=datetime.now)
    date_of_return = Column(DateTime)
    student = relationship('Students', back_populates='books')
    book = relationship('Books', back_populates='students')

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # @hybrid_property
    # def count_days_since_receiving_books(self):
    #     if self.date_of_return:
    #         return (self.date_of_return - self.date_of_issue).days
    #     else:
    #         return (datetime.date(datetime.now()) - self.date_of_issue).days


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
    receiving_book = session.query(ReceivingBook).filter(ReceivingBook.book_id == book_id,
                                                         ReceivingBook.student_id == student_id).one()
    if not receiving_book:
        return jsonify({'Ошибка': 'Не найдена книга по данному ID'}), 400
    receiving_book.date_of_return = datetime.now()
    session.commit()
    return jsonify({'Удачно': 'Книга успешна сдана'}), 200


@app.route('/books/author/<int:author_id>/', methods=['GET'])
def books_by_author(author_id):
    count = 0
    books = session.query(Books).filter(Books.author_id == author_id, Books.id == ReceivingBook.book_id, ReceivingBook.date_of_return == None).all()
    for book in books:
        book = book.to_json()
        count += book['count']
    return f'Количество оставшихся в библиотеке книг этого автора: {count}'


@app.route('/books/not_read_by_student/<int:student_id>', methods=['GET'])
def recommend_books_by_student(student_id):
    books_id = session.query(ReceivingBook.book_id).distinct().filter(ReceivingBook.book_id == Books.id, ReceivingBook.student_id == student_id).all()
    books_id = [item[0] for item in books_id]
    authors_id = session.query(Books.author_id).distinct().filter(ReceivingBook.book_id == Books.id, ReceivingBook.student_id == student_id).all()
    authors_id = [item[0] for item in authors_id]
    books_by_authors = session.query(Books).distinct().filter(Books.author_id.in_(authors_id), Books.id.notin_(books_id)).all()
    books_list = []
    for book in books_by_authors:
        book = book.to_json()
        books_list.append(book['name'])
    return f'Другие произведения этого автора: {str(books_list)[1:-1]}'


@app.route('/books/avgerage', methods=['GET'])
def avgerage_count_books_per_month():
    month = datetime(datetime.now().year, datetime.now().month, 1)
    books_count = session.query(func.count(ReceivingBook.book_id)).filter(
        ReceivingBook.book_id.date_of_issue >= month).scalar()
    students_count = session.query(func.count(Students.id)).scalar()
    average_books_per_month = round(books_count / students_count, 2)
    return f'Среднее количество книг, которые студенты брали в этом месяце: {average_books_per_month}'


@app.route('/most_popular_book', methods=['GET'])
def the_most_popular_book():
    book_id = session.query(func.count(ReceivingBook.book_id)). \
        filter(ReceivingBook.student_id == Students.id, Students.average_score >= 4.0).group_by(ReceivingBook.book_id). \
        order_by(func.count(ReceivingBook.book_id).desc()).limit(1).one()
    book = session.query(Books).filter(Books.id == book_id[0]).one()
    book = book.to_json()
    result = book['name']
    return f'Cамая популярная книга среди студентов со средним баллом больше 4.0: {result}'


@app.route('/top_10_readers', methods=['GET'])
def get_top_readers_students():
    today = datetime.now()
    beginning_of_the_year = datetime(today.year, 1, 1)
    end_of_year = datetime(today.year + 1, 1, 1) - timedelta(days=1)
    top_readers = session.query(Students.name).filter(ReceivingBook.student_id == Students.id, ReceivingBook.date_of_issue > beginning_of_the_year,
                                                      ReceivingBook.date_of_issue < end_of_year).group_by(Students.id).order_by(func.count(ReceivingBook.book_id).desc()).limit(10).all()
    result = ''
    for student in top_readers:
        result += student[0] + ', '
    top_10 = result[:-2]
    return f'ТОП-10 самых читающих студентов в этом году: {top_10}'


@app.route('/get_students_from_csv', methods=['POST'])
def get_students_from_csv():
    students_file = request.files.get('students_file')
    if not students_file:
        return 'Файл "students_file" не найден', 400
    try:
        students_file.save('students.csv')
        students_list = []
        with open('students.csv', 'r', newline='') as file:
            reader = csv.DictReader(file, delimiter=';')
            for student in reader:
                student['scholarship'] = True if student['scholarship'].lower() == 'true' else False
                students_list.append(student)
        session.bulk_insert_mappings(Students, students_list)
    except Exception as e:
        print(e)
        return 'Ошибка при обработке файла "students_file"', 400
    session.commit()
    return 'Студенты из файла "students_file" были успешно добавлены', 200


if __name__ == '__main__':
    app.run(debug=True)
