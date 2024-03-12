class Bookparser():
  def __init__(self):
    parserdBook=[]

  def parse(self, text, chapter_parser):
    parsed_strings=[]
    string=""
    text_size= len(text)
    for i in range(0,text_size):
        if text[i]=="." and text[i+1]=="." and text[i+2]==".":
            string+="..."
            i=i+3
            if text[i]=="\"":
                string+="\""
                i+=1
            if text[i]=="\'":
                i+=1
                string+="\""
            parsed_strings.append(string)
            string=""
        string+=text[i]
        if text[i]==".":
           parsed_strings.append(string)
           string=""
    
    return parsed_strings