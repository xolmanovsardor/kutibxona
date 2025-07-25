import sys
from kutubxona.menyu import print_main
from kutubxona.books import show_books, show_read_status, search_books

def main() -> None:
    while True:
        print_main()
        op = input('> ')

        if op == '1':
            show_books()
        elif op == '2':
            show_read_status()
        elif op == '3':
            search_books()
        elif op == '4':
            print("Dasturdan chiqildi. Xayr!")
            sys.exit(0)
        else:
            print(" Noto‘g‘ri tanlov!")

if __name__ == '__main__':
    main()
