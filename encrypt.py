import json
import base64
import sys


#PUBLIC KEY => (e,n)
try:
    PUBLIC_KEY = sys.argv[1]

except IndexError:
    filename = __file__.split("\\")[-1]
    print(f"\nUsage => python {filename} <PUBLIC_KEY>")
    
    exit()


key_split = PUBLIC_KEY.split("_")

e = int(key_split[1])
n = int(key_split[2])
sm = int(key_split[3])


#Reading Chars Scheme
db = dict(json.loads(open("db.json","r").read()))

reverse_db = dict(zip(db.values(),db.keys()))


#Asking Message to Encrypt
m = str(input("\nType your MSG => "))

#PUBLIC KEY => (e,n)

encrypted_msg = "$$$_"

#Reading each letter to encrypt
for char in m:

    try:
        enc = int(reverse_db[char])

    except Exception as ex:
        print(f"\n{ex} => not in db scheme | replace by => $")
        enc = int(reverse_db["$_$_$_$_$"])

    #Chiper Text 
    c = int(pow((enc*sm),e) % n)

    encrypted_msg+= f"{c}_"

encrypted_msg+= "$$$"

encrypted_msg = base64.b64encode(encrypted_msg.encode())


print(f"\nENCRYPTED MSG => {encrypted_msg.decode()}")