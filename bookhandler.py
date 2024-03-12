
class BookMark:
    def __init__(self):
        self.book_path=""
        self.book_title=""
        self.book_text=""
        self.chapter_parser=""
        self.current_chapter=""
        self.current_part=""
        self.current_pos=0
        self.last_quote=""
        self.current_quote=""
        self.dots_counted=0
        self.last_update_date=None


class BookHandler:
    def __init__(self):
        self.ru_book=None
        self.en_book=None
        self.last_update_date=None
    
    def find_chapter(self, quote):
        i=quote.find('CHAPTER')
        chapter = None
        if i == -1:
            chapter=None
        else:
            chapter=''
            a=i
            while quote[a]!=' ':
                a+=1
            a+=1
            num =''
            while quote[a]!=' ':
                num+=quote[a]
                a+=1
            chapter = quote[i:a]
        return chapter
    
    def find_part(self, quote):
        i=quote.find('PART')
        chapter = None
        if i == -1:
            chapter=None
        else:
            chapter=''
            a=i
            while quote[a]!=' ':
                a+=1
            a+=1
            num =''
            while quote[a]!=' ':
                num+=quote[a]
                a+=1
            chapter = quote[i:a]
        return chapter
    
    def set_datetime(self, date):
        self.last_update_date = date
    
    def set_english_path(self, path):
        self.en_book = BookMark()
        self.en_book.book_path = path
        en_file = open( self.en_book.book_path , 'r', encoding="utf-8")
        en_lines = en_file.readlines()
        en_text=""
        for l in en_lines:
            en_text+=l
        en_file.close()
        self.en_book.book_text = en_text

    def set_russian_path(self, path):
        self.ru_book = BookMark()
        self.ru_book.book_path = path
        ru_file = open( self.ru_book.book_path , 'r', encoding="utf-8")
        ru_lines = ru_file.readlines()
        ru_text=""
        for l in ru_lines:
            ru_text+=l
        ru_file.close()
        self.ru_book.book_text = ru_text

        
    def getnextquote(self):
        cur_pos = self.en_book.current_pos
        text_size = len(self.en_book.book_text)
        
        quote=""
        book_text = self.en_book.book_text
        for i in range(cur_pos, text_size):
            quote+= book_text[i]
            if book_text[i]==".":
                if len(quote) > 100:
                    # checar se não é três pontos ou citação
                    saida =True
                    while book_text[i+1]==".":
                        quote+="."
                        i+=1
                    
                    if book_text[i+1]=="\"":
                        quote+="\""
                        i+1
                    else:    
                        quote = self.format_quote(quote)
                    
                    self.en_book.current_pos = i+1
                    self.en_book.last_quote = self.en_book.current_quote

                    chapter = self.find_chapter(quote)
                    
                    if chapter != None:
                        self.en_book.current_chapter = chapter
                    
                    chapter = self.find_part(quote)
                    if chapter != None:
                        self.en_book.current_part = chapter

                    self.en_book.current_quote = quote
                    return
        return
    
    def format_quote(self,quote):
        fquote = ""
        for q in quote:
            if q == '\n':
                fquote+=' '
            else:
                fquote+=q
        return fquote
    
    def check_chapter(self, quote):
        
        return 






    
    def status(self):
        print("current pos " + str(self.en_book.current_pos) + "\n")
        print("current chapter: " + str(self.en_book.current_chapter) + "\n")
        print("current part: " + str(self.en_book.current_part) + "\n")
        print("last quote:\n" + str(self.en_book.last_quote) + "\n")
        print("current quote:\n" + str(self.en_book.current_quote) + "\n")
        print("last update:\n"+str( self.last_update_date) +"\n")


    
    def check_chapter(self, quote):
        chapter = "CHAPTER"
        index = quote.find(chapter)
        if index <0:
            return None
        new_chapter = ""
        i = index+6
        while quote[i]==" ":
            i+=1
        while quote[i]!=" ":
            new_chapter+=quote[i]
            i+=1
        
        return (new_chapter, i)

        










