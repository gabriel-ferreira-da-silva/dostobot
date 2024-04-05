import pickle
import sys

book_path = "C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/assets/books/demons.txt"
book = None

en_file = open( book_path , 'r', encoding="utf-8")
en_lines = en_file.readlines()
en_text=""
a  = len(en_lines)
f=0
b =0
for l in en_lines:
    print(str( 100*b/a) +"%")
    b+=1
    textsize=len(l)
    t=0
    text=""
    while t < textsize:

        if l[t:t+7]=="CHAPTER":
            while l[t]!=".":
                text+=l[t]
                t+=1
            t+=1
            text+="\n\n"
        
        text+=l[t]
        t+=1
    print(text)
    en_text+=text


en_file = open( book_path + "2", 'w', encoding="utf-8")
en_file.write(en_text)
en_file.close()