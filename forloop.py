import os
from dotenv import load_dotenv

load_dotenv()

N = int(os.getenv("N","0"))

for i in range(N):
    if i%3==0:
        print(i)