import secrets,random
import string

numbers = string.digits

####################################################

#FUNCTIONS

def gen_number():
    while True:

        x = ""

        for _ in range(3):
            x+= secrets.choice(numbers)

        x = int(x)

        if(isPrime(x)):
            return x


def isPrime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True




def mcd(a,b):
    while b:
        a, b = b, a % b
    return a

        

#####################################################

#RSA ALGORITHM 


#Defining P and Q (prime numbers)
p = gen_number()
q = gen_number()

#Security Multiplier
sm = ""

for _ in range(3):
    sm+= secrets.choice(numbers)

sm = int(sm)


#RSA Module
n = p * q

#PHI N
z = (p-1) * (q-1)


#Defining E (public key component)
while True:
    e = ""

    for _ in range(5):
        e+= secrets.choice(numbers)
    
    e = int(e)

    if mcd(e,z) == 1:
        break


#Defining D (private key component)
d = pow(e,-1,z)


#Checking ` (d*e) % z = 1 `
if((d*e) % z == 1):

    PUBLIC_KEY = f"KKK_{e}_{n}_{sm}_KKK"

    PRIVATE_KEY = f"KKK_{d}_{n}_{sm}_KKK"

    from datetime import datetime

    to_write = f"""CB_RSA_2.0 SECRET INFO (generated in date => {datetime.now().isoformat(timespec="seconds")})\n
p => {p}     <--- random prime number 1
q => {q}     <--- random prime number 2

sm => {sm}   <--- Secure Multiplier

n => {n}    <--- RSA Module
z => {z}    <--- phi(n)

e => {e}    <--- public exponent
d => {d}    <--- private exponent


--------------------------------------------------


PUBLIC KEY => {PUBLIC_KEY}

PRIVATE KEY => {PRIVATE_KEY}
    """

    filename = "secrets_info.txt"
    open(filename,"w").write(to_write)

    print(f"\nYour info are stored in `{filename}`")
        
    
else:
    print("\nGenerate Again !")