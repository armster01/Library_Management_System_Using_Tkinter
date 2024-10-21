import tkinter as tk
from tkinter import messagebox, simpledialog

class Library:
    def __init__(self):
        self.books = [
            "The Alchemist", "Python Programming", "Data Science with Python",
            "Machine Learning Basics", "Artificial Intelligence"
        ]

    def display_books(self):
        return "\n".join(self.books)

    def add_book(self, book_name):
        self.books.append(book_name)
        return f"'{book_name}' has been added to the library."

    def issue_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            return f"'{book_name}' has been issued. Please return it on time."
        else:
            return f"Sorry, '{book_name}' is not available."

    def return_book(self, book_name):
        self.books.append(book_name)
        return f"Thank you for returning '{book_name}'."

class LibraryManagementGUI:
    def __init__(self, root):
        self.library = Library()
        self.root = root
        self.root.title("Library Management System")

        # Title Label
        title_label = tk.Label(root, text="Library Management System", font=("Arial", 20, "bold"))
        title_label.pack(pady=10)

        # Frame for Buttons
        frame = tk.Frame(root)
        frame.pack(pady=10)

        # Buttons for each operation
        tk.Button(frame, text="Display Books", command=self.display_books, width=15).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame, text="Add Book", command=self.open_add_book_window, width=15).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(frame, text="Issue Book", command=self.issue_book, width=15).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(frame, text="Return Book", command=self.return_book, width=15).grid(row=1, column=1, padx=5, pady=5)

        # Text area to display messages and results
        self.result_text = tk.Text(root, height=10, width=50)
        self.result_text.pack(pady=10)

    def display_books(self):
        books = self.library.display_books()
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Available Books:\n{books}")

    def open_add_book_window(self):
        """Opens a new window for adding a book."""
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Book")

        tk.Label(add_window, text="Enter Book Name:", font=("Arial", 12)).pack(pady=10)
        book_name_entry = tk.Entry(add_window, width=30)
        book_name_entry.pack(pady=5)

        def add_book_action():
            book_name = book_name_entry.get()
            if book_name:
                result = self.library.add_book(book_name)
                self.show_result(result)
                add_window.destroy()
            else:
                messagebox.showwarning("Input Error", "Book name cannot be empty!")

        tk.Button(add_window, text="Add", command=add_book_action, width=10).pack(pady=10)

    def issue_book(self):
        book_name = self.get_input("Issue Book", "Enter the book name:")
        if book_name:
            result = self.library.issue_book(book_name)
            self.show_result(result)

    def return_book(self):
        book_name = self.get_input("Return Book", "Enter the book name:")
        if book_name:
            result = self.library.return_book(book_name)
            self.show_result(result)

    def get_input(self, title, prompt):
        return simpledialog.askstring(title, prompt)

    def show_result(self, result):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementGUI(root)
    root.mainloop()