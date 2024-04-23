import random
import time
import datetime

s_t=str(time.time())

st=float(s_t)

while st+15>time.time():
  n=random.randrange(100000)
  num=("{:05}".format(n))
  print(num)
  answer=input()
  while answer!=num:
    print("Wrong! One more try.")
    print(num)
    answer=input()
  print("Good!")
print("time over!")