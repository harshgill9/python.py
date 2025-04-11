
import random
while True:
  num = int(input("Enter your choice - "))
  c_num = random.randint(1, 10)

  if (num == c_num):
    print("Winner")
    break
  else:
    print("Better luck next time")