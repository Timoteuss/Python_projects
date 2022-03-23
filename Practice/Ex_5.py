import os
import time

spisok = []

for adress, dirs, files in os.walk("C:\\Users\Timofey\Documents\My Games\skyrim"):
    for file in files:
        full = os.path.join(adress, file)
        if time.time() - os.path.getctime(full) < 86400:
            if '.txt' in full:
                spisok.append(full)

print(spisok)