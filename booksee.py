import pickle

file_path="C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/barr"

book=None
with open(file_path, 'rb') as file:
        # Deserialize and retrieve the variable from the file
        book = pickle.load(file)

for b in book:
    print(b.en_book.book_text[0:100])
    print("\n\n\n\n\n")