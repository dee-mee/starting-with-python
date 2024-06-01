import string
import random

pieces = string.ascii_letters +string.hexdigits + string.punctuation
length = 15
password = "".join(random.sample(pieces, length))
print(password)
