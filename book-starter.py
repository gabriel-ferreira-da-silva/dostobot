import time
import tweepy
import pickle
from bookhandler import BookHandler
from datetime import datetime
import sys

file_path="C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/barr"

book_arr=[]
book_title = "crime and punishment"
book_path = "C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/books/crime-and-punishment.txt"
book_arr.append((book_title, book_path))

book_title = "notes from the underground"
book_path = "C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/books/notes-from-the-underground.txt"

book_arr.append((book_title, book_path))

book_title = "demons"
book_path = "C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/books/demons.txt"
book_arr.append((book_title, book_path))

book_title = "brothers karamazov"
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
