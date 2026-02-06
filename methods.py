import struct
from constants import RECORD_SIZE, FMT

# Pack Records

def pack_record(book_id, title, author, stock):
    title = title.encode("utf-8").ljust(30, b'\x00')
    author = author.encode("utf-8").ljust(30, b'\x00')
    return struct.pack(FMT, book_id, title, author, stock)
    
# Unpack Records

def unpack_record(record):
    book_id, title_b, author_b, stock = struct.unpack(FMT, record)

    title = title_b.split(b"\x00", 1)[0].decode("utf-8", errors="replace")
    author = author_b.split(b"\x00", 1)[0].decode("utf-8", errors="replace")

    return {
        "Book ID": book_id,
        "Title": title,
        "Author": author,
        "Stock": stock
    }
    
# Add a new book

def add_book(file):
    with open(file, 'ab') as f:
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        stock = int(input("Enter Book Stock: "))
        print("Adding book:", book_id, title, author, stock)
        record = pack_record(book_id, title, author, stock)
        f.write(record)
        
# View all books

def view_books(file):
    with open(file, 'rb') as f:
        while True:
            record = f.read(RECORD_SIZE)
            if not record:
                break
            book = unpack_record(record)
            print(book)

# Update book stock

def update_stock(file):
    with open(file, 'r+b') as f:
        book_id = int(input("Enter Book ID to update: "))
        new_stock = int(input("Enter new stock quantity: "))
        while True:
            pos = f.tell()
            record = f.read(RECORD_SIZE)
            if not record:
                break
            book = unpack_record(record)
            if book["Book ID"] == book_id:
                updated_record = pack_record(book_id, book["Title"], book["Author"], new_stock)
                f.seek(pos)
                f.write(updated_record)
                print(f"Updated stock for Book ID {book_id} to {new_stock}")
                return
        print(f"Book ID {book_id} not found.")
        
# Search for a book by title

def search_book(file):
    title = input("Enter Book Title to search: ")
    with open(file, 'rb') as f:
        while True:
            record = f.read(RECORD_SIZE)
            if not record:
                break
            book = unpack_record(record)
            if book["Title"].lower() == title.lower():
                print(book)
                return
        print(f"Book titled '{title}' not found.")