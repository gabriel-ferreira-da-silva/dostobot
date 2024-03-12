import pickle
import sys

book_path = "C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/assets/books/brothers-karamazov.txt"
book = None

en_file = open( book_path , 'r', encoding="utf-8")
en_lines = en_file.readlines()
en_text=""
a  = len(en_lines)
f=0
for l in en_lines:
    print(str( f*100/a))
    f+=1
    en_text+=l

text=""
en_file.close()
print()
textsize = len(en_text)
t=0

while t < (textsize - 100):
    print(str(t*100/(textsize -200)) +"%")
    if en_text[t] == 'C' and en_text[t+1] == 'h' and en_text[t+2] == 'a' and en_text[t+3] == 'p' and en_text[t+4] == 't' and en_text[t+5] == 'e' and en_text[t+6] == 'r':
        text +="\n\nCHAPTER "
        while en_text[t]!=" ":
            t+=1
        while en_text[t]==" ":
            t+=1
        
        while en_text[t]!=" ":
            text += en_text[t]
            t+=1
        
        text+="\n\n"
        t+=1
    
    text += en_text[t]
    t+=1


en_file = open( book_path + "2", 'w', encoding="utf-8")
en_file.write(text)
en_file.close()