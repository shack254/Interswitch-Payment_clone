import pytest
import time
import random
import string


date = time.strftime("%y%m%d", time.localtime())
alphabet = string.ascii_uppercase


ref = f"{date}TP{"".join(random.choices(alphabet , k =5))}"

print (ref)
