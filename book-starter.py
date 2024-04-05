import time
import tweepy
import pickle
from bookhandler import BookHandler
from datetime import datetime
import sys

file_path="C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/barr"

book_arr=[]

book_title = "House of the Dead"
book_path = "C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/books/house-of-the-dead.txt"

book = BookHandler()
book.set_english_path(book_path)
book.en_book.book_title = book_title
book.last_update_date= datetime.now()

with open(file_path, 'rb') as file:
        book_arr = pickle.load(file)



book_arr.append(book)
for book in book_arr:
        print(book.en_book.book_title)

file_path="C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/barr3"
with open(file_path, 'wb') as file:
        pickle.dump(book_arr,file)