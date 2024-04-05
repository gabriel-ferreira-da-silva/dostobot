import time
import tweepy
import pickle
from bookhandler import BookHandler
from datetime import datetime
import sys

file_path="C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/barr"
last_path="C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/lb"

book_arr=[]

book_title = "Crime and Punishment"
book_path = "C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/books/crime-and-punishment.txt"
book_arr.append((book_title, book_path))

book_title = "Notes from the Underground"
book_path = "C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/books/notes-from-the-underground.txt"
book_arr.append((book_title, book_path))


book_title = "The Devils"
book_path = "C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/books/the-devils.txt"
book_arr.append((book_title, book_path))


book_title = "Brothers Karamazov"
book_path = "C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/books/brothers-karamazov.txt"
book_arr.append((book_title, book_path))


bh_array = []
for b in book_arr:
    print("Loading : " + b[0]+"...")
    book = BookHandler()
    book.set_english_path(b[1])
    book.en_book.book_title = b[0]
    book.last_update_date= datetime.now()
    bh_array.append(book)
    
with open(file_path, 'wb') as file:
                # Serialize and write the variable to the file
                pickle.dump(bh_array, file)

lb=None
with open(last_path, 'wb') as file:
                # Serialize and write the variable to the file
                pickle.dump(lb, file)

