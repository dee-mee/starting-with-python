import string
import random

pieces = string.ascii_letters + string.values + string.punctuation
length = 10
password = "".join(random.sample(pieces, length))
print(password)
