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

with open(file_path, 'rb') as file:
        book_arr = pickle.load(file)

for book in book_arr:
        print(book.en_book.book_title)