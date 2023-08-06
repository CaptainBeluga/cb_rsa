import json
import secrets
import os

db = dict(json.loads(open("db_BASE.json","r").read()))

body = '{'


keys = []

for k in db:
    keys.append(db[k])

for x in range(len(db) +1):
    if x != 0:
        delimiter = ""

        choice = secrets.choice(keys)
        keys.remove(choice)

        if choice == "":
            choice = " "
        
        elif x != len(db):
            delimiter = ","

        body += f'"{x}" : "{choice}"{delimiter}\n'


body += '}'


filename = "db.json"
open(filename,"w").write(body)

print(f"Successfully Mixed => `{filename}`")

path = __file__[:len(__file__) - len(__file__.split("\\")[-1])]

os.system(f"start {path}")