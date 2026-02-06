import struct
import methods

file_name = 'lib_manager.dat'



def main():
    while True:
        print("=== Library Management System ===")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Stock")
        print("4. Search Book")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        match choice:
            case '1':
                methods.add_book(file_name)
            case '2':
                methods.view_books(file_name)
            case '3':
                methods.update_stock(file_name)
            case '4':
                methods.search_book(file_name)
            case '5':
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
