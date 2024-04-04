import random
import string

chars=string.ascii_letters+string.digits+string.punctuation
length=int(input("ENTER PASSWORD LENGTH: "))
password=''
for i in range(length):
    nxt_char=random.choice(chars)
    password+=nxt_char

print('YOUR RANDOM GENERATED PASSWORD: ',password)
