import tkinter as tk
from tkinter import messagebox
import psql_db

def submit_data():
    book_name = book_name_entry.get()
    author = author_entry.get()
    year_publication = year_publication_entry.get()
    
    if book_name and author and year_publication:
        if psql_db.insert_data(book_name, author, int(year_publication)):
            messagebox.showinfo("Success", "Data inserted successfully!")
            book_name_entry.delete(0, tk.END)
            author_entry.delete(0, tk.END)
            year_publication_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Failed to insert data.")
    else:
        messagebox.showwarning("Input Error", "Please provide all the information.")

def reset_form():
    book_name_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    year_publication_entry.delete(0, tk.END)


# Setup the main application window
root = tk.Tk()
root.title("Book Data Entry Form")

# Create and place the book name label and entry
tk.Label(root, text="Book Name:").grid(row=0, column=0, padx=10, pady=10)
book_name_entry = tk.Entry(root)
book_name_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the author label and entry
tk.Label(root, text="Author:").grid(row=1, column=0, padx=10, pady=10)
author_entry = tk.Entry(root)
author_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the year of publication label and entry
tk.Label(root, text="Year of Publication:").grid(row=2, column=0, padx=10, pady=10)
year_publication_entry = tk.Entry(root)
year_publication_entry.grid(row=2, column=1, padx=10, pady=10)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=3, columnspan=1, pady=20)

reset_button = tk.Button(root, text='Reset', command=reset_form)
reset_button.grid(row=3, columnspan=3, pady=20)

# Run the Tkinter event loop
root.mainloop()
