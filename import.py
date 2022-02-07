import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db=scoped_session(sessionmaker(bind=engine))

def main():
    bookdata=open("books.csv")
    reader = csv.reader(bookdata)
    for isbn, title, author, pubyear in reader:
        db.execute("INSERT INTO books (isbn, title, author, pubyear) VALUES (:isbn, :title, :author, :pubyear)", {"isbn": isbn, "title": title, "author": author, "pubyear": pubyear})
        print(f"Added {title} by {author}")
    db.commit()

if __name__=="__main__":
    main()
