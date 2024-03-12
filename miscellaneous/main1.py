import pickle
from datetime import datetime
file_path="C:/Users/gab_f/OneDrive/Desktop/projetos/dostobot/var"

bh=None
with open(file_path, 'rb') as file:
    # Deserialize and retrieve the variable from the file
    bh = pickle.load(file)
bh.last_update_date = datetime.now()
bh.getnextquote()
bh.status()

with open(file_path, 'wb') as file:
    # Serialize and write the variable to the file
    pickle.dump(bh, file)
    