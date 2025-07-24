class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.read = False   

    def read_book(self):
        self.read = True
        print(f" Siz '{self.title}' kitobini o‘qidingiz!\n")

books = [
    Book("Python OOP", "Ali Karimov"),
    Book("Django Basics", "Zarina Akbarova"),
    Book("AI Intro", "Sardor X.")
]

def show_books():
    print(" Kitoblar ro‘yxati:")
    for i, book in enumerate(books, 1):
        status = " O‘qilgan" if book.read else " O‘qilmagan"
        print(f"{i}. {book.title} - {book.author} [{status}]")

    choice = input("\nQaysi kitobni o‘qimoqchisiz? (raqam yoki Enter bekor qilish): ")
    if choice.strip() == "":
        return
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(books):
            books[idx].read_book()
        else:
            print(" Noto‘g‘ri tanlov!")
    except ValueError:
        print(" Raqam kiriting!")

def show_read_status():
    print(" Kitoblar o‘qilgan / o‘qilmagan holati:")
    for book in books:
        status = " O‘qilgan" if book.read else " O‘qilmagan"
        print(f"- {book.title}: {status}")
def search_books():
    keyword = input(" Qidirish uchun so‘z yoki matn kiriting: ").lower()

    print(" Qidiruv natijalari:")
    found = False
    for book in books:
        if keyword in book.title.lower() or keyword in book.author.lower():
            status = " O‘qilgan" if book.read else " O‘qilmagan"
            print(f"- {book.title} - {book.author} [{status}]")
            found = True

    if not found:
        print(" Hech narsa topilmadi.")
