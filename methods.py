import struct
from constants import RECORD_SIZE

# Pack Records

def pack_record(book_id, title, author, stock):
    title = title.encode().ljust(30).strip()
    author = author.encode().ljust(30).strip()
    return struct.pack('i30s30si', book_id, title, author, stock)
    
# Unpack Records

def unpack_record(record):
    unpacked = struct.unpack('i30s30si', record)
    return {
        "Book ID": unpacked[0],
        "Title": unpacked[1].decode().strip(),
        "Author": unpacked[2].decode().strip(),
        "Stock": unpacked[3]
    }
    
# Add a new book

def add_book(file, book_id, title, author, stock):
    with open(file, 'ab') as f:
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

def update_stock(file, book_id, new_stock):
    with open(file, 'r+b') as f:
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

def search_book(file, title):
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