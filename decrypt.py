import json
import base64
import sys


#PRIVATE KEY => (d,n)
try:
    PRIVATE_KEY = sys.argv[1]

except IndexError:
    filename = __file__.split("\\")[-1]
    print(f"\nUsage => python {filename} <PRIVATE_KEY>")

    exit()


key_split = PRIVATE_KEY.split("_")

d = int(key_split[1])
n = int(key_split[2])
sm = int(key_split[3])


#Reading Chars Scheme
db = dict(json.loads(open("db.json","r").read()))


#Asking Message to Decrypt
m = str(input("\nType your Encrypted MSG => "))

m = base64.b64decode(m).decode().split("_")

message = ""

for val in m:
    if val != "$$$":

        c = round((int(val)**d % n) / sm)
        
        message+= db[str(c)]

print(f"\nORIGINAL MESSAGE => {message}")